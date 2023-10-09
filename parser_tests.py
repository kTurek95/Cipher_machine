import argparse
import unittest
from unittest.mock import patch
from parser import create_parser


class TestCreateParser(unittest.TestCase):

    @patch('argparse._sys.argv', ['main.py', '-m', 'encrypt', '-p', 'your_password', '-d', 'your_directory'])
    def test_create_parser(self):
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
