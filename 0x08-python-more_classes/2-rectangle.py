#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """rectangle"""
    def __init__(self, width=0, height=0):
        """__init__: instance method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """the width getter function"""
        return self.__width

    @width.setter
    def width(self, value):
        """the width setter function"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the height getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """the width setter fucntion"""
        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """the area"""
        return self.__width * self.__height

    def perimeter(self):
        """the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
