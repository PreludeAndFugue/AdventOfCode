
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


if __name__ == '__main__':
    p1 = part1()
    print(p1)
