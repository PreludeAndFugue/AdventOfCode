#!python 3

from itertools import chain

SOURCE = 'day03.txt'


def triangles():
    with open(SOURCE, 'r') as f:
        for line in f.readlines():
            yield map(int, line.strip().split())


def transpose(matrix):
    return zip(*matrix)


def is_valid(triangle):
    t = sorted(triangle)
    if sum(t[:2]) > t[2]:
        return True
    else:
        return False


def main1():
    count = 0
    for t in triangles():
        if is_valid(t):
            count += 1
    print(count)


def run2():
    ts = list(triangles())
    triangle = []
    for i, x in enumerate(chain(*transpose(ts)), start=1):
        triangle.append(x)
        if i % 3 == 0:
            yield triangle
            triangle = []


def main2():
    count = 0
    for t in run2():
        if is_valid(t):
            count += 1
    print(count)



if __name__ == '__main__':
    main1()
    main2()
