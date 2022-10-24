#!/usr/bin/python3
""" 1-my_list """


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        """ prints the list in ascending sort """
        print(sorted(self))
