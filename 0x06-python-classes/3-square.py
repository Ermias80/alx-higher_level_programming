#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the Square instance."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
