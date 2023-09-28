import os
import unittest
from encryptdecrypt import EncryptDecrypt


class TestEncryptedDecrypted(unittest.TestCase):
    def test_set_password(self):
        ed = EncryptDecrypt('random_directory', 'kacper95')
        with open('test_password_file.txt', 'w') as file:
            file.write(ed.password)

        with open('test_password_file.txt') as file:
            content = file.read()

        ed.set_password()

        self.assertIn('kacper95', content)

        os.remove(os.path.join('test_password_file.txt'))


if __name__ == '__main__':
    unittest.main()