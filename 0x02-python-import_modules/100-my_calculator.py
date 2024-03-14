#!/usr/bin/python3
if __name__ == "__main__":
    """Handle basic arithmetic operations."""
import sys
from calculator_1 import add, sub, mul, div

if len(sys.argv) != 4:
    sys.exit(1)

operator = sys.argv[2]

if operator == '+':
    result = add(a, b)
elif operator == '-':
    result = sub(a, b)
elif operator == '*':
    result = mul(a, b)
elif operator == '/':
    result = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
print("{} {} {} = {}".format(a, operator, b, result))
