#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {keys: x * 2 for(keys, x) in a_dictionary.items()}
    return new_dic
