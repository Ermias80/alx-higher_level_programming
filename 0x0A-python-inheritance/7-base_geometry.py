#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """Raises an Exception since area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
