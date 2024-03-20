#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = []
    for line in matrix:
        sq.append([c**2 for c in line])
    return sq
