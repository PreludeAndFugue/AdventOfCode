#!python


INPUT = '792845136'
TEST_INPUT = '389125467'

EXTEND = 1_000_000
MOVES = 10_000_000

EXTEND_TEST = 1_000_000
MOVES_TEST = 100


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def __repr__(self):
        l = self.left.value if self.left is not None else '?'
        r = self.right.value if self.right is not None else '?'
        return f'Node({self.value}, l: {l}, r: {r})'


def get_input(input):
    nodes = list(map(Node, (map(int, list(input.strip())))))
    nodes1 = nodes[1:] + [nodes[0]]
    for n1, n2 in zip(nodes, nodes1):
        n1.right = n2
        n2.left = n1
    return nodes[0]


def extend_input_nodes(node, max_value):
    '''Create all nodes for part 2.'''
    last_node = node.left
    last_node.right = None
    node.left = None
    previous_node = last_node
    for i in range(10, max_value + 1):
        new_node = Node(i)

        previous_node.right = new_node
        new_node.left = previous_node

        previous_node = new_node

    previous_node.right = node
    node.left = previous_node


def remove_after(node):
    removed = node.right
    removed_end = removed.right.right
    new_right = removed_end.right
    node.right = new_right
    new_right.left = node
    removed.left = None
    removed_end.right = None
    return removed


def get_removed_values(node):
    values = []
    while node is not None:
        values.append(node.value)
        node = node.right
    # print('pick up:', values)
    return values


def get_insertion_value(current_value, removed_values, n):
    i = (current_value - 2) % n
    while (i + 1) in removed_values:
        i  = (i - 1) % n
    # print('destination:', i + 1)
    return i + 1


def find_node_with_value(value, node):
    while node.value != value:
        node = node.right
    # print('find node with value', value, node)
    return node


def insert_after(node, new_right):
    old_right = node.right

    node.right = new_right
    new_right.left = node

    new_right_end = new_right.right.right
    new_right_end.right = old_right
    old_right.left = new_right_end


def print_nodes(node):
    values = []
    while node.value not in values:
        values.append(node.value)
        node = node.right
    print(values)
    print()


def move(current_node, n):
    removed = remove_after(current_node)
    removed_values = get_removed_values(removed)
    insertion_value = get_insertion_value(current_node.value, removed_values, n)
    insertion_node = find_node_with_value(insertion_value, current_node)
    insert_after(insertion_node, removed)


def answer(node):
    n1 = find_node_with_value(1, node)
    n = n1.right
    values = []
    while n.value != 1:
        values.append(n.value)
        n = n.right
    return ''.join(str(i) for i in values)


def print_window_around(node):
    print(node)
    start = node.left.left.left.left.left
    values = []
    for _ in range(11):
        values.append(start.value)
        start = start.right
    print(values)


def _part1(node, n):
    for _ in range(n):
        # print(f'-- move {i + 1} --')
        move(node, 9)
        print_nodes(node)
        node = node.right
    return answer(node)


def test1():
    current_node = get_input(TEST_INPUT)
    x = _part1(current_node, 10)
    assert x == '92658374'


def test2():
    current_node = get_input(TEST_INPUT)
    x = _part1(current_node, 100)
    assert x == '67384529'


def part1():
    current_node = get_input(INPUT)
    x = _part1(current_node, 100)
    return x


def test3():
    node = get_input(TEST_INPUT)
    extend_input_nodes(node, EXTEND_TEST)

    first_value = node.value
    values = [first_value]
    node = node.right
    while node.value != first_value:
        values.append(node.value)
        node = node.right
    assert len(values) == EXTEND_TEST
    assert min(values) == 1
    assert max(values) == EXTEND_TEST
    assert len(set(values)) == EXTEND_TEST


def _part2(node, moves, max_value):
    for _ in range(moves):
        # print(f'-- move {i + 1} --')
        move(node, max_value)
        node = node.right
        # print_window_around(node)
    # print(node)
    # print(node.right)
    # print(node.right.right)


def test4():
    node = get_input(TEST_INPUT)
    extend_input_nodes(node, EXTEND_TEST)
    _part2(node, MOVES_TEST, EXTEND_TEST)


def main():
    # test1()
    # test2()

    # p = part1()
    # print(p)

    # test3()
    test4()


if __name__ == "__main__":
    # main()
    import timeit
    x = timeit.timeit('main()', setup='from __main__ import main', number=1)
    print(x)