from collections import Counter

from help import get_input

TEST = '''Time:      7  15   30
Distance:  9  40  200'''


def main():
    d = get_input('06').strip()
    # d = TEST.strip()
    times, distances = d.split('\n')
    times = [int(n) for n in times.split(':')[1].strip().split()]
    distances = [int(n) for n in distances.split(':')[1].strip().split()]

    max_ss = []
    for t, d in zip(times, distances):
        c = Counter()
        for v in range(t + 1):
            dt = t - v
            s = v * dt
            c[s] += 1
            print('\t', v,  dt, s)
        w = 0
        for k, v in c.items():
            if k > d:
                w += v
        max_ss.append(w)

    n = 1
    for m in max_ss:
        n *= m
    print(n)


if __name__ == '__main__':
    main()
