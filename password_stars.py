MINIMUM_LENGTH = 10


def version_1():
    """Get a password of valid size and print asterisks."""
    password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")

    print('*' * len(password))


# Call the function to execute
version_1()
