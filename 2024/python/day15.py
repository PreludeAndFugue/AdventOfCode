
from geometry import UP, DOWN, LEFT, RIGHT

from help import get_input

test1 = '''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<'''

test2 = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''

MOVEMENT = {
    '^': UP,
    '>': RIGHT,
    '<': LEFT,
    'v': DOWN
}

def parse(source):
    m, movements = source.split('\n\n')
    movements = ''.join(movements.split('\n'))
    map_ = {}
    start = None
    for r, row in enumerate(m.split('\n')):
        for c, ch in enumerate(row):
            if ch == '#':
                continue
            if ch == '@':
                start = r, c
                ch = '.'
            map_[(r, c)] = ch
    return start, movements, map_


def move_box(p, d, map_):
    boxes = [p]
    r, c = p
    dr, dc = d
    assert map_[p] == 'O'
    while True:
        r += dr
        c += dc
        pp = r, c
        ch = map_.get(pp, '#')
        if ch == '#':
            return False
        if ch == 'O':
            boxes.append(pp)
        if ch == '.':
            break

    map_[p] = '.'
    pp = boxes[-1]
    rr, cc = pp
    rr += dr
    cc += dc
    pp = rr, cc
    map_[pp] = 'O'

    return True


def move(p, d, map_):
    r, c = p
    dr, dc = d
    rr, cc = r + dr, c + dc
    pp = rr, cc
    ch = map_.get(pp, None)
    if ch is None:
        return p
    if ch == '.':
        return pp
    if move_box(pp, d, map_):
        return pp
    else: return p


def print_map(map_, pp):
    ks = list(map_.keys())
    r_max = max(r for r, _ in ks) + 2
    c_max = max(c for _, c in ks) + 2
    rows = []
    for r in range(0, r_max):
        row = []
        for c in range(0, c_max):
            p = r, c
            ch = map_.get(p, '#')
            if p == pp:
                ch = '@'
            else:
                ch = map_.get(p, '#')
            row.append(ch)
        rows.append(''.join(row))
    print('\n'.join(rows))


def score(map_):
    t = 0
    for (r, c), ch in map_.items():
        if ch == 'O':
            t += 100*r + c
    return t


# source = test1.strip()
# source = test2.strip()
source = get_input(15)

p, movements, map_ = parse(source)

print(p)
print(movements)
for m in movements:
    d = MOVEMENT[m]
    print(d)
    p = move(p, d, map_)

    # print_map(map_, p)
    # input()

print(p)
print_map(map_, p)
print(score(map_))