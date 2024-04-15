#!/usr/bin/python3
"""Module for Subclass Check"""


def inherits_from(obj, a_class):
    """Check if obj is a subclass of a_class (but not a direct instance)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
