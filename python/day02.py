#!python3

INPUT = 'day02.txt'
TEST_INPUT = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
2-9 c: cccccccccc'''
TEST_OUTPUT = [True, False, True, False]
TEST_OUTPUT2 = [True, False, False, False]


def get_input(input):
    for line in input:
        r, l, p = line.strip().split()
        r1, r2 = list(map(int, r.split('-')))
        r = range(r1, r2 + 1)
        l = l[0]
        yield r, l, p


def is_valid1(r, l, p):
    l_count = p.count(l)
    return l_count in r


def is_valid2(r, l, p):
    p1 = p[r.start - 1] == l
    p2 = p[r.stop - 2] == l
    return p1 != p2


def test1(input):
    for (r, l, p), result in zip(input, TEST_OUTPUT):
        assert is_valid1(r, l, p) == result


def test2(input):
    for data, result in zip(input, TEST_OUTPUT2):
        assert is_valid2(*data) == result


def part(input, is_valid):
    p = sum(is_valid(*data) for data in input)
    return p


def main():
    test_input = list(get_input(TEST_INPUT.split('\n')))
    test1(test_input)

    input = list(get_input(open(INPUT, 'r')))
    p = part(input, is_valid1)
    print(p)

    test2(test_input)
    p = part(input, is_valid2)
    print(p)


if __name__ == "__main__":
    main()
