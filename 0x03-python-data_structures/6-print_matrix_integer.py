#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for count1 in range(len(matrix)):
        for count2 in range(len(matrix[count1])):
            print('{:}'.format(matrix[count1][count2]), end = '')
            if count2 + 1 < len(matrix[count1]):
                print(end = ' ')
        print()
