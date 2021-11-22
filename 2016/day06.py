#!python3

from collections import Counter

SOURCE = 'day06.txt'

TEST1 = '''eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar'''


def main1():
    result = []
    lines = open(SOURCE, 'r').read().strip().split()
    t = zip(*lines)
    for x in t:
        c = Counter(x)
        result.append(c.most_common()[0][0])
    print(''.join(result))


def main2():
    result = []
    lines = open(SOURCE, 'r').read().strip().split()
    t = zip(*lines)
    for x in t:
        c = Counter(x)
        result.append(c.most_common()[-1][0])
    print(''.join(result))


def test1():
    result = []
    lines = TEST1.split()
    t = zip(*lines)
    for x in t:
        c = Counter(x)
        result.append(c.most_common()[0][0])
    assert ''.join(result) == 'easter'


def test2():
    result = []
    lines = TEST1.split()
    t = zip(*lines)
    for x in t:
        c = Counter(x)
        result.append(c.most_common()[-1][0])
    assert ''.join(result) == 'advent'


if __name__ == '__main__':
    test1()
    test2()
    main1()
    main2()
