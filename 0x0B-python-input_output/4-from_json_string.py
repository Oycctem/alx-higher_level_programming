#!/usr/bin/python3
"""Function that returns an object represented by JSON string"""
import json


def from_json_string(my_str):
    """returs an object represented by JSON"""
    return json.loads(my_str)
