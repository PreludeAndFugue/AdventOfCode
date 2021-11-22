#!python3

'''Day 2'''

INPUT = 'day02.txt'

def parse_input(input):
    '''Parse the input string.'''
    lines = open(input, 'r').read().strip()
    rows = (row.strip() for row in lines.split('\n'))
    return [sorted(map(int, row.split('x'))) for row in rows]


def area(box):
    '''Calculate area of box.'''
    a, b, c = box
    return 2*a*b + 2*b*c + 2*c*a


def extra(box):
    '''Calculate extra area.'''
    a, b, _ = box
    return a*b


def part1(boxes):
    return sum(area(box) + extra(box) for box in boxes)


def ribbon(box):
    '''Length of ribbon for box.'''
    a, b, _ = box
    return 2*(a + b)


def bow(box):
    '''Length for bow.'''
    a, b, c = box
    return a*b*c


def part2(boxes):
    return sum(ribbon(box) + bow(box) for box in boxes)


def main():
    boxes = parse_input(INPUT)

    p1 = part1(boxes)
    print(p1)

    p2 = part2(boxes)
    print(p2)


if __name__ == '__main__':
    main()
