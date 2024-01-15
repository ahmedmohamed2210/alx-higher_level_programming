#!/usr/bin/python3
"""This is still unknown class"""

class Base:
    """The Base class serve as base of all class created"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects