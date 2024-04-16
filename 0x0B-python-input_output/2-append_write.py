#!/usr/bin/python3
"""Append to file module"""


def append_write(filename="", text=""):
    """append_write

    Appends text to a file and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        ch = f.write(text)
        return ch
