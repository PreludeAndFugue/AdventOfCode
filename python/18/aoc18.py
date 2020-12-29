#!python3

from collections import defaultdict
from itertools import combinations
from queue import Queue, PriorityQueue
from string import ascii_lowercase, ascii_uppercase

INPUT = 'day18.txt'

TEST_INPUT_1 = '''
#########
#b.A.@.a#
#########
'''
TEST_OUTPUT_1 = 8

TEST_INPUT_2 = '''
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
'''
TEST_OUTPUT_2 = 86

TEST_INPUT_3 = '''
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
'''
TEST_OUTPUT_3 = 132

TEST_INPUT_4 = '''
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
'''
TEST_OUTPUT_4 = 136
# a, f, b, j, g, n, h, d, l, o, e, p, c, i, k, m

TEST_INPUT_5 = '''
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
'''
TEST_OUTPUT_5 = 81


def parse_map(input):
    base_map = {}
    keys = {}
    for x, line in enumerate(input.strip().split('\n')):
        for y, ch in enumerate(line):
            if ch == '#':
                continue
            elif ch ==  '@':
                keys[ch] = x, y
            elif ch in ascii_lowercase:
                keys[ch] = x, y
            elif ch in ascii_uppercase:
                pass
            elif ch == '.':
                pass
            else:
                raise Exception(f'Wrong chr {ch}')
            base_map[(x, y)] = ch
    return base_map, keys


def get_neighbours(x, y, base_map):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x = x + dx
        new_y = y + dy
        value = base_map.get((new_x, new_y), None)
        if value is not None:
            yield new_x, new_y, value


def bfs(l1, l2, base_map):
    to_check = Queue()
    to_check.put((l1,))
    seen = set()
    while to_check:
        path = to_check.get()
        l = path[-1]
        seen.add(l)

        if l == l2:
            # print(l, l1, l2)
            required_keys = [
                base_map[x] for x in path[1:-1]
                if base_map[x] in ascii_uppercase or base_map[x] in ascii_lowercase
            ]
            required_keys = [x.lower() for x in required_keys]
            r = set(required_keys)
            # print(r)
            # print(base_map[l])
            # if base_map[l] != '@':
            #     r.remove(base_map[l])
            return len(path) - 1, r

        x, y = l
        for n_x, n_y, _ in get_neighbours(x, y, base_map):
            n = n_x, n_y
            if n not in seen:
                new_path = path + (n,)
                to_check.put(new_path)
    raise Exception('Goal not found')


def make_key_map(key_locations, base_map):
    locations = list(key_locations.values())
    key_map = defaultdict(dict)
    for l1, l2 in combinations(locations, 2):
        k1, k2 = base_map[l1], base_map[l2]
        d, required_keys = bfs(l1, l2, base_map)
        key_map[k1][k2] = d, required_keys
        key_map[k2][k1] = d, required_keys
    return key_map


def get_key_neighbours(location, current_keys, key_map):
    for k, (d, required_keys) in key_map[location].items():
        # print(k, d, required_keys)
        c = set(current_keys)
        # print(c)
        # print()
        if k == '@':
            continue
        if k in current_keys:
            continue
        if not required_keys <= c:
            continue
        yield k, d


def bfs_keys(key_map):
    print(key_map)
    print(key_map['i'])
    all_key_count = len(key_map)
    to_check = PriorityQueue()
    to_check.put((0, '@'))
    seen = set()
    while to_check:
        d, path = to_check.get()

        # print(d, path)
        # input()

        if len(path) == all_key_count:
            return path

        l = path[-1]
        seen.add(path)
        for n, d_n in get_key_neighbours(l, path, key_map):
            new_path = path + n
            if new_path not in seen:
                to_check.put((d + d_n, new_path))
    raise Exception('Goal not found')


def path_length(path, key_map):
    total = 0
    for k1, k2 in zip(path, path[1:]):
        d = key_map[k1][k2][0]
        total += d
    return total


def test1():
    base_map, key_locations = parse_map(TEST_INPUT_1)
    key_map = make_key_map(key_locations, base_map)
    p = bfs_keys(key_map)
    d = path_length(p, key_map)
    print(p)
    print(d)


def test2():
    base_map, key_locations = parse_map(TEST_INPUT_2)
    key_map = make_key_map(key_locations, base_map)
    p = bfs_keys(key_map)
    d = path_length(p, key_map)
    print(p)
    print(d)


def test3():
    base_map, key_locations = parse_map(TEST_INPUT_3)
    key_map = make_key_map(key_locations, base_map)
    p = bfs_keys(key_map)
    d = path_length(p, key_map)
    print(p)
    print(d)


def test4():
    base_map, key_locations = parse_map(TEST_INPUT_4)
    key_map = make_key_map(key_locations, base_map)
    p = bfs_keys(key_map)
    d = path_length(p, key_map)
    print(p)
    print(d)


def test4a():
    base_map, key_locations = parse_map(TEST_INPUT_4)
    key_map = make_key_map(key_locations, base_map)

    assert key_map['m']['a'][1] == set('hc')
    assert key_map['m']['b'][1] == set('ch')
    assert key_map['m']['c'][1] == set('ch')
    assert key_map['m']['d'][1] == set('ch')
    assert key_map['m']['e'][1] == set('ch')
    assert key_map['m']['f'][1] == set('ch')
    assert key_map['m']['g'][1] == set('ch')
    assert key_map['m']['h'][1] == set('c')
    assert key_map['m']['i'][1] == set('cgh')
    assert key_map['m']['j'][1] == set('abch')
    assert key_map['m']['k'][1] == set('aceh')
    assert key_map['m']['l'][1] == set('cdfh')
    assert key_map['m']['n'][1] == set('bcgh')
    assert key_map['m']['o'][1] == set('cdfh')
    assert key_map['m']['p'][1] == set('ceh')

    assert key_map['a']['b'][1] == set()
    assert key_map['a']['c'][1] == set()
    assert key_map['a']['d'][1] == set()
    assert key_map['a']['e'][1] == set()
    assert key_map['a']['f'][1] == set()
    assert key_map['a']['g'][1] == set()
    assert key_map['a']['h'][1] == set()
    assert key_map['a']['i'][1] == set('cg')
    assert key_map['a']['j'][1] == set('ab')
    assert key_map['a']['k'][1] == set('e')
    assert key_map['a']['l'][1] == set('df')
    assert key_map['a']['m'][1] == set('ch')
    assert key_map['a']['n'][1] == set('bg')
    assert key_map['a']['o'][1] == set('df')
    assert key_map['a']['p'][1] == set('eh')


def test5():
    base_map, key_locations = parse_map(TEST_INPUT_5)
    key_map = make_key_map(key_locations, base_map)
    p = bfs_keys(key_map)
    d = path_length(p, key_map)
    print(p)
    print(d)


def main():
    # test1()
    # test2()
    # test3()
    # test5()
    # test4()
    test4a()


if __name__ == "__main__":
    main()
