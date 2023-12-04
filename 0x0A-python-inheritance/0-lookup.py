#!/usr/bin/python3
"""Function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Returns the list of attributes and methods"""
    return list(dir(obj))
