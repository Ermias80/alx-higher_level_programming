#!/usr/bin/python3
"""
    Divides all elements of a matrix by a number.
"""
def matrix_divided(matrix, div):
    """
    Division of matrix function
    args:
    matrix: matrix to be divided
    div: divisor
    Return: new matrix of dividends
    """
# Check if matrix is a list of lists of integers/floats
    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Divide each element of the matrix by div and round to 2 decimal places
    return [[round(val / div, 2) for val in row] for row in matrix]
