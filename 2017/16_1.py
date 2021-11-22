#!python3

'''Day 16, part 1.'''

from data_16 import commands, dance, data
import data_16


if __name__ == '__main__':
    items = dance(commands, data, data_16.items)
    print(items)
