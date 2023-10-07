"""
Tests for the EncryptDecrypt module.

This module contains a suite of unit tests for the EncryptDecrypt class,
which is responsible for encryption and decryption functionalities. The tests aim
to ensure that the methods of the class operate correctly and as expected.

The tests cover:
- Setting and retrieving the password.
- Creating the key derivation function (KDF) and a Fernet object.
- The process of encrypting and decrypting text.
- Saving encrypted and decrypted text.

To run the tests, execute this script directly as the main module.

Example:
    $ python3 encryptdecrypt_tests.py
"""


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
        encrypt_decrypt = EncryptDecrypt('random_directory', 'kacper95')
        with open('test_password_file.txt', 'w', encoding='utf8') as file:
            file.write(encrypt_decrypt.password)

        with open('test_password_file.txt', encoding='utf8') as file:
            content = file.read()

        encrypt_decrypt.set_password()

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
        with open('test_password_file.txt', 'w', encoding='utf8') as file:
            file.write('kacper95')

        with open('test_password_file.txt', encoding='utf8') as file:
            content = file.read()

        encrypt_decrypt = EncryptDecrypt('random_directory', content)

        result = encrypt_decrypt.get_password()

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
            b'\xe2kx\x96\x06\xfb\xc2\x8f\x97\x82\xbf\xc1\
            xc6\x19\x83$\xcfWFm\x14]Ip\x1a\xe5\xaa\xc1k\xee5\x1d'

        encreypt_decrypt = EncryptDecrypt('random_directory', 'kacper95')

        result = encreypt_decrypt.create_kdf()

        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 32)

    def test_create_fernet(self):
        """
        Tests the create_fernet method of the EncryptDecrypt class.

        This test case creates an EncryptDecrypt object with the given
        directory and password, and then calls the create_fernet method
        to generate a Fernet object.
        """
        encrypt_decrypt = EncryptDecrypt('random_directory', 'kacper95')

        result = encrypt_decrypt.create_fernet()

        self.assertIsInstance(result, Fernet)

    def test_encrypt(self):
        """
        Test the encryption functionality of the EncryptDecrypt class.

        This function creates a temporary directory, writes sample text data to a file
        in that directory, initializes an EncryptDecrypt instance, and tests whether
        the encryption process returns the expected results.
        """
        temp_dir = 'random_directory'
        os.mkdir(temp_dir)
        sample_text = ['kacper', 'kamil', 'oliwia']
        with open(os.path.join(temp_dir, 'test_file.txt'), 'w', encoding='utf-8') as file:
            for text in sample_text:
                file.write(f'{text}\n')

        encrypt_decrypt = EncryptDecrypt('random_directory', 'kacper95')
        result = encrypt_decrypt.encrypt()

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)

        for item in result:
            self.assertIsInstance(item, bytes)

        os.remove(os.path.join(temp_dir, 'test_file.txt'))
        os.rmdir(temp_dir)

    def test_decrypt(self):
        """
        Test the decryption functionality of the EncryptDecrypt class.

        This function creates a temporary directory, writes sample text data to a file
        in that directory, initializes an EncryptDecrypt instance, encrypts and then
        decrypts the data, and tests whether the decrypted data matches the original.
        """
        temp_dir = 'random_directory1'
        os.mkdir(temp_dir)
        sample_text = ['kacper', 'kamil', 'oliwia']

        with open(os.path.join(temp_dir, 'test_file.txt'), 'w', encoding='utf-8') as file:
            for text in sample_text:
                file.write(f'{text}\n')

        encrypt_decrypt = EncryptDecrypt('random_directory1', 'kacper95')
        encrypt_decrypt.encrypt()
        result = encrypt_decrypt.decrypt()

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        self.assertEqual(result, sample_text)

        for item in result:
            self.assertIsInstance(item, str)

        os.remove(os.path.join(temp_dir, 'test_file.txt'))
        os.rmdir(temp_dir)

    def test_save_encrypted_text(self):
        """
        Test the save_encrypted_text() function in the EncryptDecrypt class.

        Creates a temporary directory 'random_directory2' and a text file with sample data.
        Then, uses the EncryptDecrypt class to encrypt the file and save the encrypted text.
        After saving the text, it checks if the output file 'result/encrypted_file.txt' exists.
        Reads the contents of the encrypted file and verifies that each line is of type bytes
        and that the number of lines is 3.
        Finally, it removes all temporary files and directories.
        """
        temp_dir = 'random_directory2'
        os.mkdir(temp_dir)
        sample_text = ['kacper', 'kamil', 'oliwia']
        with open(os.path.join(temp_dir, 'test_file.txt'), 'w', encoding='utf-8') as file:
            for text in sample_text:
                file.write(f'{text}\n')

        encrypt_decrypt = EncryptDecrypt('random_directory2', 'kacper95')
        encrypt_decrypt.encrypt()
        encrypt_decrypt.save_encrypted_text()

        self.assertTrue(os.path.exists('result/encrypted_file.txt'))

        with open('result/encrypted_file.txt', 'rb') as file:
            lines = file.readlines()
            for line in lines:
                self.assertIsInstance(line.strip(), bytes)
                self.assertEqual(len(lines), 3)

        os.remove(os.path.join(temp_dir, 'test_file.txt'))
        os.remove(os.path.join('result/encrypted_file.txt'))
        if os.path.exists('result'):
            for file_name in os.listdir('result'):
                file_path = os.path.join('result', file_name)
                os.remove(file_path)
            os.rmdir('result')
        os.rmdir(temp_dir)

    def test_save_decrypted_text(self):
        """
       Test the save_decrypted_text() function in the EncryptDecrypt class.

       This function creates a temporary directory, writes sample texts from a list to a file,
       then uses EncryptDecrypt to encrypt, decrypt, and save the decrypted text to a file.
       It checks whether the output file exists, contains the correct text data, and whether
       the number of lines in the output file matches the number of sample texts.

       """
        temp_dir = 'random_directory3'
        os.mkdir(temp_dir)
        sample_text = ['kacper', 'kamil', 'oliwia']

        with open(os.path.join(temp_dir, 'test_file.txt'), 'w', encoding='utf-8') as file:
            for text in sample_text:
                file.write(f'{text}\n')

        encrypt_decrypt = EncryptDecrypt('random_directory3', 'kacper95')
        encrypt_decrypt.encrypt()
        encrypt_decrypt.decrypt()
        encrypt_decrypt.save_decrypted_text()

        self.assertTrue(os.path.exists('result/decrypted_file.txt'))

        with open('result/decrypted_file.txt', 'r', encoding='utf8') as file:
            lines = file.readlines()
            for line in lines:
                self.assertIsInstance(line.strip(), str)
                self.assertEqual(len(lines), 3)

        lines_stripped = [line.strip() for line in lines]
        self.assertEqual(lines_stripped, sample_text)

        os.remove(os.path.join(temp_dir, 'test_file.txt'))
        os.rmdir(temp_dir)


if __name__ == '__main__':
    unittest.main()
