#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    NumOfArguments = len(sys.argv) - 1
    count = len(sys.argv)
    
    if count == 1:
        print("{} arguments.".format(NumOfArguments))
    elif count == 2:
        print("{} argument:".format(NumOfArguments))
    else:
        print("{} arguments:".format(NumOfArguments))
    for i in range(count - 1):
        print("{}: {}".format(i + 1, sys.argv[i +1])))
