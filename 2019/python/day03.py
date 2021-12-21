#!python3

from helpers import BASE, manhattan_distance_2

TEST01 = '''R8,U5,L5,D3
U7,R6,D4,L4'''

TEST02 = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83'''

TEST03 = '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''


def parse(string):
    p1, p2 = string.strip().split('\n')
    p1 = p1.split(',')
    p1 = [(x[0], int(x[1:])) for x in p1]
    p2 = p2.split(',')
    p2 = [(x[0], int(x[1:])) for x in p2]
    return p1, p2


def make_diff(direction):
    if direction == 'U':
        return 0, 1
    if direction == 'D':
        return 0, -1
    if direction == 'L':
        return -1, 0
    if direction == 'R':
        return 1, 0
    return ValueError


def make_coords(path):
    x, y = 0, 0
    coords = []
    for direction, distance in path:
        dx, dy = make_diff(direction)
        for _ in range(distance):
            x += dx
            y += dy
            coords.append((x, y))
    return coords


def part1(p1, p2):
    c1 = make_coords(p1)
    c2 = make_coords(p2)
    intersection = set(c1).intersection(c2)
    return min(manhattan_distance_2((0, 0), c) for c in intersection)


def part2(p1, p2):
    c1 = make_coords(p1)
    c2 = make_coords(p2)
    intersection = set(c1).intersection(c2)
    distances = []
    for c in intersection:
        l1 = c1.index(c)
        l2 = c2.index(c)
        distances.append(l1 + l2)
    return min(distances) + 2


def main():
    t1 = part1(*parse(TEST01))
    assert t1 == 6

    t2 = part1(*parse(TEST02))
    assert t2 == 159

    t3 = part1(*parse(TEST03))
    assert t3 == 135

    data = parse(open(BASE + 'day03.txt', 'r').read())

    p1 = part1(*data)
    print(f'Part 1: {p1}')

    t4 = part2(*parse(TEST01))
    assert t4 == 30

    t5 = part2(*parse(TEST02))
    assert t5 == 610

    t6 = part2(*parse(TEST03))
    assert t6 == 410

    p2 = part2(*data)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
