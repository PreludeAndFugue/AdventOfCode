#!python
'''
2 3
    0 3
        m: 10 11 12
    1 1
        0 1
            m: 99
        m: 2
    m: 1 1 2
'''

INPUT = '8.txt'

TEST_INPUT = '''2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'''


def parse_input(data):
    return map(int, data.split(' '))


class Node(object):
    def __init__(self, child_count, meta_count, children, meta_data):
        self.child_count = child_count
        self.meta_count = meta_count
        self.children = children
        self.meta_data = meta_data
        self.child_map = {i + 1: c for i, c in enumerate(children)}


    def meta_data_sum(self):
        s = 0
        for child in self.children:
            s += child.meta_data_sum()
        return s + sum(self.meta_data)


    def value(self):
        assert self.child_count == len(self.children)
        assert self.meta_count == len(self.meta_data)
        if self.child_count == 0:
            return sum(self.meta_data)
        else:
            s = 0
            for n in self.meta_data:
                child = self.child_map.get(n, None)
                if child is not None:
                    s += child.value()
            return s


    def __repr__(self):
        c_count = len(self.children)
        return f'Node({self.child_count}, {self.meta_count}, children: {c_count}, meta: {self.meta_data})'


def make_nodes(data):
    child_count = next(data)
    meta_count = next(data)
    children = []
    meta_data = []

    for _ in range(child_count):
        child = make_nodes(data)
        children.append(child)

    for _ in range(meta_count):
        meta_data.append(next(data))

    return Node(child_count, meta_count, children, meta_data)


def test1(data):
    node = make_nodes(data)
    assert node.meta_data_sum() == 138


def part1(data):
    node = make_nodes(data)
    return node.meta_data_sum()


def test2(data):
    node = make_nodes(data)
    assert node.value() == 66


def part2(data):
    node = make_nodes(data)
    return node.value()



def main():
    test1(parse_input(TEST_INPUT))

    data1 = parse_input(open(INPUT, 'r').read())
    p = part1(data1)
    print(p)

    test2(parse_input(TEST_INPUT))

    data2 = parse_input(open(INPUT, 'r').read())
    p =part2(data2)
    print(p)


if __name__ == '__main__':
    main()
