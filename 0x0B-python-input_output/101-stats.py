#!/usr/bin/python3
"""
101-stats
    Reads from standard input and computes metrics
"""

import sys


def print_stats():
    """Prints metrics
    """
    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

lc = 0
file_size = 0

try:
    for line in sys.stdin:
        if lc != 0 and lc % 10 == 0:
            print_stats()

        pieces = line.split()

        try:
            status = int(pieces[-2])

            if str(status) in status_codes.keys():
                status_codes[str(status)] += 1
        except (IndexError, ValueError) as e:
            pass

        try:
            file_size += int(pieces[-1])
        except (IndexError, ValueError) as e:
            pass

        lc += 1

    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
