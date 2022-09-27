#!/usr/bin/python3
""" module contain class Square that inherits from Rectangle
    (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """

    def __init__(self, size):
        """ Initialize the size of a square
        Args:
            self: first argument to instance methods
            size: private instance attribute, size of the square
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Public instance method
        Args:
            self: first argument to instance methods
        returns: print the square description
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
