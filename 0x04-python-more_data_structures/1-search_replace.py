#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = [replace if element == search else element for element in my_list]
    return (i)
