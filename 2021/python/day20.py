#!python3

from collections import Counter

from helpers import BASE

TEST01 = '''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###'''


TEST01_1 = '''...............
...............
...............
...............
...............
.....#..#......
.....#.........
.....##..#.....
.......#.......
.......###.....
...............
...............
...............
...............
...............'''

TEST01_2 = '''...............
...............
...............
...............
.....##.##.....
....#..#.#.....
....##.#..#....
....####..#....
.....#..##.....
......##..#....
.......#.#.....
...............
...............
...............
...............'''

TEST01_3 = '''...............
...............
...............
..........#....
....#..#.#.....
...#.#...###...
...#...##.#....
...#.....#.#...
....#.#####....
.....#.#####...
......##.##....
.......###.....
...............
...............
...............'''


TEST02 = '''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

.'''


def parse(string):
    enhancement, base_image = string.strip().split('\n\n')
    image = {}
    for r, row in enumerate(base_image.split('\n')):
        for c, ch in enumerate(row):
            location = r, c
            image[(location)] = ch
    return enhancement, image


def enhance_location(location, image, enhancement, step):
    row, col = location
    chars = []
    # If the enhancement string contains a `#` at the zeroth position it
    # means that an infinite number of pixels are switched on for each
    # odd enhancement step.
    if enhancement[0] == '#':
        assert enhancement[-1] == '.'
        default_char = '.' if step % 2 else  '#'
    else:
        default_char = '.'
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            location = r, c
            e = '1' if image.get(location, default_char) == '#' else '0'
            chars.append(e)
    position = int(''.join(chars), 2)
    return enhancement[position]


def enhance_image(image, enhancement, step):
    new_image = {}
    current_locations = image.keys()
    row_min = min(l[0] for l in current_locations) - 1
    row_max = max(l[0] for l in current_locations) + 1
    col_min = min(l[1] for l in current_locations) - 1
    col_max = max(l[1] for l in current_locations) + 1
    for c in range(col_min, col_max + 1):
        for r in range(row_min, row_max + 1):
            location = r, c
            new_image[location] = enhance_location(location, image, enhancement, step)
    return new_image


def print_image(image):
    chars = []
    for r in range(-5, 9 + 1):
        for c in range(-5, 9 + 1):
            location = r, c
            chars.append(image.get(location, '.'))
        chars.append('\n')
    return ''.join(chars[:-1])


def part(image, enhancement, steps):
    for i in range(1, steps + 1):
        image = enhance_image(image, enhancement, i)
    c = Counter(image.values())
    return c['#']


def tests():
    test_enhancement, test_image = parse(TEST01)

    e1 = enhance_location((2, 2), test_image, test_enhancement, 1)
    assert e1 == '#'

    assert print_image(test_image) == TEST01_1
    test_image = enhance_image(test_image, test_enhancement, 1)
    assert print_image(test_image) == TEST01_2
    test_image = enhance_image(test_image, test_enhancement, 1)
    assert print_image(test_image) == TEST01_3

    test_enhancement, test_image = parse(TEST01)
    t1 = part(test_image, test_enhancement, 2)
    assert t1 == 35


def main():
    tests()

    enhancement, image = parse(open(BASE + 'day20.txt', 'r').read())

    p1 = part(image, enhancement, 2)
    print(f'Part 1: {p1}')

    p2 = part(image, enhancement, 50)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
