#!/usr/bin/python3
"""class MyList that inherits from List"""


class MyList(list):
    """Subclass"""
    def print_sorted(self):
        print(sorted(self))
