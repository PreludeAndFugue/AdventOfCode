#!python.

from math import prod

INPUT = 'day03.txt'
TEST_INPUT = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''

SLOPES = [
    (1, 1), (1, 3), (1, 5), (1, 7), (2, 1)
]
TEST_SLOPE_ANSWERS = [
    2, 7, 3, 4, 2
]


def count_trees(map, dr, dc):
    columns = len(map[0])
    rows = len(map)
    count = 0
    c = 0
    for r in range(0, rows, dr):
        if map[r][c] == '#':
            count += 1
        c = (c + dc) % columns
    return count


def test2(map, slopes, results):
    for (dr, dc), result in zip(slopes, results):
        count = count_trees(map, dr, dc)
        assert count == result, f'{dr}, {dc}, {count}, {result}'


def part2(map, slopes):
    counts = []
    for dr, dc in slopes:
        count = count_trees(map, dr, dc)
        counts.append(count)
    return prod(counts)


def main():
    test_map = TEST_INPUT.strip().split('\n')
    full_map = open(INPUT, 'r').read().strip().split('\n')

    assert count_trees(test_map, 1, 3) == 7

    p = count_trees(full_map, 1, 3)
    print(p)

    test2(test_map, SLOPES, TEST_SLOPE_ANSWERS)
    assert part2(test_map, SLOPES) == 336

    p = part2(full_map, SLOPES)
    print(p)


if __name__ == "__main__":
    main()