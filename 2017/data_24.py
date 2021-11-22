#!python3

'''Day 24, part 1.'''

INPUT = '''48/5
25/10
35/49
34/41
35/35
47/35
34/46
47/23
28/8
27/21
40/11
22/50
48/42
38/17
50/33
13/13
22/33
17/29
50/0
20/47
28/0
42/4
46/22
19/35
17/22
33/37
47/7
35/20
8/36
24/34
6/7
7/43
45/37
21/31
37/26
16/5
11/14
7/23
2/23
3/25
20/20
18/20
19/34
25/46
41/24
0/33
3/7
49/38
47/22
44/15
24/21
10/35
6/21
14/50'''


TEST_INPUT = '''0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10'''


class EmptyNodesException(Exception):
    pass


class Node(object):
    '''A node.'''
    def __init__(self, number, empty):
        self.number = number
        self.empty = empty


    def __str__(self):
        x = 'o' if self.empty else 'x'
        return f'N({self.number}, {x})'


    def __repr__(self):
        return str(self)


class Component(object):
    '''A component.'''
    def __init__(self, i, node1, node2):
        self.id = i
        self.node1 = node1
        self.node2 = node2


    def __str__(self):
        return f'Component({self.id}, {self.node1}, {self.node2})'


    def __repr__(self):
        return str(self)


    def __eq__(self, other):
        return self.id == other.id


    def contains(self, n):
        if self.node1.number == n:
            return True
        if self.node2.number == n:
            return True
        return False


    def empty_node_value(self):
        if self.node1.empty and self.node2.empty:
            raise EmptyNodesException()
        if self.node1.empty:
            return self.node1.number
        return self.node2.number


class Container(object):
    '''The container.'''

    def __init__(self, components):
        self.components = components


    def next_components(self, component):
        components = []
        value = component.empty_node_value()
        for c in self.components:
            if c.contains(value):
                components.append(c)
        return components


    def remove(self, component):
        return Container(tuple(c for c in components if c != component))


    def is_empty(self):
        return len(components) == 0


def parse_input(data):
    '''Parse the input.'''
    components = []
    for i, row in enumerate(data.strip().split('\n')):
        n1, n2 = tuple(map(int, row.strip().split('/')))
        component = Component(i, Node(n1, True), Node(n2, True))
        components.append(component)
    return components


def parse_input_new(data):
    components = []
    for row in data.strip().split('\n'):
        component = tuple(map(int, row.strip().split('/')))
        components.append(component)
    return components


components = parse_input_new(INPUT)

test_components = parse_input_new(TEST_INPUT)


if __name__ == '__main__':
    print('component count', len(components))
    print('unique count', len(set(components)))
