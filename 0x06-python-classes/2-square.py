#!/usr/bin/python3
"""First class"""


class Square:
    """Build a class"""
    def __init__(self, size=0):
        """Initialize the attributes"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
