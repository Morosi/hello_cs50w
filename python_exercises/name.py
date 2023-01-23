import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    name = input("enter your name: ")
    print("")
    print(f"hello, my name is {name}")