#!/usr/bin/python3
"""Function that writes a string to a text file and returns the number of characters written"""


def read_file(file="", text=""):
    """writes a string to a text file"""
    with open(file, "w", encoding="utf-8") as file:
        print(file.write(text))
