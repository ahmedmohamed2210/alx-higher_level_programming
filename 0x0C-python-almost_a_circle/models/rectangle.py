#!/usr/bin/python3
"""Rectangle class inherits from base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """inialization attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """Gits the value for width"""
            return self.__width

        @property
        def height(self):
            """Gits the value of height"""
            return self.__height

        @property
        def x(self):
            """Gits the value for x"""
            return self.__x

        @property
        def y(self):
            """Gits the value for y"""
            return self.__y

        @width.setter
        def width(self, value):
            """Sets the value for width"""
            if (type(value) is not int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @height.setter
        def height(self, value):
            """Sets the value for height"""
            if (type(value) is not int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @x.setter
        def x(self, value):
            """Sets the value for x"""
            if (type(value) is not int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self._x = value

        @y.setter
        def y(self, value):
            """Sets the value for y"""
            if (type(value) is not int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
