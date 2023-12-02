from help import get_input

MAX = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def main():
    d = get_input('02').strip().split('\n')
    t1 = 0
    t2 = 0
    for l in d:
        g, r = l.split(':', maxsplit=1)
        g = int(g.split(' ')[1])

        # part 1
        g_valid = True
        # part 2
        p2 = {'red': 0, 'green': 0, 'blue': 0}

        for r in r.strip().split('; '):
            parts = r.strip().split(', ')
            parts = [p.split(' ') for p in parts]
            parts = [(p[1], int(p[0])) for p in parts]
            parts = dict(parts)

            for k, v in parts.items():
                # part 1
                if g_valid and MAX[k] < v:
                    g_valid = False
                # part 2
                p2[k] = max(v, p2[k])

        # part 1
        if g_valid:
            t1 += g

        # part 2
        x = 1
        for n in p2.values():
            x *= n
        t2 += x

    print(t1, t2)


if __name__ == '__main__':
    main()
