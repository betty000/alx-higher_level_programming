#!/usr/bin/python3
""" 8-rectangle """


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        """ raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Class Rectangle subclass of BaseGeometry"""
    def __init__(self, width, height):
        """ class constructor """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
