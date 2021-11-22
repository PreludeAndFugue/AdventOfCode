#!python3


INPUT = 'day20.txt'


class ClosedRange(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop


    @property
    def count(self):
        return self.stop - self.start + 1


    def contains(self, n):
        return self.start <= n <= self.stop


    def remove(self, other):
        '''Remove another closed range from this closed range.

        Returns a list of ClosedRanges
        '''
        if other.start < self.start:
            if other.stop < self.start:
                return [self]
            elif other.stop < self.stop:
                return [ClosedRange(other.stop + 1, self.stop)]
            else:
                return []

        elif other.start == self.start:
            if other.stop < self.stop:
                return [ClosedRange(other.stop + 1, self.stop)]
            else:
                return []

        elif self.contains(other.start):
            if other.stop < self.stop:
                return [ClosedRange(self.start, other.start - 1), ClosedRange(other.stop + 1, self.stop)]
            else:
                return [ClosedRange(self.start, other.start - 1)]

        else:
            return [self]


    def __repr__(self):
        return f'[{self.start}, {self.stop}]'


def make_ranges(input):
    lines = open(input, 'r').read().strip().split('\n')
    ranges = []
    for line in lines:
        x, y = line.split('-', 1)
        x, y = int(x), int(y)
        assert x < y
        r = range(x, y + 1)
        ranges.append(r)
    return ranges



def make_closed_ranges(input):
    lines = open(input, 'r').read().strip().split('\n')
    ranges = []
    for line in lines:
        x, y = line.split('-', 1)
        x, y = int(x), int(y)
        assert x < y
        # r = range(x, y + 1)
        r = ClosedRange(x, y)
        ranges.append(r)
    return ranges


def not_in_ranges(n, ranges):
    for r in ranges:
        if n in r:
            return False, r.stop
    return True, None


def part1():
    ranges = make_ranges(INPUT)
    i = 0
    while True:
        result, n = not_in_ranges(i, ranges)
        if result:
            return i
        else:
            i = n


def part2_2():
    ranges = make_closed_ranges(INPUT)
    ranges = sorted(ranges, key=lambda r: r.start)

    MAX = 4294967295
    answer = [ClosedRange(0, MAX)]

    for r in ranges:
        new_answer = []
        for a in answer:
            new_answer.extend(a.remove(r))
        answer = new_answer
    return sum(r.count for r in answer)


def main():
    p = part1()
    print(p)

    p = part2_2()
    print(p)


if __name__ == '__main__':
    main()
