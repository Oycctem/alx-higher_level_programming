#!/usr/bin/python3
"""Function returns True if the object is an instance of or if the object is an instance of class that inherited from"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance"""
    return isinstance(obj, a_class)
