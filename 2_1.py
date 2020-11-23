#!python3

'''Day 2, part 1.'''

import data_2


def area(box):
    '''Calculate area of box.'''
    a, b, c = box
    return 2*a*b + 2*b*c + 2*c*a


def extra(box):
    '''Calculate extra area.'''
    a, b, _ = box
    return a*b


def main():
    '''Main entry point.'''
    data = data_2.data
    total = sum(area(box) + extra(box) for box in data)
    print(total)


if __name__ == '__main__':
    main()
