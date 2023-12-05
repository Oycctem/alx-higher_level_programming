#!/usr/bin/python3
"""Function that adds all arguments to a pythong list and then save them to a file"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
            
    filename = "add_item.json"
    try:
        List = load(filename)
    excpect FileNotFoundError:
        List = []
    List.extend(sys.argv[1:])
    save_to_json_file(List, filename)
