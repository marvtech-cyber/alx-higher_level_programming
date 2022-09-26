#!/usr/bin/python3
""" module contain class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        """
        Public instance method
        Args:
            self: first argument to instance methods
        Raise:
            Exception: area() is not implemented
        returns: no return
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public instance method, validate the value
        Args:
            self: first argument to instance methods
            name: string
            value: value
        Return: No return.
        Raise:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
