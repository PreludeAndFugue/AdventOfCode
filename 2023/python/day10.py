
from help import get_input

import sys
sys.setrecursionlimit(30_000)

TEST = '''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L'''

VALID_MOVES = {
    'S': set([(-1, 0), (1, 0), (0, -1), (0, 1)]),
    '|': set([(-1, 0), (1, 0)]),
    '-': set([(0, -1), (0, 1)]),
    'F': set([(1, 0), (0, 1)]),
    '7': set([(1, 0), (0, -1)]),
    'J': set([(-1, 0), (0, -1)]),
    'L': set([(-1, 0), (0, 1)]),
}

MOVES = {
    (-1, 0): set(['|', 'F', '7']),
    (1, 0): set(['|', 'L', 'J']),
    (0, -1): set(['-', 'F', 'L']),
    (0, 1): set(['-', 'J', '7'])
}

NEW_CHAR = {
    'S': '*',
    '-': '\u2501',
    '|': '\u2503',
    'F': '\u250f',
    '7': '\u2513',
    'J': '\u251b',
    'L': '\u2517',
    ' ': ' '
}

LEFT = set(NEW_CHAR[ch] for ch in MOVES[(0, -1)])
RIGHT = set(NEW_CHAR[ch] for ch in MOVES[(0, 1)])
ABOVE = set(NEW_CHAR[ch] for ch in MOVES[(-1, 0)])
BELOW = set(NEW_CHAR[ch] for ch in MOVES[(1, 0)])


class V:
    def __init__(self, position, ch):
        self.position = position
        self.ch = ch
        self.n = 0
        self.discovered = False

    def adjacent(self, G):
        r, c = self.position
        for m in VALID_MOVES[self.ch]:
            dr, dc = m
            rr, cc = r + dr, c + dc
            p = rr, cc
            v = G.get(p, None)
            valid = MOVES[m]
            if v is not None and v.ch in valid:
                yield v

    def __repr__(self) -> str:
        return f'{self.position}: {self.ch}, {self.n}, {self.discovered}'


def search(G, v):
    v.discovered = True
    for w in v.adjacent(G):
        if not w.discovered:
            w.n = v.n + 1
            search(G, w)


def flood(location, expanded):
    ch = expanded.get(location, None)
    if ch is None:
        return
    if ch != ' ':
        return
    expanded[location] = 'O'
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = location
        new_location = r + dr, c + dc
        flood(new_location, expanded)


def parse(d):
    d = get_input('10').strip()
    # d = TEST.strip()
    G = {}
    start = None
    for r, l in enumerate(d.split('\n')):
        for c, p in enumerate(l):
            v = V((r, c), p)
            G[(r, c)] = v
            if p == 'S':
                start = v
    return start, G


def part1(start, G):
    search(G, start)

    discovered = [v for v in G.values() if v.discovered]
    discovered.sort(key=lambda v: v.n)

    return int(len(discovered)/2), discovered


def part2(discovered, G):
    max_r = max(r for r, _ in G.keys()) + 1
    max_c = max(c for _, c in G.keys()) + 1

    expanded = {(r, c): ' ' for r in range(2*max_r) for c in range(2*max_c)}
    for v in discovered:
        r, c = v.position
        new_r = 2*r
        new_c = 2*c
        new_position = new_r, new_c
        if v.ch == 'S':
            expanded[new_position] = NEW_CHAR['|']
        else:
            expanded[new_position] = NEW_CHAR[v.ch]
    for p, ch in expanded.items():
        r, c = p

        left = expanded.get((r, c - 1), None)
        right = expanded.get((r, c + 1), None)
        if left in LEFT and right in RIGHT:
            expanded[p] = NEW_CHAR['-']

        above = expanded.get((r - 1, c), None)
        below = expanded.get((r + 1, c), None)
        if above in ABOVE and below in BELOW:
            expanded[p] = NEW_CHAR['|']

    flood((0, 0), expanded)
    # flood((2*max_r - 1, 0), expanded)
    # flood((0, 2*max_c - 1), expanded)
    # flood((2*max_r - 1, 2*max_c - 1), expanded)

    return sum(1 for (r, c), ch in expanded.items() if r % 2 == 0 and c % 2 == 0 and ch == ' ')


def main():
    d = get_input('10').strip()
    # d = TEST.strip()
    start, G = parse(d)

    p1, discovered = part1(start, G)
    print(p1)

    p2 = part2(discovered, G)
    print(p2)


if __name__ == '__main__':
    main()


# with open('day10.output.txt', 'w') as f:
#     for r in range(max_r):
#         for c in range(max_c):
#             v = G[(r, c)]
#             ch = v.ch if v.discovered else ' '
#             f.write(NEW_CHAR[ch])
#         f.write('\n')

# with open('day10.output.1.txt', 'w') as f:
#     for r in range(2*max_r):
#         for c in range(2*max_c):
#             v = expanded[(r, c)]
#             f.write(v)
#         f.write('\n')

# with open('day10.output.2.txt', 'w') as f:
#     for r in range(max_r):
#         for c in range(max_c):
#             v = unexpanded[(r, c)]
#             f.write(v)
#         f.write('\n')