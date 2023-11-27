#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """rectangle"""
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """__init__: instance method"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """Rectangle as a string"""
        if self.__height == 0 or self.__width == 0:
            return ""
        symbol = str(self.print_symbol)
        pattern = self.__width * symbol
        rectangle = ""
        for i in range(self.__height):
            rectangle += pattern
            if i == self.__height - 1:
                break
            rectangle += '\n'
        return rectangle

    def __repr__(self):
        """string representation"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """deleting the Rectangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect2):
        """the biggest rectangle based on it's area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 >= area2:
            return rect_1
        else:
            return rect_2
