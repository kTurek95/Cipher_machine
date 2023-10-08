import argparse


def create_parser(args=None):
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