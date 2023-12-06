#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    this function sort keys of dictionary
    according to alphabets order
    """
    
    keys = list(a_dictionary.keys())
    keys.sort()
    for i in keys:
        print("{}: {}".format(i, a_dictionary[i]))
    
