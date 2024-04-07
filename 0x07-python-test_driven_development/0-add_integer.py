#!/usr/bin/python3
"""
    Adds two integers
    Args:
        a (int): The first integer
        b (int): The second integer, defaults to 98
"""
def add_integer(a, b=98):
    """
    Returns:
        int: The addition of a and b
    Raises:
        TypeError: If a or b is not an integer or float
        TypeError: a must be an integer
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
