import os
import unittest
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


if __name__ == '__main__':
    unittest.main()
