#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ValueError, ZeroDivisionError, TypeError, IndexError) as e:
        print("Exception:", e, file=sys.stderr)
        return None
