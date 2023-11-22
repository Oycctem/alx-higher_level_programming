#!/usr/bin/python3
"""defining a class called squre"""

class Square:
    """Class Square"""
    def _init__(self, __size=None):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
