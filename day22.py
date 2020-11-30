#!python3

from itertools import product
import re

INPUT = 'day22.txt'

prog = re.compile(r'/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+\d+T\s+\d+%')


class Node(object):
    def __init__(self, x, y, size, used):
        self.x = x
        self.y = y
        self.size = size
        self.used = used


    @property
    def free(self):
        return self.size - self.used


    @property
    def is_empty(self):
        return self.used == 0


    @classmethod
    def make_from_groups(cls, groups):
        values = map(int, groups)
        return cls(*values)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return f'N({self.x}, {self.y}, {self.size}, {self.used})'


def make_nodes(input):
    nodes = []
    for line in open(input, 'r').readlines():
        m = prog.match(line)
        if m is None:
            continue
        node = Node.make_from_groups(m.groups())
        nodes.append(node)
    return nodes


def viable_pair(n1, n2):
    if n1.is_empty:
        return False
    if n1 == n2:
        return False
    return n1.used <= n2.free


def part1():
    nodes = make_nodes(INPUT)
    total = 0
    for n1, n2 in product(nodes, repeat=2):
        if viable_pair(n1, n2):
            total += 1
    return total


def main():
    p = part1()
    print(p)


if __name__ == '__main__':
    main()
