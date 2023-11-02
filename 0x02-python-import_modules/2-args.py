#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_of_arg = len(sys.argv) - 1
    count = len(sys.argv)

    if count == 1:
        print("{} arguments.".format(num_of_arg))
    elif count == 2:
        print("{} argument:".format(num_of_arg))
    else:
        print("{} arguments:".format(num_of_arg))
    i = 1
    for arg in sys.argv[1:]:
        print("{}: {}".format(i, arg))
        i += 1
