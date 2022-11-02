#!/usr/bin/python3
"""Module to return JSON file of a python object"""


def save_to_json_file(my_obj, filename):
    '''Writes the converted python object to json data, to a file'''
    import json
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
