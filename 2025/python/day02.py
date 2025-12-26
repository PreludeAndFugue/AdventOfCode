
from help import get_input
from maths import divisors

TEST1 = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''

source = get_input(2)
# source = TEST1.strip()


def part1():
    total = 0
    m = 0
    for _range in  source.split(','):
        # print(_range)
        a, b = _range.split('-')
        a = int(a)
        b = int(b)
        for n in range(a, b + 1):
            s = str(n)
            l = len(s)
            if l % 2 != 0:
                continue
            else:
                x, y = s[:l//2], s[l//2:]
                if x == y:
                    total += 1
                    m += n

    return m


def part2():
    m = 0
    for _range in  source.split(','):
        # print(_range)
        a, b = _range.split('-')
        a = int(a)
        b = int(b)
        for n in range(a, b + 1):
            s = str(n)
            l = len(s)
            # print(s)
            ds = divisors(l)
            # print(f'  divisors: {ds}')
            for d in ds[:-1]:
                t = s[:d] * (l // d)
                if t == s:
                    # print('invalid', s)
                    m += n
                    break

    return m



if __name__ == '__main__':
    print(part1())
    print(part2())