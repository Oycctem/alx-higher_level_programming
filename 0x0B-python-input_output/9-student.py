#!/usr/bin/python3
"""a class that defines a Student"""


class Student:
    """dictionary representation of Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation"""
        return self.__dict__
