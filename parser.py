"""Module with parser function"""

import argparse


def create_parser(args=None):
    """
    Create and configure an argument parser.

    This function creates an instance of `argparse.ArgumentParser` and configures it
    with the necessary command-line arguments.

    Args:
        args (list): A list of command-line arguments to parse. If not provided,
                     command-line arguments will be parsed from `sys.argv`.

    Returns:
        argparse.Namespace: An object containing the parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description='You can use this program for secure message sending',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-m', '--mode', choices=['encrypt', 'decrypt', 'append'], required=True,
                        help='''Choose what you want to do:
    encrypt given file or files
    decrypt encrypted file or files
    append -> decrypt file, append text and encrypt the file again '''
                        )
    parser.add_argument('-p', '--password', help='Enter password')
    parser.add_argument('-d', '--directoryfile', help='directoryfile with files to process')

    args = parser.parse_args()
    return args
