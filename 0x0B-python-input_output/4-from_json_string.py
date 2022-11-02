#!/usr/bin/python3
"""Module to return object from JSON data"""


def from_json_string(my_str):
    '''Returns python object form JSON'''
    import json
    return json.loads(my_str)
