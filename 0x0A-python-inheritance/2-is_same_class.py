#!/usr/bin/python3
""" 2-is_same_Class """


def is_same_class(obj, a_class):
    """ return True if the object is an instance of a class"""
    if type(obj) == a_class:
            return True
    else:
            return False
