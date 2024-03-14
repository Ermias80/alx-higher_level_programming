#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
import sys

sum_of_args = 0

for arg in sys.argv[1:]:
    sum_of_args += int(arg)
print(sum_of_args)
