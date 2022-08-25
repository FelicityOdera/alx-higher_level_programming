#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print('{:d} arguments.'.format(0))
    elif len(argv) == 2:
        print('{:d} argument:'.format(1))
    elif len(argv) > 2:
        print('{:d} arguments:'.format(len(argv) - 1))
    if len(argv) >= 2:
        for i in argv[1:]:
            index = argv.index(i)
            print('{:d}: {}'.format(index, argv[index]))
