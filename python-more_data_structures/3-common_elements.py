#!/usr/bin/python3

def common_elements(set_1, set_2):

    common_elements = set()

    for i in set_1:
        if i in set_2:
            common_elements.add(i)

    return common_elements
