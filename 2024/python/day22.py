
from help import get_input

test1 = '''1
10
100
2024'''

test2 = '''1
2
3
2024'''

X = 2**24 - 1

def secret(n):
    b = n << 6
    n = n^b
    n = n & X
    b = n >> 5
    n = n^b
    n = n & X
    b = n << 11
    n = n^b
    n = n & X
    return n


def part1():
    source = get_input(22)
    ns = [int(x) for x in source.split('\n')]

    t = 0
    for n in ns:
        for i in range(2000):
            n = secret(n)
        t += n
    print(t)


def make_map(n):
    values = [n % 10]
    for _ in range(2000):
        n = secret(n)
        values.append(n % 10)
    assert len(values) == 2001
    diffs = [n2 - n1 for n1, n2 in zip(values, values[1:])]
    map_ = {}
    for i in range(1997):
        n0 = diffs[i]
        n1 = diffs[i + 1]
        n2 = diffs[i + 2]
        n3 = diffs[i + 3]
        k = n0, n1, n2, n3
        v = values[i + 4]
        if k in map_:
            pass
        else:
            map_[k] = v
    return map_


def part2():
    # source = test1.strip()
    # source = test2.strip()
    source = get_input(22)
    ns = [int(x) for x in source.split('\n')]

    all_maps = []
    unique_keys = set()
    for n in ns:
        map_ = make_map(n)
        all_maps.append(map_)
        unique_keys.update(map_.keys())

    t = 0
    for k in unique_keys:
        n = sum(map_.get(k, 0) for map_ in all_maps)
        t = max(t, n)

    print(t)

# part1()
part2()
