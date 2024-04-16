#!/usr/bin/python3

class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings specifying attribute names to retrieve.
                If None, all attributes will be retrieved.

        Returns:
            dict: A dictionary representing the Student instance.

        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with values from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
