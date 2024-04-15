#!/usr/bin/python3
"""Inheritance check module

Check if an object is an instance of a class that inherited
(directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check for inheritance.

    Returns:
        bool: True if obj is an instance of a class that inherited from a_class,
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
