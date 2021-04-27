#!/usr/bin/python3
for hexa in range(00, 100):
    if hexa != 99:
        print('{:02d}, '.format(hexa), end="")
    else:
        print('{:02d}'.format(hexa))
