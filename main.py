import os.path


def set_password_if_not_set(directory):
    saved_password = directory.get_password()

    if saved_password is None:
        directory.set_password()
        print('Hasło zostało ustawione')
        return

    return saved_password


def process_mode(parser, directory, saved_password):
    entered_password = parser.password

    if entered_password == saved_password:
        try:
            if parser.mode == 'encrypt':
                directory.save_encrypted_text()
            elif parser.mode == 'decrypt':
                if os.path.exists('result/encrypted_file.txt'):
                    directory.save_decrypted_text()
                else:
                    print('Nie ma pliku z zaszyfrowanym tekstem')
            elif parser.mode == 'append':
                text = input('Podaj jakis wyraz: ')
                file = input('Podaj plik: ')
                print(directory.append_text_to_file(text, file))
            else:
                raise Exception('Nieznany tryb')
        except Exception as error:
            print(str(error))
    else:
        print('Nieprawidłowe hasło')
