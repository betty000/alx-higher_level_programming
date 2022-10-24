#!/usr/bin/python3
""" 11-square """


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
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ Class Rectangle subclass of Rectangle subclass of BaseGeometry"""
    def __init__(self, size):
        """subclass constructor"""
        self.__size = size
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)

    def area(self):
        """ returns area of square"""
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
