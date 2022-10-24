#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ function that returns True if the objext is an intance of a class\
            that inherited from the specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
