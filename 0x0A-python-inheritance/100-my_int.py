#!/usr/bin/python3
"""a class that inherits from int"""


class MyInt(int):
    """integer class inverting == and != operators"""

    def __eq__(self, value):
        """Override == to behave like !="""
        return self.real != value

    def __ne__(self, value):
        """Override != to behave like =="""
        return self.real == value
