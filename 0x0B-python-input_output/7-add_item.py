#!/usr/bin/python3
"""
    This script adds all arguments to a Python list and saves them to a file
"""


import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

if not path.exists(filename):
    items = []
else:
    items = load_from_json_file(filename)

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
