#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if 'a' <= character <= 'z':
            character = chr(ord(character) - 32)
        print("{}".format(character), end='')
    print()
