#!python3


from hashlib import md5
from queue import SimpleQueue


INPUT = 'edjrjqaa'

TEST_INPUT1 = 'ihgpwlah'
TEST_PATH1 = 'DDRRRD'
TEST_INPUT2 = 'kglvqrro'
TEST_PATH2 = 'DDUDRLRRUDRD'
TEST_INPUT3 = 'ulqzkmiv'
TEST_PATH3 = 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'

OPEN_CHRS = 'bcdef'

STEP_ORDER = 'UDLR'

MIN = 0
MAX = 3
GOAL = 3, 3

current_input = TEST_INPUT2


def is_valid_location(location):
    x, y = location
    return MIN <= x <= MAX and MIN <= y <= MAX


def move(location, direction):
    x, y = location
    if direction == 'U':
        return x, y - 1
    elif direction == 'D':
        return x, y + 1
    elif direction == 'L':
        return x - 1, y
    elif direction == 'R':
        return x + 1, y
    else:
        assert False


def get_neighbours(location, path, passcode):
    h = md5(f'{passcode}{path}'.encode('utf8')).hexdigest()
    n = []
    for c, direction in zip(h, STEP_ORDER):
        if c not in OPEN_CHRS:
            continue
        new_location = move(location, direction)
        if is_valid_location(new_location):
            new_path = path + direction
            n.append((new_location, new_path))
    return n


def part1(passcode):
    start = 0, 0
    queue = SimpleQueue()
    queue.put((start, ''))
    while not queue.empty():
        location, path = queue.get()
        if location == GOAL:
            return path
        for x in get_neighbours(location, path, passcode):
            queue.put(x)


def part2(passcode):
    longest_path = ''
    start = 0, 0
    queue = SimpleQueue()
    queue.put((start, ''))
    while not queue.empty():
        location, path = queue.get()
        if location == GOAL:
            if len(path) > len(longest_path):
                longest_path = path
        else:
            for x in get_neighbours(location, path, passcode):
                queue.put(x)

    return len(longest_path)


def test1():
    assert part1(TEST_INPUT1) == TEST_PATH1
    assert part1(TEST_INPUT2) == TEST_PATH2
    assert part1(TEST_INPUT3) == TEST_PATH3


def test2():
    assert part2(TEST_INPUT1) == 370
    assert part2(TEST_INPUT2) == 492
    assert part2(TEST_INPUT3) == 830


def main():
    test1()
    p = part1(INPUT)
    print(p)

    test2()
    p = part2(INPUT)
    print(p)


if __name__ == '__main__':
    main()
