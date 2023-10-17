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
import getpass
from parser import create_parser
from encryptdecrypt import EncryptDecrypt


def set_password_if_not_set(directory):
    password_from_user = getpass.getpass('Enter the password: ')
    return directory.set_password(password_from_user)


def process_mode(parser, directory):
    """
    Process the specified mode of operation for a directory.

    Params:
        parser (argparse.ArgumentParser): The argument parser to parse command-line arguments.
        directory (Directory): The directory to operate on.
    """
    try:
        if parser.directoryFile is None:
            print('You forgot to add a directory path.')
        elif not os.path.exists(parser.directoryFile):
            print('The specified directory does not exist')
        elif parser.mode == 'encrypt':
            if not os.path.exists(f'result/{parser.directoryFile.replace("/", "_")}.encrypt'):
                directory.save_encrypted_text()
            else:
                print('Encrypted file already exists')
        elif parser.mode == 'decrypt':
            if os.path.exists(f'result/{parser.directoryFile.replace("/", "_")}.encrypt'):
                if not os.path.exists(f'result/{parser.directoryFile.replace("/", "_")}.decrypt'):
                    directory.save_decrypted_text()
                else:
                    print('Decrypted file already exists')
            else:
                print('There is no file with encrypted text')
        elif parser.mode == 'append':
            text = input('Write what you want to add to the file: ')
            print(directory.append_text_to_file(text, parser.directoryFile))
        elif parser.mode is None:
            print('Add -m with one of the given options [encrypt, decrypt, append]')
        else:
            raise Exception('Unknown mode')
    except Exception as error:
        print(str(error))


def main():
    """
    Main function for performing directory operations based on command-line arguments.
    This function creates a command-line argument parser,
     initializes a directory for encryption/decryption,
    checks if a password is already set or sets it if not,
     and then processes the specified mode of operation.
    """
    parser = create_parser()
    directory = EncryptDecrypt(parser.directoryFile)

    if not os.path.exists('password.txt'):
        if parser.password:
            set_password_if_not_set(directory)
            print('Password has been set')
        elif not parser.password:
            print('You must provide a password using -p')
    elif os.path.exists('password.txt') and parser.password:
        print('The password has already been set')
    else:
        access_password = directory.get_password()
        if parser.accessPassword == access_password:
            process_mode(parser, directory)
        else:
            print('Wrong password')


if __name__ == '__main__':
    main()
