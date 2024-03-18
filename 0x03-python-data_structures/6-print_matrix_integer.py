#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_idx, num in enumerate(row):
            if col_idx != len(row) - 1:
                print("{:d} ".format(num), end="")
            else:
                print("{:d}".format(num))
    if not matrix:
        print()
