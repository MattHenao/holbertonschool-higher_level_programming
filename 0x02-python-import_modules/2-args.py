#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv)
    if count == 1:
        print('{} arguments.'.format(count - 1))
    else:
        print('{} arguments:'.format(count - 1))
    for words in range(1, count):
        print('{}: {}'.format(words, sys.argv[words]))
