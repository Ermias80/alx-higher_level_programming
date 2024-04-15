#!/usr/bin/python3
"""Lookup Module

Returns a list of available attributes and methods of an object
"""


def lookup(obj):
    """lookup function

    Args:
        obj (object): the object to list its attributes

    Returns:
        list: list of attributes and methods
    """
    return dir(obj)
