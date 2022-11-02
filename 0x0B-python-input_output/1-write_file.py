#!/usr/bin/python3
"""Module to write to a file"""


def write_file(filename="", text=""):
    '''Writes a string to text file and returns string length'''
    with open(filename, 'w', encoding="utf-8") as f:
        for char in text:
            f.write(char)
    return len(text)
