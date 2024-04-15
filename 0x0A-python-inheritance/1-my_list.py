#!/usr/bin/python3
"""MyList Module

Defines a class MyList that inherits from list
"""


class MyList(list):
    """MyList class

    Inherits from list and provides additional functionality.
    """

    def print_sorted(self):
        """Prints the list sorted

        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
