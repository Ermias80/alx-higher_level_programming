#!/usr/bin/python3
"""From JSON string module"""


def from_json_string(my_str):
    """from_json_string

    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    import json
    return json.loads(my_str)
