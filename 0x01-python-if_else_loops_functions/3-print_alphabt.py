#!/usr/bin/python3
for ascii in range(ord('a'), ord('z') + 1):
    lowercase = chr(ascii)
    if lowercase not in ('q', 'e'):
        print("{}".format(lowercase), end='')
