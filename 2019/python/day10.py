#!python3

from collections import Counter, defaultdict
from itertools import combinations
from math import atan2, pi

from helpers import BASE
from maths import gcd

TEST01 = '''.#..#
.....
#####
....#
...##'''

TEST02 = '''......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####'''

TEST03 = '''#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.'''

TEST04 = '''.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..'''

TEST05 = '''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''


def parse(string):
    asteroids = set([])
    for y, line in enumerate(string.strip().split('\n')):
        for x, ch in enumerate(line):
            if ch == '#':
                asteroids.add((x, y))
    return asteroids


def make_vectors(asteroids):
    vectors = defaultdict(list)
    for a1, a2 in combinations(asteroids, 2):
        x1, y1 = a1
        x2, y2 = a2
        vectors[a1].append((x2 - x1, -(y2 - y1)))
        vectors[a2].append((x1 - x2, -(y1 - y2)))
    return vectors


def make_angles(vectors, best):
    angles = defaultdict(list)
    for x, y in vectors:
        a = atan2(y, x)
        if a < 0:
            # Switch the angles below the x-axis to rotate anti-clockwise.
            a += 2 * pi
        angles[a].append((x, y))
    # Switch to clockwise rotation.
    angles = {2 * pi - k if k > 0 else k: v for k, v in angles.items()}
    # Make zero angle slightly greater than zero.
    angles = {(k + 0.000001) if k == 0 else k: v for k, v in angles.items()}
    # Rotate to make the positive y-axis the zero angle.
    angles = {(k + pi / 2) % (2 * pi): v for k, v in angles.items()}
    for a, ast in angles.items():
        ast.sort(key=lambda x: abs(x[0]) + abs(x[1]))
    return angles



def test1():
    asteroids = parse(TEST01)
    assert part1(asteroids) == (8, (3, 4))


def test2():
    asteroids = parse(TEST02)
    assert part1(asteroids)[0] == 33


def test3():
    asteroids = parse(TEST03)
    assert part1(asteroids)[0] == 35


def test4():
    asteroids = parse(TEST04)
    assert part1(asteroids)[0] == 41


def test5():
    asteroids = parse(TEST05)
    assert part1(asteroids) == (210, (11, 13))


def test6():
    asteroids = parse(TEST05)
    _, best = part1(asteroids)
    assert part2(asteroids, best) == 802


def part1(asteroids):
    vs = make_vectors(asteroids)
    counter = Counter()
    for asteroid, vectors in vs.items():
        unique_vectors = set()
        for v in vectors:
            x = gcd(*v)
            if x != 1:
                v = (v[0] // x, v[1] // x)
            unique_vectors.add(v)
        counter[asteroid] = len(unique_vectors)
    m = counter.most_common(1)[0]
    return m[1], m[0]


def part2(asteroids, best):
    vs = make_vectors(asteroids)
    best_vectors = vs[best]
    angles = make_angles(best_vectors, best)
    count = 0
    sorted_angles = sorted(angles.keys())
    while True:
        for angle in sorted_angles:
            ast = angles[angle]
            try:
                a = ast.pop(0)
                count += 1
                if count == 200:
                    return 100 * (best[0] + a[0]) + best[1] - a[1]
            except IndexError:
                pass


def main():
    test1()
    test2()
    test3()
    test4()
    test5()

    asteroids = parse(open(BASE + 'day10.txt', 'r').read().strip())

    p1, best = part1(asteroids)
    print(f'Part 1: {p1}')

    test6()

    p2 = part2(asteroids, best)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
