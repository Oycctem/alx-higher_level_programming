#!/usr/bin/python3
"""Function that appends a string at the end of a text file and returns the number of characters added"""


def append_write(filename="", text=""):
    """appends a string at the end of text file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
