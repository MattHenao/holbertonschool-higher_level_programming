#!/usr/bin/python3
"""Create rectangle class"""


class Rectangle:
    """Build the class"""
    def __init__(self, width=0, height=0):
        """Init the attributes"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Return it"""
        return self.__width

    @width.setter
    def width(self, value):
        """Excepts"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Return it"""
        return self.__height

    @height.setter
    def height(self, value):
        """Excepts"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Rectangle area"""
        return(self.__height * self.__width)

    def perimeter(self):
        """Rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return('')

        tmp = ''
        for num in range(self.__height):
            tmp += '{:s}'.format(self.__width * '#')
            if num is not self.__height - 1:
                tmp += '\n'
        return tmp
