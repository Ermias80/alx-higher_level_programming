#!/usr/bin/python3
"""Save to JSON file module

Writes an object to a text file using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file


    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file to write the JSON representation to.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
