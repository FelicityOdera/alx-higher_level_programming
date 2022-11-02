#!/usr/bin/python3
"""Module to append to a file"""


def append_write(filename="", text=""):
    '''Appends a string to text file and returns length of appended string'''
    with open(filename, 'a', encoding="utf-8") as f:
        for char in text:
            f.write(char)
    return len(text)
