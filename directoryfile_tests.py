""" Module with tests for Directoryfile class"""

import os
import shutil
import unittest
from directoryfile import DirectoryFile


class TestDirectoryFile(unittest.TestCase):
    """
    Test suite for the DirectoryFile class functionalities.
    """
    def setUp(self):
        """
        Set up the testing environment before each test.

        Creates a temporary directory and files
        for later testing the methods of the DirectoryFile class.
        """
        self.temp_dir = 'temp_test_dir'
        os.mkdir(self.temp_dir)
        with open(os.path.join(self.temp_dir, 'file1.txt'), 'w', encoding='UTF-8') as file:
            file.write("Example content")
        os.mkdir(os.path.join(self.temp_dir, 'temp_dir2'))
        with open(os.path.join(self.temp_dir, 'temp_dir2', 'file2.txt'), 'w', encoding='UTF-8')\
                as file:
            file.write("Another example")

    def tearDown(self):
        """
        Clean up the testing environment after each test, removing temporary files and directories.
        """
        shutil.rmtree(self.temp_dir)

    def test_get_file(self):
        """
        Checks if the method correctly lists all files
        in the specified directory and its subdirectories.
        """
        dir_fil = DirectoryFile(self.temp_dir)
        result = dir_fil.get_file()

        self.assertIn(os.path.join(self.temp_dir, 'file1.txt'), result)
        self.assertIn(os.path.join(self.temp_dir, 'temp_dir2', 'file2.txt'), result)

    def test_text_from_file(self):
        """
        Verifies if the method correctly retrieves text content
        from files in the specified directory.
        """
        dir_fil = DirectoryFile(self.temp_dir)
        result = dir_fil.text_from_file()

        self.assertIn("Example content", result)
        self.assertIn("Another example", result)

    def test_append_text_to_file(self):
        """
        Ensures that the method appends the provided text content
        to the specified file in the directory.
        """
        dir_fil = DirectoryFile(self.temp_dir)
        dir_fil.append_text_to_file('New content', 'file1.txt')

        with open(os.path.join(self.temp_dir, 'file1.txt'), encoding='UTF-8') as file:
            content = file.read()
            self.assertIn('New content', content)


if __name__ == '__main__':
    unittest.main()
