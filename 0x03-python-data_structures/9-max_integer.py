#!/usr/bash/python3

def max_integer(my_list=[]):
    if my_list:
        max_int = my_list.sort()[-1]
    else:
        return ("None")
