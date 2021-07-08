#!/usr/bin/python3
"""First class"""


class Square:
    """Build a class"""
    def __init__(self, size=0):
        """Initialize the attributes"""
        self.__size = size

    @property
    def size(self):
        """Return it"""
        return self.__size

    @size.setter
    def size(self, size):
        """The exception"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """return the area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with #"""
        if self.__size == 0:
            print('')
        for num in range(0, self.__size):
            print('#' * self.__size)
