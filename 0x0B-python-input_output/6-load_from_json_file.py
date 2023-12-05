#!/usr/bin/python3
"""Function that creates an object from a JSON file"""
import json


def load_to_json_file(filename):
    """Returns an object from a JSON file"""
    with open(filename, "r") as file:
        return json.load(file)
