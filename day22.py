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


def print_nodes(nodes):
    nodes = sorted(nodes, key=lambda n: (n.y, n.x))
    goal_x = max(n.x for n in nodes)
    print(goal_x)
    rows = []
    row = []
    for n in nodes:
        if n.is_empty:
            print(n)
            row.append('_')
        elif n.x == goal_x and n.y == 0:
            print(n)
            row.append('G')
        elif n.used > 200:
            row.append('#')
        else:
            row.append('.')

        if n.x == goal_x:
            r = ' '.join(row)
            rows.append(r)
            row = []
    print('\n'.join(rows))


def part1(nodes):
    total = 0
    for n1, n2 in product(nodes, repeat=2):
        if viable_pair(n1, n2):
            total += 1
    return total


def part2(nodes):
    print_nodes(nodes)


def main():
    nodes = make_nodes(INPUT)
    p = part1(nodes)
    print(p)

    p = part2(nodes)
    print(p)


if __name__ == '__main__':
    main()
