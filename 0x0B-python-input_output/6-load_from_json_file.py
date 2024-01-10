#!/usr/bin/python3
"""Define an object from a json file"""
import json


def load_from_json_file(filename):
    """create object from json file"""
    with open(filename) as f:
        return json.load(f)
