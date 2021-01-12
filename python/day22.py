#! python3

import re

data = "day22.txt"
p1 = re.compile('deal into new stack')
p2 = re.compile('cut (-?\\d+)')
p3 = re.compile('deal with increment (\\d+)')


def parse():
    with open(data, 'r') as f:
        for line in f:
            print(p1.match(line))
            print(p2.match(line))
            print(p3.match(line))


def main():
    parse()


if __name__ == '__main__':
    main()
