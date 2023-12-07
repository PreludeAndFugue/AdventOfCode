from collections import Counter
from math import ceil, sqrt

from help import get_input

TEST = '''Time:      7  15   30
Distance:  9  40  200'''


def main():
    d = get_input('06').strip()
    # d = TEST.strip()
    times, distances = d.split('\n')

    t1 = [int(n) for n in times.split(':')[1].strip().split()]
    d1 = [int(n) for n in distances.split(':')[1].strip().split()]

    t2 = int(''.join(times.split(':')[1].strip().split()))
    d2 = int(''.join(distances.split(':')[1].strip().split()))

    ws = []
    for t, d in zip(t1, d1):
        c = Counter(v*(t - v) for v in range(t + 1))
        w = sum(v for k, v in c.items() if k > d)
        ws.append(w)

    n = 1
    for m in ws:
        n *= m
    print(n)

    def f(x):
        return t2*x - x*x

    def bin_search(l, u, up=True):
        while True:
            x = (u + l) / 2
            y = f(x)
            if up:
                if y < d2:
                    l = x
                elif y > d2:
                    u = x
                else:
                    return x
            else:
                if y > d2:
                    l = x
                elif y < d2:
                    u = x
                else:
                    return x


    x1 = bin_search(0, t2 / 2)
    x1 = int(x1) + 1
    x2 = t2 - x1 + 1
    print(x2 - x1)

    a = ceil(sqrt(t2*t2 - 4*d2))
    print(a)


if __name__ == '__main__':
    main()
