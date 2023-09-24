""" This module defines the DirectoryFile class for performing file operations in a specified directory. """

from os import walk
from pathlib import Path


class DirectoryFile:
    """
    Class representing file operations in a specified directory.

    Attributes:
        directory (str): The path to the directory where file operations will be performed.

    Methods:
        get_file(): Returns a list of paths to text files in the specified directory.
        text_from_file(): Reads the content of text files in the directory and concatenates them into a single text.
        append_text_to_file(text, file_name): Appends the specified text to an existing file with the given name.
    """
    def __init__(self, directory: str):
        """
        Initializes the DirectoryFile object.

        Args:
            directory (str): The path to the directory where file operations will be performed.
        """
        self.directory = directory

    def get_file(self):
        """
        Returns a list of paths to text files in the specified directory.

        Returns:
            List[str]: List of paths to text files (files with a .txt extension).
        """
        outputs = []
        for path, directories, files in walk(self.directory):
            for file in files:
                if file.endswith('.txt'):
                    outputs.append(f'{path}/{file}')

        return outputs

    def text_from_file(self):
        """
       Reads the content of text files in the directory and concatenates them into a single text.

       Returns:
           str: Combined text from the text files in the directory.
       """
        texts = []
        for file in self.get_file():
            with open(f'{file}') as output:
                text = "\n".join(text.strip() for text in output.readlines())
                texts.append(text)

        combined_texts = "\n".join(texts)
        return combined_texts

    def append_text_to_file(self, text, file_name):
        """
        Appends the specified text to an existing file with the given name.

        Args:
            text (str): The text to add to the file.
            file_name (str): The name of the file to which the text should be added.

        Returns:
            str: Success message or file not found information.
        """
        samples = self.get_file()
        for sample in samples:
            sample_path = Path(sample)
            if sample_path.name == file_name:
                with open(sample_path, 'a') as output:
                    output.write(f'{text}\n')
                return None
        return f'File {file_name} does not exist.'
