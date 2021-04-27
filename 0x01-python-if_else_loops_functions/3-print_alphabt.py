#!/usr/bin/python3
for alfabeto in range (97, 123):
    if alfabeto == 113 or alfabeto == 101:
        continue
    else:
        print('{:c}'.format(alfabeto), end="")
