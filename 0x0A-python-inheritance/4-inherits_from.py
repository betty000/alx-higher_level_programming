#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited\
 directly or indirectly from the specified class
 """
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return True
    else:
        return False
