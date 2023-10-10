""" Module with test for parser.py module"""

import argparse
import unittest
from unittest.mock import patch
from parser import create_parser


class TestCreateParser(unittest.TestCase):
    """ Test case for the create_parser function."""
    @patch('argparse._sys.argv',
           ['main.py', '-m', 'encrypt', '-p', 'your_password', '-d', 'your_directory'])
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
        self.assertTrue(hasattr(args, 'password'))
        self.assertTrue(hasattr(args, 'directoryfile'))

        self.assertEqual(args.mode, 'encrypt')
        self.assertEqual(args.password, 'your_password')
        self.assertEqual(args.directoryfile, 'your_directory')


if __name__ == '__main__':
    unittest.main()
