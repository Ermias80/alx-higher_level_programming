#!/usr/bin/python3
"""Module: MyList

Defines a class MyList that inherits from the list class
"""


class MyList(list):
    """MyList class

    Inherits from list and provides custom functionality.
    """

    def print_sorted(self):
        """Prints the list in sorted order

        Sorts the list in ascending order and prints it.
        """
        print(sorted(self))
