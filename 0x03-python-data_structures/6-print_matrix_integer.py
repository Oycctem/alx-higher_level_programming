#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for i in r:
            print("{:d}".format(i), end=" " if i != r[-1] else "\n")
        print()
