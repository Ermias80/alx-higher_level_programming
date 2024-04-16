#!/usr/bin/python3
"""Module that defines the class Student."""


class Student:
    """Class that defines a student."""
    def __init__(self, first_name, last_name, age):
        """Initializes a student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with values from a dictionary."""
        for key, value in json.items():
            self.__dict__[key] = value
