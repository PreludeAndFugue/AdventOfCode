
from help import get_input

'''
Better algorithm for part 2?
----------------------------
- Only interested in lowest integer in a range because this will map to the lowest
  integer in a new range.
- A range can be mapped into new non-overlapping ranges.

         1    2      3       4
         -------------------------
         |    |      |       |
         |    |      |       |
      ---+----|      +-------|
         |    |      |       |
         |    |      |       |
         a    b      c       d

    a is the mapping of 1 (the first value in the range)
    b is the mapping of 2 (the first value after the end of the first mapping range)
    c is the mapping of 3 (the first value in the range equal to the first value of the
    second mapping range)
    d is the mapping of 4 (the first value after the end of the first mapping range)

    It may not be the case that a < b < c < d.

         1    2
         ---------------
         |    |
         |    |
         |    +----------------
         |    |
         |    |
         a    b

'''

TEST = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''


def make_map(d):
    rows = []
    for row in d:
        row = [int(n) for n in row.split()]
        rows.append(row)
    rows
    return rows


def parse(d):
    seeds, maps = d.split('\n\n', maxsplit=1)
    seeds = [int(x) for x in seeds.split(':')[1].strip().split()]
    final_maps = []
    for map_ in maps.split('\n\n'):
        map_ = map_.split('\n')[1:]
        final_maps.append(make_map(map_))
    return seeds, final_maps


def do_mapping(seed, map_):
    for (source, destination, length) in map_:
        if seed < source:
            return seed
        if seed < source + length:
            return destination + (seed - source)
    # exhasted all ranges
    return seed


def part1(seeds, maps):
    lowest = 1_000_000_000_000_000
    x = 0

    new_maps = []
    for map_ in maps:
        new_map = []
        for row in map_:
            row = (row[1], row[0], row[2])
            new_map.append(row)
        new_map.sort()
        new_maps.append(new_map)

    for seed in seeds:
        n = seed
        for map_ in new_maps:
            n = do_mapping(n, map_)
        lowest = min(n, lowest)
        if n < lowest:
            lowest = n
            x = seed
    return lowest, seed


def part2(seeds, maps):
    seed_ranges = []
    for a, b in zip(seeds[::2], seeds[1::2]):
        seed_ranges.append(range(a, a + b))

    new_maps = []
    for map_ in maps:
        new_map = []
        for row in map_:
            row = (row[0], row[1], row[2])
            new_map.append(row)
        new_map.sort()
        new_maps.append(new_map)
    new_maps = list(reversed(new_maps))

    n = 1
    while True:
        m = n
        for map_ in new_maps:
            m = do_mapping(m, map_)
        for r in seed_ranges:
            if m in r:
                return n, m
        n += 1


def main():
    # d = get_input('05')
    d = TEST.strip()
    seeds, maps = parse(d)

    p1 = part1(seeds, maps)
    print(p1)

    p2 = part2(seeds, maps)
    print(p2)


if __name__ == '__main__':
    main()
