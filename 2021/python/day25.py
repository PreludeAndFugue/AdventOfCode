#!python3

from helpers import BASE

TEST01 = '''...>>>>>...'''

TEST02 = '''..........
.>v....v..
.......>..
..........'''

TEST03 = '''...>...
.......
......>
v.....>
......>
.......
..vvv..'''

TEST04 = '''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>'''


def parse(string):
    map_ = {}
    for y, line in enumerate(string.strip().split('\n')):
        for x, ch in enumerate(line):
            map_[x, y] = ch
    return map_, x + 1, y + 1


def construct_map(map_, x_max, y_max):
    rows = []
    for y in range(y_max):
        row = ''.join(map_.get((x, y), '.') for x in range(x_max))
        rows.append(row)
    return '\n'.join(rows)



def move(map_, ch, x_max, y_max):
    locations = [k for k, v in map_.items() if v == ch]
    new_map = map_.copy()
    for x, y in locations:
        neighbour = (x, (y + 1) % y_max) if ch == 'v' else ((x + 1) % x_max, y)
        if map_[neighbour] == '.':
            new_map[x, y] = '.'
            new_map[neighbour] = ch
    return new_map


def step(map_, x_max, y_max):
    for ch in ['>', 'v']:
        map_ = move(map_, ch, x_max, y_max)
    return map_


def test1():
    t1, x, y = parse(TEST01)
    m1 = construct_map(t1, x, y)
    assert m1 == '...>>>>>...'

    t1 = move(t1, '>', x, y)
    m1 = construct_map(t1, x, y)
    assert m1 == '...>>>>.>..'

    t1 = move(t1, '>', x, y)
    m1 = construct_map(t1, x, y)
    assert m1 == '...>>>.>.>.'


def test2():
    t2, x, y = parse(TEST02)
    m2 = construct_map(t2, x, y)
    assert m2 == TEST02

    t2 = step(t2, x, y)
    m2 = construct_map(t2, x, y)
    assert m2 == '''..........
.>........
..v....v>.
..........'''


def test3():
    t3, x, y = parse(TEST03)
    m3 = construct_map(t3, x, y)
    assert m3 == TEST03

    t3 = step(t3, x, y)
    m3 = construct_map(t3, x, y)
    assert m3 == '''..vv>..
.......
>......
v.....>
>......
.......
....v..'''

    t3 = step(t3, x, y)
    m3 = construct_map(t3, x, y)
    assert m3 == '''....v>.
..vv...
.>.....
......>
v>.....
.......
.......'''

    t3 = step(t3, x, y)
    m3 = construct_map(t3, x, y)
    assert m3 == '''......>
..v.v..
..>v...
>......
..>....
v......
.......'''

    t3 = step(t3, x, y)
    m3 = construct_map(t3, x, y)
    assert m3 == '''>......
..v....
..>.v..
.>.v...
...>...
.......
v......'''


def test4():
    t4, x, y = parse(TEST04)
    m4 = construct_map(t4, x, y)
    assert m4 == TEST04

    x = part1(t4, x, y)
    assert x == 58


def part1(map_, x, y):
    i = 0
    while True:
        i += 1
        new_map = step(map_, x, y)
        if new_map == map_:
            return i
        map_ = new_map


def main():
    test1()
    test2()
    test3()
    test4()

    m, x, y = parse(open(BASE + 'day25.txt', 'r').read())
    p1 = part1(m, x, y)
    print(f'Part 1: {p1}')



if __name__:
    main()
