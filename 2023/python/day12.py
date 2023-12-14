from itertools import combinations, permutations

from tqdm import tqdm

from help import get_input

TEST = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''

# d = get_input('12').strip()
d = TEST.strip()


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


p1 = 0
# for l in tqdm(d.split('\n')):
for l in d.split('\n'):
    s, ns = l.split(' ')
    ns = ns.split(',')
    ns = [int(n) for n in ns]

    print(s, ns)

    for x in part2(s, ns):
        print(x)

    input()


    # s, ns = unfold(s, ns)

    # q_count = s.count('?')
    # h_count = s.count('#')
    # h_total = sum(ns)
    # h = h_total - h_count

    # q_indexes = []
    # for i, ch in enumerate(s):
    #     if ch == '?':
    #         q_indexes.append(i)
    # print(l, ns, '-- h', h, ' -- ', 'q count', q_count, ' -- ', q_indexes)

    # for i in tqdm(get_bins(h, q_count)):
    #     # print(i)
    #     chs = []
    #     for j in range(q_count):
    #         chs.append('#' if i & 1 else '.')
    #         i >>= 1
    #     # print(chs)

    #     test = []
    #     for ch in s:
    #         if ch == '?':
    #             x = chs.pop()
    #             test.append(x)
    #         else:
    #             test.append(ch)
    #     # print(test)
    #     if is_valid(test, ns):
    #         p1 += 1

    # input()
print(p1)