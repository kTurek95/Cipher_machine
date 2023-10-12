"""
Module for directory encryption and decryption.

This module provides functionality for setting passwords for a directory,
performing encryption and decryption operations on the directory,
and controlling the main program flow.

Functions:
    - set_password_if_not_set(directory):
        Sets a password for the directory if it is not already set.
    - process_mode(parser, directory, saved_password):
        Processes the specified mode of operation for a directory.
    - main(): Main function for performing directory operations based on command-line arguments.

"""

import os.path
from parser import create_parser
from encryptdecrypt import EncryptDecrypt


def set_password_if_not_set(directory):
    """
    Sets a password for the given directory if one is not already set.

    Args:
        directory (Directory): The directory for which to set the password.

    Returns:
        str or None: If a password was set, returns 'The password has been set';
        otherwise, returns the saved password (or None if no password is set).
    """
    saved_password = directory.get_password()

    if saved_password is None:
        directory.set_password()
        print('The password has been set')
        return

    return saved_password


def process_mode(parser, directory, saved_password):
    """
    Process the specified mode of operation for a directory.

    Params:
        parser (argparse.ArgumentParser): The argument parser to parse command-line arguments.
        directory (Directory): The directory to operate on.
        saved_password (str): The saved password for the directory.
    """
    entered_password = parser.password

    if entered_password == saved_password:
        try:
            if parser.mode == 'encrypt':
                directory.save_encrypted_text()
            elif parser.mode == 'decrypt':
                if os.path.exists('result/encrypted_file.txt'):
                    directory.save_decrypted_text()
                else:
                    print('There is no file with encrypted text')
            elif parser.mode == 'append':
                text = input('Write what you want to add to the file: ')
                file = input('Provide the file: ')
                print(directory.append_text_to_file(text, file))
            else:
                raise Exception('Unknown mode')
        except Exception as error:
            print(str(error))
    else:
        print('Wrong password')


def main():
    """
    Main function for performing directory operations based on command-line arguments.
    This function creates a command-line argument parser,
     initializes a directory for encryption/decryption,
    checks if a password is already set or sets it if not,
     and then processes the specified mode of operation.
    """
    parser = create_parser()
    directory = EncryptDecrypt(parser.directoryfile, parser.password)

    saved_password = set_password_if_not_set(directory)

    process_mode(parser, directory, saved_password)


if __name__ == '__main__':
    main()
