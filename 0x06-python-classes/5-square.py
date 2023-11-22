#!/usr/bin/python3
"""Defining a class called Square"""


class Square:
    """Class Square"""
    def __init__(self, size=None):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if type(val) != int:
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        x = self.__size):
        for i in range(x):
            for g in range(x):
                print("#", end="")
            print()
