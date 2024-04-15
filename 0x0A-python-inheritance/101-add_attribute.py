#!/usr/bin/python3
"""
Defines the MyInt class
"""


class MyInt(int):
    """A rebel version of an integer, perfect for opposite day!"""

    def __new__(cls, *args, **kwargs):
        """Create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Override the equality comparison operator"""
        return int(self) != other

    def __ne__(self, other):
        """Override the inequality comparison operator"""
        return int(self) == other
