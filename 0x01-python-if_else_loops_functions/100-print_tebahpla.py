#!/usr/bin/python3
for ascii in range(ord('z'), ord('a') - 1, -1):
    character = chr(ascii)
    if ascii % 2 == 1:
        character = character.upper()
    print(character, end='')
