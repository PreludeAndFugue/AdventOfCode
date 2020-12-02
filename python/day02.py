#!python3

INPUT = 'day02.txt'
TEST_INPUT = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
2-9 c: cccccccccc'''
TEST_OUTPUT = [True, False, True, False]


def get_input(input):
    for line in input:
        r, l, p = line.strip().split()
        r1, r2 = list(map(int, r.split('-')))
        r = range(r1, r2 + 1)
        l = l[0]
        yield r, l, p


def is_valid(r, l, p):
    l_count = p.count(l)
    return l_count in r


def test1():
    test = get_input(TEST_INPUT.split('\n'))
    for (r, l, p), result in zip(test, TEST_OUTPUT):
        assert is_valid(r, l, p) == result


def part1():
    p = sum(is_valid(*data) for data in get_input(open(INPUT, 'r')))
    return p


def main():
    test1()
    p = part1()
    print(p)


if __name__ == "__main__":
    main()
