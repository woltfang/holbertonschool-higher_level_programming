#!/usr/bin/python3
""" Rectangle Module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle (BaseGeometry):
    """ Rectangle Class inheriths from BaseGeometry.
    Instantiation with width and height
    """
    def __init__(self, width, height):
        """ Constructor.
        width, heigth
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
