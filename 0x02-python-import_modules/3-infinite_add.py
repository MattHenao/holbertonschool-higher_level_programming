#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    for numbers in range(len(sys.argv) - 1):
        result += int(sys.argv[numbers + 1])
    print('{}'.format(result))
