#!/usr/bin/python3
"""This module define json-string converting (deserializing)"""
import json


def from_json_string(my_str):
    """REturn the python object representation of a json string"""
    return json.loads(my_str)
