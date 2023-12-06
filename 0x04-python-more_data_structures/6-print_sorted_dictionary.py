#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    this function sort keys of dictionary
    according to alphabets order
    """
    keys = list(a_dictionary.keys())
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
