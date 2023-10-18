# Cipher_machine

The Cipher machine tool allows the user to encrypt selected directories or files by providing the appropriate path. Thanks to the decryption function, the user has the ability to retrieve the original content. The results are saved in the 'result' directory. Additionally, the tool has an option to add text to one or multiple files depending on the path provided by the user.

## Installation
1. Make sure you have Python 3.x installed on your system.
2. Clone this repository to your local machine.
3. Install the required dependencies by running:
- pip install -r requirements.txt

## Usage
1. Run the main.py script to interact with program:
   - on macOs python3 main.py -p
   - on Windows python main.py -p
2. The program will prompt you to enter a password; the entered password will be invisible. This password will be required in subsequent steps.
3. After entering the password, the program will display a message indicating that the password has been set, and you will be able to proceed further.
4. The options you can select in the terminal can be viewed by entering -h.
5. Launch the program using the command python main.py -ap -m -d:
   - ap is the access password you provided at the beginning.
   - m is the mode you want to choose (encrypt, decrypt, append).
   - d  is the path to the directory or file you want to work on.
6. If you use 'append', the program will prompt you to enter the text you want to add.

## Modules

### main.py
The main module responsible for the program's operation.

### directoryfile.py
Module responsible for working with directories/files.

### encryptdecrypt.py
Module that handles encrypting and decrypting files and saving them in the directory.

### parser.py
Module responsible for the program's operation in the command line using argparse.

## Support
If you encounter any issues with my software, please reach out to me:
- Email: k.turek1995@gmail.com

## Dependencies
To run this software, you'll need the libraries and tools listed in requirements.txt

## License
This project is licensed under the MIT License - 
[![Licencja MIT](https://img.shields.io/badge/Licencja-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

