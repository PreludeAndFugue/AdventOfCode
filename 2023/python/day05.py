
from help import get_input

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
        # destination, source, range length
        row = [int(n) for n in row.split()]
        rows.append((row[1], row[0], row[2]))
    rows.sort()
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


def main():
    d = get_input('05')
    # d = TEST.strip()
    seeds, maps = parse(d)
    results = []
    for seed in seeds:
        n = seed
        for map_ in maps:
            n = do_mapping(n, map_)
        results.append(n)
    print(min(results))


if __name__ == '__main__':
    main()
