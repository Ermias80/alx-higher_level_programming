#!/usr/bin/python3
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Check if the file exists
if not path.exists(filename):
    # Create an empty list if the file doesn't exist
    items = []
else:
    # Load the existing list from the file
    items = load_from_json_file(filename)

# Add all command line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
