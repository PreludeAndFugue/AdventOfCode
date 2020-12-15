#!python3

from collections import namedtuple
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


def bot_sorter(bot):
    return bot.pos


def get_best_bot(bots):
    best_r = 0
    best_bot = None
    for bot in bots:
        if bot.r > best_r:
            best_bot = bot
            best_r = bot.r
    return best_bot


def get_distance(bot1, bot2):
    x1, y1, z1 = bot1.pos
    x2, y2, z2 = bot2.pos
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)


def _part1(bots):
    best_bot = get_best_bot(bots)
    nearby = []
    for bot in bots:
        d = get_distance(best_bot, bot)
        if d <= best_bot.r:
            nearby.append(bot)
    return len(nearby)


def test1():
    bots = list(get_input(TEST_INPUT))
    assert _part1(bots) == 7


def part1():
    bots = list(get_input(open(INPUT, 'r').read()))
    return _part1(bots)


def main():
    test1()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
