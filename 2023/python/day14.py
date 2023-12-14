
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


d = get_input('14').strip()
# d = TEST.strip()

dish = [list(row) for row in d.split('\n')]

# print('\n'.join(''.join(row) for row in dish))

for c in range(len(dish[0])):

    # print('\ncolumn', c)
    # print('\n'.join(''.join(row) for row in dish))
    # print()

    for r in range(1, len(dish)):
        rock = dish[r][c]
        # print(r, c, rock)
        if rock == 'O':
            # print('move from', r, c)
            for r1 in range(r - 1, -1, -1):
                item = dish[r1][c]
                # print('\t', r1, c, item)
                if item != '.':
                    # print('move from', r, c, 'to', r1, c)
                    dish[r][c] = '.'
                    dish[r1 + 1][c] = 'O'
                    # print('\t', r1 + 1, c)
                    break
            else:
                dish[r][c] = '.'
                dish[r1][c] = 'O'
                # print('\t', r1, c)


# print()
# print('\n'.join(''.join(row) for row in dish))

p1 = 0
c_count = len(dish)
for i, row in enumerate(dish):
    # print(c_count - i, i, row)
    for item in row:
        if item == 'O':
            p1 += c_count - i

print(p1)