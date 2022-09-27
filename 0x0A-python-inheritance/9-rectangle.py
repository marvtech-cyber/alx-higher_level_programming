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

    def area(self):
        """
        Public instance method, calculate the area
        Args:
            self: first argument to instance methods
        Raise:
            Exception: area() is not implemented
        return: area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Public instance method
        Args:
            self: first argument to instance methods
        returns: print the rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
