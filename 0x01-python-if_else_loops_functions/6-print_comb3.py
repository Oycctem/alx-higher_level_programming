#!/usr/bin/python3
for number in range(10):
    for number1 in range(number + 1, 10):
        if number == 8 and number1 == 9:
            print('89')
        else:
            print('{}{}'.format(number, number1), end=", ")
