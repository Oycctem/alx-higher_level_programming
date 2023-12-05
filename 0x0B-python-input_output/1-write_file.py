#!/usr/bin/python3
"""Function that writes a string to a text file and returns the number of characters written"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
