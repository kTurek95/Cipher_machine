from pathlib import Path
from directoryfile import DirectoryFile


class EncryptDecrypt(DirectoryFile):
    def __init__(self, directory: str, password):
        super().__init__(directory)
        self.password = password
        self.key = b'!123!321!'
        self.new_folder = Path('result')
        self.password_file = "password.txt"

    def set_password(self):
        with open(self.password_file, 'w') as file:
            file.write(self.password)

    def get_password(self):
        try:
            with open(self.password_file, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            return None


