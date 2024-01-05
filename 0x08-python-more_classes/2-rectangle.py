#!/usr/bin/python3
"""A rectangle class presentation"""


class Rectangle:
    "This represents rectangle class"

    def __init__(self, width=0, height=0):
        """A magic method to set width and height 
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        Rasies:
            ValueError: if size less than 0
            TypeError: if size not integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__width
    
    @height.setter
    def height(self, value):
        """Sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the Calc the area of rectangle"""
        return (self.__width * self.__height)
    
    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.height * 2))
    