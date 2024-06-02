MINIMUM_LENGTH = 10


def get_password():
    password = input(f"Password too short! It must be at least {MINIMUM_LENGTH} characters.")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter a password of at least {MINIMUM_LENGTH} characters: ")

    print('*' * len(password))


# Call the function to execute
get_password()
