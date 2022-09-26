#!/usr/bin/python3
""" module contain function inherits_from """


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance of
    a class that inherited (directly or indirectly) from the specified class ;
    otherwise False
        Args:
            obj: object
            a_class: class
        Return:
            True or false
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
