#!/usr/bin/python3

def element_at(my_list, idx):
    """ this function retrieves an element from the list"""
    if idx < 0 or idx >= len(my_list):
        return ("None")
    else: 
        return my_list[idx]
