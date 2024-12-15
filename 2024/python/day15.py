
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

test3 = '''#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^'''

MOVEMENT = {
    '^': UP,
    '>': RIGHT,
    '<': LEFT,
    'v': DOWN
}

def expand_row(row):
    r = []
    for ch in row:
        if ch in ('.', '#'):
            r.append(ch*2)
        elif ch == '@':
            r.append('@.')
        elif ch == 'O':
            r.append('[]')
        else:
            raise ValueError
    return ''.join(r)


def parse(source, part2):
    m, movements = source.split('\n\n')
    movements = ''.join(movements.split('\n'))
    map_ = {}
    start = None
    for r, row in enumerate(m.split('\n')):
        if part2:
            row = expand_row(row)
        for c, ch in enumerate(row):
            if ch == '#':
                continue
            if ch == '@':
                start = r, c
                ch = '.'
            map_[(r, c)] = ch
    return start, movements, map_


def expand(map_source):
    pass


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

def move_box_horizontal(b, d, map_):
    r, c = b
    boxes = [b]
    dr, dc = d
    dr *= 2
    dc *= 2
    while True:
        r += dr
        c += dc
        pp = r, c
        ch = map_.get(pp, '#')
        if ch == '#':
            return False
        if ch in '[]':
            boxes.append(pp)
        if ch == '.':
            break

    map_[b] = '.'
    is_left = d == LEFT
    parts = '][' if is_left else '[]'
    for p in boxes:
        r, c = p
        r += d[0]
        c += d[1]
        map_[(r, c)] = parts[0]
        r += d[0]
        c += d[1]
        map_[(r, c)] = parts[1]
    return True


def can_move_box_vertical(b, d, map_):
    box = [b]
    r, c = b
    ch = map_[b]
    if ch == '[':
        b1 = r, c + 1
    else:
        b1 = r, c - 1
    box.append(b1)
    box.sort()

    dr, dc = d
    chs = ''
    for bb in box:
        r, c = bb
        rr = r + dr
        cc = c + dc
        chs += map_.get((rr, cc), '#')

    if chs == '..':
        return True
    if '#' in chs:
        return False
    elif chs == '[]':
        b = box[0]
        r, c = b
        r += dr
        c += dc
        return can_move_box_vertical((r, c), d, map_)
    elif chs == '][':
        b0 = box[0]
        r0, c0 = b0
        bb0 = r0 + dr, c0 + dc
        b1 = box[1]
        r1, c1 = b1
        bb1 = r1 + dr, c1 + dc
        m1 = can_move_box_vertical(bb0, d, map_)
        m2 = can_move_box_vertical(bb1, d, map_)
        return m1 and m2
    elif chs == '.[':
        b = box[1]
        r, c = b
        r += dr
        c += dc
        return can_move_box_vertical((r, c), d, map_)
    elif chs == '].':
        b = box[0]
        r, c = b
        r += dr
        c += dc
        return can_move_box_vertical((r, c), d, map_)
    else:
        raise ValueError(chs)


def move_box_vertical(b, d, map_):
    box = [b]
    r, c = b
    ch = map_[b]
    if ch == '[':
        b1 = r, c + 1
    else:
        b1 = r, c - 1
    box.append(b1)
    box.sort()

    dr, dc = d
    chs = ''
    for bb in box:
        r, c = bb
        rr = r + dr
        cc = c + dc
        chs += map_[(rr, cc)]

    if chs == '..':
        pass
    elif '#' in chs:
        raise ValueError
    elif chs == '[]':
        b = box[0]
        r, c = b
        r += dr
        c += dc
        move_box_vertical((r, c), d, map_)
    elif chs == '][':
        b0 = box[0]
        r0, c0 = b0
        bb0 = r0 + dr, c0 + dc
        b1 = box[1]
        r1, c1 = b1
        bb1 = r1 + dr, c1 + dc
        move_box_vertical(bb0, d, map_)
        move_box_vertical(bb1, d, map_)
    elif chs == '.[':
        b = box[1]
        r, c = b
        r += dr
        c += dc
        move_box_vertical((r, c), d, map_)
    elif chs == '].':
        b = box[0]
        r, c = b
        r += dr
        c += dc
        move_box_vertical((r, c), d, map_)
    else:
        raise ValueError

    parts = '[]'
    for b, p in zip(box, parts):
        r, c = b
        map_[b] = '.'
        rr = r + dr
        cc = c + dc
        map_[(rr, cc)] = p


def move_box_2(b, d, map_):
    horizontal = d in (LEFT, RIGHT)
    if horizontal:
        return move_box_horizontal(b, d, map_)
    else:
        if can_move_box_vertical(b, d, map_):
            move_box_vertical(b, d, map_)
            return True
        else:
            return False


def move(p, d, move_box, map_):
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
    else:
        return p


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


def score2(map_):
    t = 0
    for (r, c), ch in map_.items():
        if ch == '[':
            t += 100*r + c
    return t


def part1():
    # source = test1.strip()
    # source = test2.strip()
    source = get_input(15)

    p, movements, map_ = parse(source, False)

    for m in movements:
        d = MOVEMENT[m]
        p = move(p, d, move_box, map_)
    print(score(map_))


def part2():
    # source = test1.strip()
    # source = test2.strip()
    # source = test3.strip()
    source = get_input(15)

    p, movements, map_ = parse(source, True)

    for m in movements:
        d = MOVEMENT[m]
        p = move(p, d, move_box_2, map_)

    print(score2(map_))


# part1()
part2()
