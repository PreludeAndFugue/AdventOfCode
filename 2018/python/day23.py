#!python3

from collections import namedtuple
from itertools import product
import re

INPUT = 'day23.txt'
TEST_INPUT = '''
pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1
'''
TEST_INPUT_2 = '''pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5
'''

Bot = namedtuple('Bot', ['pos', 'r'])
BOT = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)')


def get_input(input):
    for line in input.strip().split('\n'):
        match = re.match(BOT, line)
        x = int(match.group(1))
        y = int(match.group(2))
        z = int(match.group(3))
        r = int(match.group(4))
        pos = (x, y, z)
        yield Bot(pos, r)


def bot_sorter_by_pos(bot):
    return bot.pos


def bot_sorter_by_r(bot):
    return bot.r


def get_best_bot(bots):
    best_r = 0
    best_bot = None
    for bot in bots:
        if bot.r > best_r:
            best_bot = bot
            best_r = bot.r
    return best_bot


def get_distance(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)


def intersect(bot1, bot2):
    d = get_distance(bot1.pos, bot2.pos)
    r = bot1.r + bot2.r
    return d <= r


def is_in_range(bot, pos):
    d = get_distance(bot.pos, pos)
    return d <= bot.r


def spanning_coords(bots):
    xs = [bot.pos[0] for bot in bots]
    ys = [bot.pos[1] for bot in bots]
    zs = [bot.pos[2] for bot in bots]
    return min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)


def smallest_bot(bots):
    best_r = 1_000_000_000
    best_bot = None
    for bot in bots:
        if bot.r < best_r:
            best_bot = bot
            best_r = bot.r
    return best_bot


def _part1(bots):
    best_bot = get_best_bot(bots)
    nearby = []
    for bot in bots:
        d = get_distance(best_bot.pos, bot.pos)
        if d <= best_bot.r:
            nearby.append(bot)
    return len(nearby)


def test1():
    bots = list(get_input(TEST_INPUT))
    assert _part1(bots) == 7


def part1():
    bots = list(get_input(open(INPUT, 'r').read()))
    return _part1(bots)


def _part2(bots):
    xmin, xmax, ymin, ymax, zmin, zmax = spanning_coords(bots)
    max_count = 0
    max_coords = []
    for x, y, z in product(range(xmin, xmax + 1), range(ymin, ymax + 1), range(zmin, zmax + 1)):
        count = sum(1 if is_in_range(bot, (x, y, z)) else 0 for bot in bots)
        if count > max_count:
            max_coords = [(x, y, z)]
            max_count = count
        elif count == max_count:
            max_coords.append((x, y, z))
    return max_coords


def _part2_a(bots):
    '''Partition bots into intersecting sets.'''
    partitions = [[bots[0]]]
    remaining_bots = bots[1:]
    for bot in remaining_bots:
        print('testing bot', bot)
        for p in partitions:
            if all(intersect(bot, b) for b in p):
                p.append(bot)
                print('intersects all in partition')
                break
        else:
            print('bot not in any partition')
            partitions.append([bot])
        print('done testing bot')
    return partitions


def test2():
    bots = list(get_input(TEST_INPUT_2))
    c = _part2(bots)
    print(c)


def test2a():
    bots = list(get_input(TEST_INPUT_2))
    partitions = _part2_a(bots)
    for x in partitions:
        print(len(x))
        print(spanning_coords(x))
        print(smallest_bot(x))
        y = sorted(bots, key=bot_sorter_by_r)
        z = sorted(bots, key=bot_sorter_by_pos)
        print(y[:2])
        print(z[0], z[-1])


def part2():
    bots = list(get_input(open(INPUT, 'r').read()))
    c = _part2(bots)
    return c


def part2a():
    bots = list(get_input(open(INPUT, 'r').read()))
    partitions = _part2_a(bots)
    for x in partitions:
        print(len(x))
        print(spanning_coords(x))
        print(smallest_bot(x))
        y = sorted(bots, key=bot_sorter_by_r)
        z = sorted(bots, key=bot_sorter_by_pos)
        print(y[:2])
        z_first = z[0]
        z_last = z[-1]
        print(z_first, z_last)
        print(intersect(z_first, z_last))


def main():
    test1()

    p = part1()
    print(p)

    test2()
    test2a()

    # p = part2()
    # print(p)

    part2a()


if __name__ == "__main__":
    main()
