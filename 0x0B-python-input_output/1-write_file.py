#!/usr/bin/python3
"""
File contains function that
writes a string to text file and returns
number of characters written TO IT.
"""


def write_file(filename="", text=""):
    """
    function to write to files
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return (file.write(str(text)))
