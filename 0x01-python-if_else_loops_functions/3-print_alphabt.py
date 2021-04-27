#!/usr/bin/python3
for abcd in range(97, 123):
    if abcd == 113 or abcd == 101:
        continue
    else:
        print('{:c}'.format(abcd), end="")
