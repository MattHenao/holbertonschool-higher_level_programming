#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10

if n > 5:
    print('is {:d} and is greater than 5'.format(n)end="")

elif n == 0:
    print('is {:d} and is zero'.format(n))

elif n < 6 and n != 0:
    print('is {:d} and is less than 6 and not 0'.format(n))
