
from help import get_input

TEST = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''

TEST_1_CYCLE = '''.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....'''

TEST_2_CYCLE = '''.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O'''

TEST_3_CYCLE = '''.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O'''


# d = get_input('14').strip()
d = TEST.strip()

def make_dish(d):
    return [list(row) for row in d.split('\n')]


def view(dish):
    return '\n'.join(''.join(row) for row in dish)


def move_vertical(dish, north=True):
    R = len(dish)
    offset = 1 if north else -1

    for c in range(len(dish[0])):

        # print('\ncolumn', c)
        # print('\n'.join(''.join(row) for row in dish))
        # print()
        if north:
            range1 = range(1, R)
        else:
            range1 = range(R - 2, -1, -1)

        for r in range1:
            rock = dish[r][c]
            # print(r, c, rock)
            if rock == 'O':
                # print('move from', r, c)

                if north:
                    range2 = range(r - 1, -1, -1)
                else:
                    range2 = range(r + 1, R)

                for r1 in range2:
                    item = dish[r1][c]
                    # print('\t', r1, c, item)
                    if item != '.':
                        # print('move from', r, c, 'to', r1, c)
                        dish[r][c] = '.'
                        dish[r1 + offset][c] = 'O'
                        # print('\t', r1 + 1, c)
                        break
                else:
                    dish[r][c] = '.'
                    dish[r1][c] = 'O'
                    # print('\t', r1, c)


def move_horizontal(dish, west=True):
    C = len(dish[0])
    offset = 1 if west else -1

    for r in range(len(dish)):

        if west:
            range1 = range(1, C)
        else:
            range1 = range(C - 2, -1, -1)

        for c in range1:
            rock = dish[r][c]
            if rock == 'O':

                if west:
                    range2 = range(c - 1, -1, -1)
                else:
                    range2 = range(c + 1, C)

                for c1 in range2:
                    item = dish[r][c1]
                    if item != '.':
                        dish[r][c] = '.'
                        dish[r][c1 + offset] = 'O'
                        break
                else:
                    # print('here', r, c, c1)
                    dish[r][c] = '.'
                    dish[r][c1] = 'O'


def cycle(dish):
    move_vertical(dish, north=True)
    move_horizontal(dish, west=True)
    move_vertical(dish, north=False)
    move_horizontal(dish, west=False)



def load(dish):
    total = 0
    c_count = len(dish)
    for i, row in enumerate(dish):
        # print(c_count - i, i, row)
        for item in row:
            if item == 'O':
                total += c_count - i
    return total


def part1(d):
    dish = make_dish(d)
    move_vertical(dish, north=True)
    return load(dish)


def test2(d):
    dish = make_dish(d)
    cycle(dish)
    assert view(dish) == TEST_1_CYCLE
    cycle(dish)
    assert view(dish) == TEST_2_CYCLE
    cycle(dish)
    assert view(dish) == TEST_3_CYCLE


def part2(d):
    dish = make_dish(d)
    for i in range(1, 200):
        cycle(dish)
        l = load(dish)
        # print(i, l)

    # print(view(dish))


p1 = part1(d)
print(p1)

# test2(d)

p2 = part2(d)
# print(p2)

'''
Test
----
cycle start: 169
cycle end: 175

cycle start: 182
cycle end: 198
'''

values = {
    169: 63,
    170: 68,
    171: 69,
    172: 69,
    173: 65,
    174: 64,
    175: 65,
}

values = {
    182: 100008,
    183: 100011,
    184: 100025,
    185: 100043,
    186: 100071,
    187: 100084,
    188: 100084,
    189: 100086,
    190: 100084,
    191: 100086,
    192: 100086,
    193: 100079,
    194: 100064,
    195: 100047,
    196: 100034,
    197: 100024,
    198: 100016,
}

start = min(values.keys())
end = max(values.keys())

diff = end - start + 1
done = 1_000_000_000


cycles = int((done - end) / diff)

values = {k + diff*cycles: v for k, v in values.items()}
# print(values)
values = {k + diff: v for k, v in values.items()}
print(values[done])