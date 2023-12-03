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


def adj(n, n_ps, symbols):
    for n_p in n_ps:
        for p in symbols:
            if adjacent(n_p, p):
                return n
    return 0


def main():
    d = get_input('03').strip().split('\n')
    # d = TEST1.strip().split('\n')
    ns = []
    n_ps = set()
    symbols = set()
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

        if n != 0:
            ns.append((n, n_ps))
            n = 0
            n_ps = set()

    t = 0
    for n, n_ps in ns:
        t += adj(n, n_ps, symbols)

    print(t)


if __name__ == '__main__':
    main()
