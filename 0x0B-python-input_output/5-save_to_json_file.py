#!/usr/bin/python3
"""Save to JSON file module"""


def save_to_json_file(my_obj, filename):
    """save_to_json_file

    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file to write the JSON representation to.
    """
    import json
    with open(filename, "w") as f:
        json.dump(my_obj, f)
