#!/usr/bin/python3
"""Function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts the texts"""
    text = ""
    with open(filename) as r:
        for line in r:
            text += l
            if search_string in l:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

