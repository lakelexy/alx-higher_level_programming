#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    j = 0
    for i in my_list:
        if i == search:
            new_list[j] = replace
        j += 1
    return new_list
