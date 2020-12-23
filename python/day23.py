#!python


INPUT = '792845136'
TEST_INPUT = '389125467'


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
    print('pick up:', values)
    return values


def get_insertion_value(current_value, removed_values):
    i = (current_value - 2) % 9
    while (i + 1) in removed_values:
        i  = (i - 1) % 9
    print('destination:', i + 1)
    return i + 1


def find_node_with_value(value, node):
    while node.value != value:
        node = node.right
    print('find node with value', value, node)
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


def move(current_node):
    removed = remove_after(current_node)
    removed_values = get_removed_values(removed)
    insertion_value = get_insertion_value(current_node.value, removed_values)
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


def _part1(node, n):
    for i in range(n):
        print(f'-- move {i + 1} --')
        move(node)
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


def main():
    test1()
    test2()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
