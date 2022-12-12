
import heapq

from help import get_input

TEST = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def make_map(s):
    M = dict()
    for i, line in enumerate(s.split('\n')):
        for j, ch in enumerate(line):
            if ch == 'S':
                S = (i, j)
                M[(i, j)] = ord('a')
            elif ch == 'E':
                E = (i, j)
                M[(i, j)] = ord('z')
            else:
                M[(i, j)] = ord(ch)
    return M, S, E


def get_neighbours(l, h, M):
    x, y = l
    for dx, dy in DIR:
        xi = x + dx
        yi = y + dy
        hi = M.get((xi, yi), 1_000_000_000)
        dh = hi - h
        if dh <= 1:
            yield (xi, yi), hi


def part1(M, S, E):
    q = [(0, S)]
    heapq.heapify(q)
    seen = set()

    while q:
        d, l = heapq.heappop(q)
        h = M[l]

        if l == E:
            return d

        for ln, _ in get_neighbours(l, h, M):
            if ln in seen:
                continue
            heapq.heappush(q, (d + 1, ln))
            seen.add(ln)


def main():
    s = get_input('12')
    # s = TEST
    M, S, E = make_map(s)

    p1 = part1(M, S, E)
    print('Part 1:', p1)


if __name__ == '__main__':
    main()
