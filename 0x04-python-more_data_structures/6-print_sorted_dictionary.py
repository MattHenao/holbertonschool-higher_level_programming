#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for list in sorted(a_dictionary):
        print('{}: {}'.format(list, a_dictionary[list]))
