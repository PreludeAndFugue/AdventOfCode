#!python3


from queue import Queue

INPUT = 'day18.txt'

TEST_INPUT_1 = '''
#########
#b.A.@.a#
#########
'''

TEST_INPUT_2 = '''
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
'''

TEST_INPUT_3 = '''
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
'''

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

TEST_INPUT_5 = '''
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
'''


def parse_map(input):
    base_map = {}
    start = None
    keys = set()
    for x, line in enumerate(input.strip().split('\n')):
        for y, ch in enumerate(line):
            if ch == '#':
                continue
            if ch ==  '@':
                start = x, y
                ch = '.'
            if ch.isascii() and ch.islower():
                keys.add(ch)
            base_map[(x, y)] = ch
    return base_map, start, keys


def get_neighbours(x, y, base_map):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x = x + dx
        new_y = y + dy
        value = base_map.get((new_x, new_y), None)
        if value is not None:
            yield new_x, new_y, value


def _part1(base_map, start, keys):
    x, y = start
    seen = set()
    to_check = Queue()
    to_check.put((x, y, 0, ''))
    while to_check:
        state = to_check.get()
        x, y, distance, current_keys = state

        # input()
        print(state)

        if set(current_keys) == keys:
            return distance

        seen_before = (x, y, current_keys)
        seen.add(seen_before)

        for n_x, n_y, value in get_neighbours(x, y, base_map):
            # print('neighbour', n_x, n_y, value)
            if value == '.':
                state = (n_x, n_y, distance + 1, current_keys)
                seen_before = (n_x, n_y, current_keys)
                if seen_before not in seen:
                    to_check.put(state)

            elif value.isupper():
                # print('is door', value)
                if value.lower() in current_keys:
                    # print('have key', current_keys)
                    state = (n_x, n_y, distance + 1, current_keys)
                    seen_before = (n_x, n_y, current_keys)
                    if seen_before not in seen:
                        to_check.put(state)
                else:
                    pass
                    # print('dont have key, current keys', current_keys)

            elif value.islower():
                if value not in current_keys:
                    new_keys = current_keys + value
                    # print('got new key', new_keys, distance + 1)
                else:
                    new_keys = current_keys

                state = (n_x, n_y, distance + 1, new_keys)
                seen_before = (n_x, n_y, new_keys)
                if seen_before not in seen:
                    to_check.put(state)
            else:
                raise Exception


def test1():
    base_map, start, keys = parse_map(TEST_INPUT_1)
    return _part1(base_map, start, keys)


def test2():
    base_map, start, keys = parse_map(TEST_INPUT_2)
    return _part1(base_map, start, keys)

def test3():
    base_map, start, keys = parse_map(TEST_INPUT_3)
    return _part1(base_map, start, keys)

def test4():
    base_map, start, keys = parse_map(TEST_INPUT_4)
    return _part1(base_map, start, keys)

def test5():
    base_map, start, keys = parse_map(TEST_INPUT_5)
    return _part1(base_map, start, keys)


def part1():
    base_map, start, keys = parse_map(open(INPUT, 'r').read())
    return _part1(base_map, start, keys)


def main():
    # assert test1() == 8
    # assert test2() == 86
    # assert test3() == 132
    assert test4() == 136
    # assert test5() == 81

    # p = part1()
    # print(p)


if __name__ == "__main__":
    main()
