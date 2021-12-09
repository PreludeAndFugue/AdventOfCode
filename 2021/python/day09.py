#!python3

from helpers import BASE

TEST01 = '''2199943210
3987894921
9856789892
8767896789
9899965678'''


def parse(string):
    lines = string.strip().split('\n')
    map = {}
    for i, row in enumerate(lines):
        for j, col in enumerate(row):
            map[i, j] = int(col)
    return map


def neighbour_heights(map, row, col):
    return [
        map.get((row - 1, col), 10),
        map.get((row + 1, col), 10),
        map.get((row, col - 1), 10),
        map.get((row, col + 1), 10),
    ]


def pop_neighbours(map_, location):
    row, col = location
    neighbours = []
    for n in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        h = map_.pop(n, 10)
        if h < 9:
            neighbours.append(n)
    return neighbours


def get_basin(map_, location):
    basin = []
    seen = set()
    to_search = [location]
    while to_search:
        l = to_search.pop(0)
        if l in seen:
            continue
        basin.append(l)
        seen.add(l)
        neighbours = pop_neighbours(map_, l)
        to_search.extend(neighbours)
    return basin


def part1(map_):
    minima = []
    for location, height in map_.items():
        nh = neighbour_heights(map_, *location)
        if height < min(nh):
            minima.append(height)
    return sum(n + 1 for n in minima)


def part2(map_):
    map_ = {k: v for k, v in map_.items() if v < 9}
    basins = []
    while map_:
        location, _ = map_.popitem()
        basin = get_basin(map_, location)
        basins.append(basin)
    answer = 1
    for n in sorted(len(b) for b in basins)[-3:]:
        answer *= n
    return answer


def main():
    test_map = parse(TEST01)
    map_ = parse(open(BASE + 'day09.txt').read())

    t1 = part1(test_map)
    assert t1 == 15

    p1 = part1(map_)
    print(f'Part 1: {p1}')

    t2 = part2(test_map)
    assert t2 == 1134

    p2 = part2(map_)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
