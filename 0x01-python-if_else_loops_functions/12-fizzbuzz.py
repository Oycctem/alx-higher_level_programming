#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        output = ''
        if num % 3 == 0:
            output += 'Fizz'
        if num % 5 == 0:
            output += 'Buzz'
        if not output:
            output = number
        print(output, end=' ')
