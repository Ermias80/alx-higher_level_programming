#!/usr/bin/python3
"""DefinesabasegeometryclassBaseGeometry"""


class BaseGeometry:
    """thisclassrepresentsabasegeometry"""

    def area(self):
        """methodnotimplementedyet"""
        raiseException("area()isnotimplemented")

    def integer_validator(self, name, value):
        """validatesavalueasaninteger
        """
        iftype(value)!=int:
            raiseTypeError("{}mustbeaninteger".format(name))
        ifvalue<=0:
            raiseValueError("{}mustbegreaterthan0".format(name))
