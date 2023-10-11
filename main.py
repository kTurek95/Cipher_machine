def set_password_if_not_set(directory):
    saved_password = directory.get_password()

    if saved_password is None:
        directory.set_password()
        print('Hasło zostało ustawione')
        return

    return saved_password
