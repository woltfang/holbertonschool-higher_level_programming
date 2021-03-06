#!/usr/bin/python3
"""Square Module"""


class Square():
    """Square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """
    def __init__(self, size):
        """Constructor"""
        self.__size = size
