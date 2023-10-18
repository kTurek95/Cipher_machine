""" Module with test for parser.py module"""

import argparse
import unittest
from unittest.mock import patch
from parser import create_parser


class TestCreateParser(unittest.TestCase):
    """ Test case for the create_parser function."""
    @patch('argparse._sys.argv',
           ['main.py', '-m', 'encrypt', '-ap', 'access_password', '-d', 'your_directory'])
    def test_create_parser(self):
        """
        This test case checks if the create_parser function
        correctly parses command line arguments and
        returns an argparse.Namespace object with the expected attributes and values.

        Attributes:
           - mode: The mode attribute is expected to be 'encrypt'.
           - password: The password attribute is expected to be 'your_password'.
           - directoryfile: The directoryfile attribute is expected to be 'your_directory'.
        """
        args = create_parser()

        self.assertIsInstance(args, argparse.Namespace)

        self.assertTrue(hasattr(args, 'mode'))
        self.assertTrue(hasattr(args, 'accessPassword'))
        self.assertTrue(hasattr(args, 'directoryFile'))

        self.assertEqual(args.mode, 'encrypt')
        self.assertEqual(args.accessPassword, 'access_password')
        self.assertEqual(args.directoryFile, 'your_directory')

    def test_without_password_flag(self):
        """
        Test if the password flag is not set by default.

        When the program is invoked without the '-p' flag, it's expected
        that args.password will be False.
        """
        args = create_parser()
        with patch('sys.argv', ['script_name']):
            self.assertFalse(args.password)

    @patch('getpass.getpass', return_value="test_password")
    def test_password_prompt(self, mock_getpass):
        """
        Test the program's response to the presence of the '-p' flag.

        When the program is invoked with the '-p' flag, it's expected
        that args.password will be True and the function to get the
        password from the user will be called.
        """
        with patch('sys.argv', ['script_name', '-p']):
            args = create_parser()
            self.assertTrue(args.password)


if __name__ == '__main__':
    unittest.main()
