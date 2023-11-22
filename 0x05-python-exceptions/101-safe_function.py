#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        i = fct(*args)
        return i
    except Exception as exception:
        sys.stderr.write(f"Exception: {exception}\n")
        return None
