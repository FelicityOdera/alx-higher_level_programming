#!/usr/bin/python3
"""Module to extract python object from a JSON file"""


def load_from_json_file(filename):
    '''Reads a json file and extracts python object'''
    import json
    with open(filename, 'r', encoding="utf-8") as f:
        content = json.loads(f.read())
    return content
