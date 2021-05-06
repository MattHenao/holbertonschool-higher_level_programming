#!/usr/bin/python3
def no_c(my_string):
    none = ""
    for count in my_string:
        if count != 'c' and count != 'C':
            none += count
    return none