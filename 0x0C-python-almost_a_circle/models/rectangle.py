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
        super().__init__(Base)

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
            return self.__width = value

        @height.setter
        def height(self, value):
            """Sets the value for height"""
            return self.__height = value