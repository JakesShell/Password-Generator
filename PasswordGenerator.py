import random

def generate_password(length=16):
    # Define character sets
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    special_characters = '012456789/*-+_-@#$%&*'

    # Initialize an empty password
    new_password = ''

    for _ in range(length):  # Loop for the desired password length
        # Randomly decide whether to add a lowercase letter or a special character
        if random.randint(0, 1) == 0:
            new_password += random.choice(lowercase)
        else:
            new_password += random.choice(special_characters)

    return new_password

if __name__ == "__main__":
    password = generate_password()
    print("Here is your new password, my Liege:", password)
