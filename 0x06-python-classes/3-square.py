#!/usr/bin/python3
"""defining a class called Square"""


class Square:
    """Class Square"""
    def __init__(self, size=None):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)
