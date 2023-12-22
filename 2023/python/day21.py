
from help import get_input

TEST = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''

d = get_input('21').strip()
# d = TEST.strip()

map_ = set()
start = None
for r, line in enumerate(d.split('\n')):
    for c, ch in enumerate(line):
        # print(r, c, ch)
        if ch == '.':
            map_.add(complex(r, c))
        elif ch == 'S':
            start = complex(r, c)
            map_.add(start)
        else:
            pass

# print(map_)
# print(start)

DIR = (complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1))

positions = set([start])
for _ in range(64):
    new_positions = set()
    for p in positions:
        for d in DIR:
            pp = p + d
            if pp in map_:
                new_positions.add(pp)
    positions = new_positions

print(len(positions))

