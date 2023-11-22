#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as exception:
        sys.stderr.write(f"Exception: {exception}\n")
    return False
