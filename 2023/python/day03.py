from help import get_input

'''
Too low:
- 537710

'''

TEST1 = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''


def adjacent(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return dx <=1 and dy <= 1


def part1(n, n_ps, symbols):
    for n_p in n_ps:
        for p in symbols:
            if adjacent(n_p, p):
                return n
    return 0


def part2(g, n, n_ps):
    for n_p in n_ps:
        if adjacent(g, n_p):
            return True
    return False


def main():
    d = get_input('03').strip().split('\n')
    # d = TEST1.strip().split('\n')
    ns = []
    n_ps = set()
    symbols = set()
    gears = set()
    for y, l in enumerate(d):
        n = 0

        for x, c in enumerate(l):
            p = x, y
            if c.isdigit():
                n_ps.add(p)
                if n == 0:
                    n = int(c)
                else:
                    n = 10*n + int(c)
            elif c == '.':
                if n != 0:
                    ns.append((n, n_ps))
                    n = 0
                    n_ps = set()
            else:
                if n != 0:
                    ns.append((n, n_ps))
                    n = 0
                    n_ps = set()
                p = x, y
                symbols.add(p)
                if c == '*':
                    gears.add(p)

        if n != 0:
            ns.append((n, n_ps))
            n = 0
            n_ps = set()

    t1 = 0
    for n, n_ps in ns:
        t1 += part1(n, n_ps, symbols)

    t2 = 0
    for g in gears:
        n_g = []
        for n, n_ps in ns:
            if part2(g, n, n_ps):
                n_g.append(n)
        if len(n_g) == 2:
            a = n_g[0]
            b = n_g[1]
            t2 += a * b

    print(t1)
    print(t2)


if __name__ == '__main__':
    main()
