
from collections import defaultdict
from queue import Queue

from help import get_input

TEST01 = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''


source = TEST01.strip()
source = get_input(7)


def make_map(source):
    map_ = {}
    start = None
    for y, row in enumerate(source.split('\n')):
        for x, c in enumerate(row):
            if c == 'S':
                start = x, y
            map_[(x, y)] = c
    return map_, start


def get_next(v, map_):
    x, y = v
    x1, y1 = x, y + 1
    v1 = x1, y1
    a = map_.get(v1, ' ')
    split = False
    if a == '^':
        split = True
        vl = x1 - 1, y1
        vr = x1 + 1, y1
        return [vl, vr], split
    elif a == '.':
        return [v1], split
    elif a == ' ':
        return [], split
    else:
        raise ValueError


def part1():
    map_, start = make_map(source)
    q = Queue()
    explored = set([start])
    q.put(start)
    splits = 0
    while not q.empty():
        v = q.get()
        ws, split = get_next(v, map_)
        if split:
             splits += 1
        for w in ws:
            if w not in explored:
                explored.add(w)
                q.put(w)
    return splits


def print_map(map_):
    rows = []
    for y in range(16):
        row = []
        for x in range(15):
            row.append(str(map_[(x, y)]))
        rows.append(' '.join(row))
    print('\n'.join(rows))


def update(p, map_):
    '''
    Dynamic programming step to update cells in next row up based on the value in the
    current cell.
    '''
    c = map_[p]
    if c == '^':
        return
    x, y = p
    left = map_.get((x - 1, y), -1)
    right = map_.get((x + 1, y ), -1)
    up = map_.get((x, y - 1), -1)
    if left == '^':
        left_up = map_.get((x - 1, y - 1), -1)
        if left_up != -1 and left_up != '^':
            map_[(x - 1, y - 1)] += c
    if right == '^':
        right_up = map_.get((x + 1, y - 1), -1)
        if right_up != -1 and right_up != '^':
            map_[(x + 1, y - 1)] += c
    if up != '^':
        map_[(x, y - 1)] = map_[p]



def part2():
    '''
    Dynamic programming. Start from the bottom and work back to the start.
    '''
    map_, start = make_map(source)
    i = max(p[1] for p in map_)

    # Replace '.' with zeros except for the bottom row where replaced by ones.
    for p in map_:
        _, y = p
        if y == i:
            c = map_[p]
            if c == '.':
                map_[p] = 1
        else:
            c = map_[p]
            if c == '.' or c == 'S':
                map_[p] = 0

    while i >= 0:
        ps = [p for p in map_ if p[1] == i]
        for p in ps:
            update(p, map_)
        i -= 1

    return map_[start]


if __name__ == '__main__':
    p1 = part1()
    print(p1)
    p2 = part2()
    print(p2)
