#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = abs(number) % 10
if number < 0:
    lastdig = lastdig * -1
if lastdig > 5:
    print(f"Last digit of {number} is {lastdig} and is greater than 5")
elif lastdig == 0:
    print(f"Last digit of {number} is {lastdig} and is 0")
elif lastdig < 6 and lastdig != 0:
    print(f"Last digit of {number} is {lastdig} and is less than 6 and not 0")
