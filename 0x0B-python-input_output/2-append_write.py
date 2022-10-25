#!/usr/bin/python3
"""
This file contains a function that appends
a string at the end of a text file and
the number of characters returned
"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as file:
        return (file.write(str(text)))
