#!python 3

SOURCE = 'day03.txt'


def triangles():
    with open(SOURCE, 'r') as f:
        for line in f.readlines():
            yield sorted(map(int, line.strip().split()))


def main1():
    count = 0
    for t in triangles():
        if sum(t[:2]) > t[2]:
            count += 1
    print(count)


if __name__ == '__main__':
    main1()
