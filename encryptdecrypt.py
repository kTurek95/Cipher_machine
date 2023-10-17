import base64
import os
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from directoryfile import DirectoryFile


class EncryptDecrypt(DirectoryFile):
    def __init__(self, directory: str):
        super().__init__(directory)
        self.key = b'!123!321!'
        self.new_folder = Path('result')
        self.password_file = "password.txt"

    def set_password(self, password):
        with open(self.password_file, 'w') as file:
            file.write(password)

    def get_password(self):
        try:
            with open(self.password_file, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            return None

    def create_kdf(self):
        salt = b'123qwerty123'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000
        )
        return kdf.derive(self.key)

    def create_fernet(self):
        fernet = Fernet(base64.urlsafe_b64encode(self.create_kdf()))
        return fernet

    def encrypt(self):
        fernet = self.create_fernet()
        encrypted_words = []
        for text in self.text_from_file().split():
            encrypted_word = fernet.encrypt(text.encode('utf-8'))
            encrypted_words.append(encrypted_word)

        return encrypted_words

    def decrypt(self):
        fernet = self.create_fernet()
        decrypted_words = []
        for text in self.encrypt():
            decrypted_word = fernet.decrypt(text).decode('utf-8')
            decrypted_words.append(decrypted_word)

        return decrypted_words

    def save_encrypted_text(self):
        file_name = f'{self.directory.replace("/", "_")}.encrypt'
        file_path = os.path.join(self.new_folder, file_name)
        if not self.new_folder.exists():
            self.new_folder.mkdir(parents=True)
        with open(file_path, 'w') as file:
            for text in self.encrypt():
                file.write(f'{text}\n')

    def save_decrypted_text(self):
        file_name = f'{self.directory.replace("/", "_")}.decrypt'
        file_path = os.path.join(self.new_folder, file_name)
        if not self.new_folder.exists():
            self.new_folder.mkdir(parents=True)
        with open(file_path, 'w') as file:
            for text in self.decrypt():
                file.write(f'{text}\n')
