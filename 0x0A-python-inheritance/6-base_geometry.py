#!/usr/bin/python3
"""BaseGeometrymodule"""


class BaseGeometry:
    """Class with unimplemented area method"""

    def area(self):
        """Raise an Exception for unimplemented method"""
        raise Exception("area() is not implemented")
