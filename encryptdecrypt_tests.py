import os
import unittest
from cryptography.fernet import Fernet
from encryptdecrypt import EncryptDecrypt


class TestEncryptedDecrypted(unittest.TestCase):
    def test_set_password(self):
        """
        Test case for the set_password method of the EncryptDecrypt class.

        This test aims to ensure that the set_password method is correctly
        storing the password in the object instance and that it can be retrieved
        and matched with the expected content from a file.

        This test will pass if the assertion in step 5 is True, indicating that
        the password is correctly set and retrieved.
        """
        ed = EncryptDecrypt('random_directory', 'kacper95')
        with open('test_password_file.txt', 'w') as file:
            file.write(ed.password)

        with open('test_password_file.txt') as file:
            content = file.read()

        ed.set_password()

        self.assertIn('kacper95', content)

        os.remove(os.path.join('test_password_file.txt'))

    def test_get_password(self):
        """
        Test case for the get_password method of the EncryptDecrypt class.

        This test validates whether the get_password method is able to
        correctly return the password from the object instance and if it
        matches the expected content from a file.

        This test will pass if the assertion in step 5 is True, signifying that
        the password is correctly retrieved and matches the expected value.
        """
        with open('test_password_file.txt', 'w') as file:
            file.write('kacper95')

        with open('test_password_file.txt') as file:
            content = file.read()

        ed = EncryptDecrypt('random_directory', content)

        result = ed.get_password()

        self.assertEqual('kacper95', result)

        os.remove(os.path.join('test_password_file.txt'))

    def test_create_kdf(self):
        """
        Tests the create_kdf method of the EncryptDecrypt class.

        This test case creates an EncryptDecrypt object with the given
        directory and password, and then calls the create_kdf method
        to generate a key derivation function.
        """
        expected_result = \
            b'\xe2kx\x96\x06\xfb\xc2\x8f\x97\x82\xbf\xc1\xc6\x19\x83$\xcfWFm\x14]Ip\x1a\xe5\xaa\xc1k\xee5\x1d'

        ed = EncryptDecrypt('random_directory', 'kacper95')

        result = ed.create_kdf()

        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 32)

    def test_create_fernet(self):
        """
        Tests the create_fernet method of the EncryptDecrypt class.

        This test case creates an EncryptDecrypt object with the given
        directory and password, and then calls the create_fernet method
        to generate a Fernet object.
        """
        ed = EncryptDecrypt('random_directory', 'kacper95')

        result = ed.create_fernet()

        self.assertIsInstance(result, Fernet)


if __name__ == '__main__':
    unittest.main()
