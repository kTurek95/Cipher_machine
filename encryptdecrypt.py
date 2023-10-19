""" Module with encryptdecrypt class """

import base64
import os
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from directoryfile import DirectoryFile


class EncryptDecrypt(DirectoryFile):
    """
   The EncryptDecrypt class is used for encrypting and decrypting files in a specified directory.

   Args:
       directory (str): The path to the directory where files will be encrypted and decrypted.
    """
    def __init__(self, directory: str):
        super().__init__(directory)
        self.key = b'!123!321!'
        self.new_folder = Path('result')
        self.password_file = "password.txt"

    def set_password(self, password):
        """
        Sets the password in the 'password.txt' file.

        Args:
            password (str): The password to set in the file.
        """
        with open(self.password_file, 'w', encoding='utf8') as file:
            file.write(password)

    def get_password(self):
        """
        Retrieves the stored password from the 'password.txt' file.

        Returns:
            str or None: The stored password if it exists, or None if the file is not found.
        """
        try:
            with open(self.password_file, 'r', encoding='utf8') as file:
                return file.read().strip()
        except FileNotFoundError:
            return None

    def create_kdf(self):
        """
        Creates a Key Derivation Function (KDF)
         using the PBKDF2-HMAC algorithm with specified parameters.

        Returns:
            bytes: The derived key based on the provided key and salt.
        """
        salt = b'123qwerty123'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000
        )
        return kdf.derive(self.key)

    def create_fernet(self):
        """
        Creates a Fernet encryption object using a derived key.

        Returns:
            Fernet: A Fernet encryption object initialized with a derived key.
        """
        fernet = Fernet(base64.urlsafe_b64encode(self.create_kdf()))
        return fernet

    def encrypt(self):
        """
        Encrypts text from a file using Fernet encryption.

        Returns:
            list of bytes: A list of encrypted words from the file.
        """
        fernet = self.create_fernet()
        encrypted_words = []
        for text in self.text_from_file().split():
            encrypted_word = fernet.encrypt(text.encode('utf-8'))
            encrypted_words.append(encrypted_word)

        return encrypted_words

    def decrypt(self):
        """
        Decrypts encrypted words using Fernet decryption.

        Returns:
           list of str: A list of decrypted words from the encrypted data.
        """
        fernet = self.create_fernet()
        decrypted_words = []
        for text in self.encrypt():
            decrypted_word = fernet.decrypt(text).decode('utf-8')
            decrypted_words.append(decrypted_word)

        return decrypted_words

    def save_encrypted_text(self):
        """
        Saves encrypted text to a file in the 'result' folder.

        The file is named based on the directory path, replacing '/' with '_',
        and has a '.encrypt' extension.

        """
        file_name = f'{self.directory.replace("/", "_")}.encrypt'
        file_path = os.path.join(self.new_folder, file_name)
        if not self.new_folder.exists():
            self.new_folder.mkdir(parents=True)
        with open(file_path, 'w', encoding='utf8') as file:
            for text in self.encrypt():
                file.write(f'{text}\n')

    def save_decrypted_text(self):
        """
        Saves decrypted text to a file in the 'result' folder.

        The file is named based on the directory path, replacing '/' with '_',
        and has a '.decrypt' extension.

        """
        file_name = f'{self.directory.replace("/", "_")}.decrypt'
        file_path = os.path.join(self.new_folder, file_name)
        if not self.new_folder.exists():
            self.new_folder.mkdir(parents=True)
        with open(file_path, 'w', encoding='utf8') as file:
            for text in self.decrypt():
                file.write(f'{text}\n')
