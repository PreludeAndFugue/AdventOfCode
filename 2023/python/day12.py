from functools import cache
from itertools import combinations, permutations
from time import perf_counter

from tqdm import tqdm

from help import get_input

TEST = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''


def parse(d):
    for l in d.split('\n'):
        s, ns = l.split(' ')
        ns = ns.split(',')
        ns = [int(n) for n in ns]
        yield s, ns


def is_valid(s, ns):
    t = 0
    ts = []
    for ch in s:
        if ch == '#':
            t += 1
        if ch == '.':
            if t > 0:
                ts.append(t)
                t = 0
    if t > 0:
        ts.append(t)
    # print(ns, ts)
    return ns == ts


def get_bins(h, q_count):
    for i in range(2 ** q_count):
        if i.bit_count() != h:
            continue
        yield i


def unfold(s, ns):
    ss = [s] * 5
    ss = '?'.join(ss)
    ns = ns * 5
    return ss, ns


def part2(s, ns):
    print('part 2', s, ns)
    if not s:
        if not ns:
            return 1
        return 0
    if not ns:
        if not s:
            return 1
        return 0
    s0 = s[0]
    if s0 == '.':
        yield from part2(s[1:], ns)
    elif s0 == '?':
        # replace ? with .
        yield from part2(s[1:], ns)
        # replace ? with #
        n = ns[0]
        s_sub = s[1:n]
        s_after = s[n + 1]
        if '.' not in s_sub:
            if s_after == '.' or s_after == '?':
                yield from part2(s[n+ 2:], ns[1:])
    elif s0 == '#':
        n = ns[0]
        s_sub = s[1:n]
        s_after = s[n + 1]
        if '.' not in s_sub:
            if s_after == '.' or s_after == '?':
                yield from part2(s[n + 2:], ns[1:])


def part1(d):
    p1 = 0
    for s, ns in parse(d):
        # print(s, ns)
        q_count = s.count('?')
        h_count = s.count('#')
        h_total = sum(ns)
        h = h_total - h_count

        q_indexes = []
        for i, ch in enumerate(s):
            if ch == '?':
                q_indexes.append(i)
        # print(ns, '-- h', h, ' -- ', 'q count', q_count, ' -- ', q_indexes)

        for i in get_bins(h, q_count):
            # print(i)
            chs = []
            for _ in range(q_count):
                chs.append('#' if i & 1 else '.')
                i >>= 1
            # print(chs)

            test = []
            for ch in s:
                if ch == '?':
                    x = chs.pop()
                    test.append(x)
                else:
                    test.append(ch)
            # print(test)
            if is_valid(test, ns):
                p1 += 1
    return p1


# @cache
def create(s, ns):
    print('create', repr(s), ns)
    if not s:
        if ns:
            yield 0
        else:
            yield 1
    elif not ns:
        if s:
            if '#' in s:
                yield 0
            else:
                yield 1
    else:
        s0 = s[0]
        if s0 == '.':
            yield from create(s[1:], ns)
        elif s0 == '?':
            yield from create(s[1:], ns)
            yield from create('#' + s[1:], ns)
        elif s0 == '#':
            n = ns[0]
            s_part = s[:n]
            l = len(s_part)
            if l < n:
                yield 0
            elif '.' in s_part:
                yield 0
            elif l == n:
                s = s[n:]
                ls = len(s)
                if ls == 0:
                    yield from create('', ns[1:])
                else:
                    x = s[0]
                    if x == '.' or x == '?':
                        yield from create(s[1:], ns[1:])
                    else:
                        yield 0
            else:
                raise ValueError
        else:
            raise ValueError


def part1a(d):
    p1 = 0
    for s, ns in parse(d):
        # s, ns = unfold(s, ns)
        print(s, ns)
        print()

        for n in create(s, tuple(ns)):
            # print('\t', pattern, pattern.count('#'))
            # input()
            p1 += n
            if n:
                print('\tyes')
            else:
                print('\tno')
            # if is_valid(pattern, ns):
            #     p1 += 1
            # else:
            #     print(pattern)
        print()
        input()

    return p1

def test():
    s = '???'
    ns = (1,)
    t = 0
    for x in create(s, ns):
        print(x)
        t += x
    print('t =', t)


def main():
    # d = get_input('12').strip()
    d = TEST.strip()

    t1 = perf_counter()

    # p1 = part1(d)
    p1 = part1a(d)
    # test()

    t2 = perf_counter()
    print('dt', t2 - t1)

    print(p1)


if __name__ == '__main__':
    main()
