#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied_values = [value * 2 for value in a_dictionary.values()]
    keys = list(a_dictionary.keys())
    return {keys[i]: multiplied_values[i] for i in range(len(keys))}
