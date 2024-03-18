#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        row = 0
        while row < len(matrix):
            col_idx = 0
            while col_idx < len(matrix[row]):
                if col_idx != len(matrix[row]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[row][col_idx]), end=endspace)
                col_idx += 1
            print()
            row += 1
