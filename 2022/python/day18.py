
from help import get_input

TEST1 = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''


def parse(s):
    for line in s.split('\n'):
        yield tuple(map(int, line.split(',')))


def manhattan(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)


def part1(cubes):
    neighbours = dict()
    for c1 in cubes:
        neighbours[c1] = []
        for c2 in cubes:
            if manhattan(c1, c2) == 1:
                neighbours[c1].append(c2)
    answer = 0
    for _, ns in neighbours.items():
        answer += 6 - len(ns)
    return answer


def main():
    s = get_input('18')
    # s = TEST1.strip()

    cubes = list(parse(s))

    p1 = part1(cubes)

    print('Part1:', p1)


if __name__ == '__main__':
    main()
