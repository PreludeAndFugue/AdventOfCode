
from help import get_input

TEST01 = '''987654321111111
811111111111119
234234234234278
818181911112111'''

source = TEST01.strip()
source = get_input(3)


def part1():
    t = 0
    for line in source.split('\n'):
        # print(line)
        ds = list(map(int, line.strip()))
        m = max(ds[:-1])
        # print(f'Max digit: {m}')
        i = ds.index(m)
        n = max(ds[i+1:])
        # print(f' Next max: {n}')
        t += 10*m + n

    return t


if __name__ == '__main__':
    p1 = part1()
    print(p1)
