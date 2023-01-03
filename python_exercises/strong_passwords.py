# Generate strong passwords that are difficult to break
import datetime
import time
import random
import string

# function that generates password string
def generate_password():
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(password_chars) for i in range(10))
    return password


# function that checks the strength of the password string

def check_password_strength(password):
    strength = 0
    common_passwords = ["password", "123456", "qwerty", "letmein", "monkey"]
    if password in common_passwords:
        return "This is too common and not strong enough"
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()_+={}[]<>?/~`" for char in password):
        strength += 1
    if strength == 5:
        print("This is a strong password\n")
        return "This is a strong password"
    if strength >= 3:
        print("This password is medium strength\n")
        return "This password is medium strength"
    else:
        print("You password is weak\n")
        return "This is a weak password"

while 5 > 3:
    password = generate_password()
    print(password)
    check_password_strength(password)
    time.sleep(2)

