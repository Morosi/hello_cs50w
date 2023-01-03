# Generate strong passwords that are difficult to break
import datetime
import time
import random

def Password():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbol = "!@#$%^&*()_+-=[]{}/<>;:|\?~`"

    user_for = lower_case + upper_case + number + symbol

    length_for_password = 10
    password = "".join(random.sample(user_for,length_for_password))
    print(f"Your Generated Password is:\n{password}\n")

while 5 < 7:
    Password()
    time.sleep(2)