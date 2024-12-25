
from help import get_input

test1 = '''#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####'''


def parse(source):
    keys = []
    locks = []
    for x in source.split('\n\n'):
        rows = x.split('\n')
        t = list(''.join(y) for y in zip(*rows))
        ns = [y.count('#') - 1 for y in t]
        if rows[0] == '#####':
            locks.append(tuple(ns))
        else:
            keys.append(tuple(ns))
    return locks, keys


def match(lock, key):
    x = all(l + k <= 5 for l, k in zip(lock, key))
    return x


# source = test1.strip()
source = get_input(25)
locks, keys = parse(source)

c = 0
for lock in locks:
    for key in keys:
        if match(lock, key):
            c += 1
print(c)
