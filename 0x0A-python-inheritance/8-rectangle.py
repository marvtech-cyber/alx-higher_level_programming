#!/usr/bin/python3
""" module contain class BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Initialize the size of a rectangle
        Args:
            self: first argument to instance methods
            width: width of the rectangle
            height: height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
