#!python3

'''
658: too high
'''

import csv
import heapq
from functools import cache

from helpers import BASE

TEST01 = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''


def parse(string):
    map_ = {}
    for y, line in enumerate(string.strip().split('\n')):
        for x, n in enumerate(line):
            map_[x, y] = int(n)
    return map_


def neighbours(location, input_map):
    x, y = location
    ns = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for n in ns:
        if n in input_map:
            yield n, input_map[n]


def part1(input_map):
    '''Dijkstra's algorithm.'''
    start = min(input_map)
    end = max(input_map)
    distance = {l: 1_000_000_000 for l in input_map}
    distance[start] = 0
    processed = {l: False for l in input_map}
    q = [(0, start)]
    counter = 0
    while q:
        counter += 1
        q.sort()
        _, a = q.pop(0)
        if not processed[a]:
            processed[a] = True
            for b, w in neighbours(a, input_map):
                if distance[a] + w < distance[b]:
                    distance[b] = distance[a] + w
                    q.append((distance[b], b))
    return distance[end]



def main():
    test_map = parse(TEST01)
    map_ = parse(open(BASE + 'day15.txt', 'r').read())

    t1 = part1(test_map.copy())
    assert t1 == 40

    p1 = part1(map_.copy())
    print(f'Part 1: {p1}')


if __name__ == '__main__':
    main()
