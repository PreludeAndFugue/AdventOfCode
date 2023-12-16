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


def unfold(s, ns):
    ss = [s] * 5
    ss = '?'.join(ss)
    ns = ns * 5
    return ss, ns


@cache
def create(s, ns):
    if not s:
        if ns:
            return 0
        else:
            return 1
    elif not ns:
        if s:
            if '#' in s:
                return 0
            else:
                return 1
    else:
        s0 = s[0]
        if s0 == '.':
            return create(s[1:], ns)
        elif s0 == '?':
            x1 = create(s[1:], ns)
            x2 = create('#' + s[1:], ns)
            return x1 + x2
        elif s0 == '#':
            n = ns[0]
            s_part = s[:n]
            l = len(s_part)
            if l < n:
                return 0
            elif '.' in s_part:
                return 0
            elif l == n:
                s = s[n:]
                ls = len(s)
                if ls == 0:
                    return create('', ns[1:])
                else:
                    x = s[0]
                    if x == '.' or x == '?':
                        return create(s[1:], ns[1:])
                    else:
                        return 0
            else:
                raise ValueError
        else:
            raise ValueError


def part(d, do_unfold=False):
    p1 = 0
    for s, ns in parse(d):
        if do_unfold:
            s, ns = unfold(s, ns)

        n = create(s, tuple(ns))
        p1 += n

    return p1


def main():
    d = get_input('12').strip()
    # d = TEST.strip()

    p1 = part(d)
    print(p1)

    p2 = part(d, True)
    print(p2)


if __name__ == '__main__':
    main()
