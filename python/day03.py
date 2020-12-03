#!python.


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


def make_map(input):
    lines = []
    for line in input:
        lines.append(line.strip())
    return lines


def count_trees(map):
    width = len(map[0])
    count = 0
    for (row, line) in enumerate(map):
        col = (3 * row) % width
        if line[col] == '#':
            count += 1
    return count


def main():
    test_map = make_map(TEST_INPUT.strip().split('\n'))
    assert count_trees(test_map) == 7

    map = make_map(open(INPUT, 'r').readlines())
    p = count_trees(map)
    print(p)


if __name__ == "__main__":
    main()