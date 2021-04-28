#!/usr/bin/python3
for FzBz in range(1, 101):
    if FzBz % 3 == 0 and FzBz % 5 == 0:
        print('FizzBuzz', end=' ')
    elif FzBz % 5 == 0:
        print('Buzz', end=' ')
    elif FzBz % 3 == 0:
        print('Fizz', end=' ')
    else:
        print('{:d}'.format(FzBz), end=' ')
