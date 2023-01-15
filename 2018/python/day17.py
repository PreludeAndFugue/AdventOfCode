#!python3

import heapq
import re

'''
Too low: 864.

'''

INPUT = 'day17.txt'

TEST_INPUT = '''x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
'''

TEST_2 ='''
..............+...............
..............................
..............................
..............................
..............................
..............................
........................#.....
.......#................#.....
.......#................#.....
.......#................#.....
.......#................#.....
.......#................#.....
.......#......#.#.......#.....
.......#......#.#.......#.....
.......#......#.#.......#.....
.......#......###.......#.....
.......#................#.....
.......#................#.....
.......#................#.....
.......#................#.....
.......##################.....
..............................
..............................
..............................
'''


TEST_3 = '''
....................+.....................
..........................................
.......#..................................
.......#..........................#.......
.......#..........................#.......
.......#.........########.........#.......
.......#.........#......#.........#.......
.......#.........########.........#.......
.......#..........................#.......
.......#..........................#.......
.......#..........................#.......
.......#..........................#.......
.......#..........................#.......
.......############################.......
..........................................
..........................................
'''


pattern = r'(\w)=(\d+), \w=(\d+)..(\d+)'
regex = re.compile(pattern)


def temp_scan(string):
    m = {}
    start = None
    for y, line in enumerate(string.strip().split()):
        for x, c in enumerate(line.strip()):
            if c == '#':
                m[(x, y)] = c
            if c == '+':
                m[(x, y)] = c
                start = x, y
    y_max = max(y for _, y in m.keys())
    return m, start, y_max


def read_scan(scan):
    for line in scan.strip().split('\n'):
        m = regex.match(line)
        first_coord = m.group(1)
        first_value = int(m.group(2))
        range_start = int(m.group(3))
        range_end = int(m.group(4))
        r = range(range_start, range_end + 1)
        if first_coord == 'x':
            yield first_value, r
        else:
            yield r, first_value


def draw_map(m, depth_map):
    flows = set()
    for v in depth_map.values():
        flows.update(v)

    xs = sorted(x for x, _ in m.keys())
    ys = sorted(y for _, y in m.keys())
    x_min = min(xs)
    x_max = max(xs)
    y_min = min(ys)
    y_max = max(ys)
    print('xs', x_min, x_max)
    print('ys', y_min, y_max)
    rows = []
    for y in range(y_min, y_max + 1):
        row = []
        for x in range(x_min - 1, x_max + 2):
            l = x, y
            if l in flows:
                row.append('|')
            else:
                row.append(m.get((x, y), '.'))
        rows.append(''.join(row))
    return '\n'.join(rows)


def make_map(scan):
    m = {}
    m[(500, 0)] = '+'
    for x, y in scan:
        if isinstance(x, int):
            for i in y:
                m[(x, i)] = '#'
        else:
            for i in x:
                m[(i, y)] = '#'

    y_max = max(y for _, y in m.keys())
    return m, (500, 0), y_max


def can_move_left(location, m):
    x, y = location
    below = x, y + 1
    below_content = m.get(below, '.')
    if below_content == '#':
        return True
    below_left = x - 1, y + 1
    below_left_content = m.get(below_left, '.')
    if below_left_content == '#':
        return True
    if below_left_content == '~':
        return True


def can_move_right(location, m):
    x, y = location
    below = x, y + 1
    below_content = m.get(below, '.')
    if below_content == '#':
        return True
    below_right = x + 1, y + 1
    below_right_content = m.get(below_right, '.')
    if below_right_content == '#':
        return True
    if below_right_content == '~':
        return True


def get_next_locations(location, m, seen, y_max):
    print('get neighbours of ', location)
    x, y = location
    if y >= y_max:
        print('at max depth - no neighbours')
        return []
    below = x, y + 1
    below_content = m.get(below, '.')
    if y + 1 <= y_max and below_content == '.':
        return [below]
    left = x - 1, y
    left_content = m.get(left, '.')
    right = x + 1, y
    right_content = m.get(right, '.')
    next_locations = []
    if left not in seen and left_content == '.':
        if can_move_left(location, m):
            next_locations.append(left)
    if right not in seen and right_content == '.':
        if can_move_right(location, m):
            next_locations.append(right)

    return next_locations


def get_x_bounds(m):
    xs = [x for x, _ in m.keys()]
    xs.sort()
    return xs[0], xs[-1]


def has_both_walls(location, m):
    '''
    Does the currently location have a wall both to the left and the right.

        #X.....#
        ########

        #X.....#
        #~~~~~~#
        ########

        ..X......#
        .#########
    '''
    print('checking has both walls')
    x_min, x_max = get_x_bounds(m)
    has_left = False
    has_right = False
    # check left
    x, y = location
    l = x
    while True:
        l -= 1
        left = l, y
        below_left = l, y + 1
        left_content = m.get(left, '.')
        below_left_content = m.get(below_left, '.')

        if left_content == '#' and below_left_content == '#':
            has_left = True
            break

        if below_left_content != '#' and below_left_content != '~':
            has_left = False
            break

        if left_content == '.' and below_left_content == '.':
            has_left = False
            break

    print('has left', has_left)

    if not has_left:
        return False

    # check right
    r = x
    while True:
        r += 1
        right = r, y
        below_right = r, y + 1
        right_content = m.get(right, '.')
        below_right_content = m.get(below_right, '.')

        print(right, right_content, below_right, below_right_content)


        print(1, right_content == '#' and below_right_content == '#')
        if right_content == '#' and below_right_content == '#':
            has_right = True
            break

        print(2, below_right_content != '#' and below_right_content != '~')
        if below_right_content != '#' and below_right_content != '~':
            has_right = False
            break

        if right_content == '.' and below_right_content == '.':
            has_right = False
            break

    print('has right', has_right)
    return has_right


def export_map(m, depth_map):
    d = draw_map(m, depth_map)
    with open('map17.txt', 'w') as f:
        f.write(d)


def run(m, start, y_max):
    # scan = read_scan(TEST_INPUT)

    # r = open(INPUT, 'r').read().strip()
    # scan = read_scan(r)

    # m, y_max = make_map(scan)
    # start = 500, 1
    seen = set()
    depth_map = {0: [start]}

    # distance, location
    q = [0]
    heapq.heapify(q)

    print('max y', y_max)
    print(q)
    print('depth map', depth_map)

    while q:
        print(q)
        d = q[0]
        locations = depth_map.get(d, [])
        print('heap size', len(q))
        print(d, locations)
        print(draw_map(m, depth_map))
        input()

        new_neighbours = []
        for location in locations:
            ns = get_next_locations(location, m, seen, y_max)
            for n in ns:
                if n in seen:
                    continue
                seen.add(n)
                new_neighbours.append(n)

        if new_neighbours:
            heapq.heappush(q, d - 1)

            if (d - 1) in depth_map:
                depth_map[d - 1].extend(new_neighbours)
            else:
                depth_map[d - 1] = new_neighbours

            # depth_map.get(d - 1, []).extend(new_neighbours)
        else:
            print('no neighbours')
            _ = heapq.heappop(q)

            # clear depth map at `d`?

            for location in locations:
                if has_both_walls(location, m):
                    m[location] = '~'
                else:
                    m[location] = '|'

    count = 0
    for v in m.values():
        if v == '~' or v == '|':
            count += 1
    print(count)

    export_map(m, depth_map)

    # print(draw_map(m, depth_map))


def test2():
    m, start, y_max = temp_scan(TEST_3)

    # r = open(INPUT, 'r').read().strip()
    # scan = read_scan(r)
    # m, start, y_max = make_map(scan)


    print(start)
    print(y_max)
    print(draw_map(m, dict()))

    run(m, start, y_max)


def main():
    # test1()
    pass


if __name__ == "__main__":
    # r = open(INPUT, 'r').read().strip()
    # scan = read_scan(r)
    # m, y_max = make_map(scan)
    # draw_map(m, [])

    # main()

    test2()
