#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    total = 0

    for number in my_list:
        if number not in unique:
            total += number
            unique.add(number)
    return (total)
