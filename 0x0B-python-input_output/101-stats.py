#!/usr/bin/python3
"""
Log parsing script that computes metrics from stdin input.
"""

import sys

def print_metrics(total_size, status_codes):
    """Prints the computed metrics."""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count:
            print("{}: {}".format(code, count))

def parse_input(line):
    """Parses a line of input and returns the IP address, status code, and file size."""
    parts = line.split()
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = parts[-1]
    return ip_address, status_code, int(file_size)
