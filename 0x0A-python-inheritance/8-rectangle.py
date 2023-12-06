#!/usr/bin/python3
"""a class Rectangle that inherits from basegeometry"""
BaseGeometry = __import__("7-base_geametry").BaseGeometry



class Rectangle(BaseGeometry):
    """class that defines rectangle using basegeometry"""
    def __init__(self, width, height):
        """rectangle"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
