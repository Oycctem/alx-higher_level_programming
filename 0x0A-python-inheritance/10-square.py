#!/usr/bin/python3
"""a class that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """width, height"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
