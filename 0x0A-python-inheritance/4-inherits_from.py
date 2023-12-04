#!/usr/bin/python3
"""Functon that returns True if the object is an instance of a class that inherited form specifie class"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class"""
    return type(obj) != a_class and issubclass(type(obj), a_class)
