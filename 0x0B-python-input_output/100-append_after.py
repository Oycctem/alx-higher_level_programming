#!/usr/bin/python3
"""Function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts the texts"""
    text = ""
    with open(filename) as read:
        for line in read:
            text += line
            if search_string in line:
                text += NewStr
    with open(filename, "w") as write:
        w.write(text)

