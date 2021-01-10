#!python3

'''Day 2'''

import data_2


def area(box):
    '''Calculate area of box.'''
    a, b, c = box
    return 2*a*b + 2*b*c + 2*c*a


def extra(box):
    '''Calculate extra area.'''
    a, b, _ = box
    return a*b


def part1():
    data = data_2.data
    return sum(area(box) + extra(box) for box in data)


def ribbon(box):
    '''Length of ribbon for box.'''
    a, b, _ = box
    return 2*(a + b)


def bow(box):
    '''Length for bow.'''
    a, b, c = box
    return a*b*c


def part2():
    data = data_2.data
    return sum(ribbon(box) + bow(box) for box in data)


def main():
    '''Main entry point.'''
    p1 = part1()
    print(p1)

    p2 = part2()
    print(p2)


if __name__ == '__main__':
    main()
