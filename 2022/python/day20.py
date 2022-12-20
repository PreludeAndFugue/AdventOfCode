from help import get_input


TEST = '''1
2
-3
3
-2
0
4'''


class Node:
    def __init__(self, n, before, after, size):
        self.n = n
        self.before = before
        self.after = after
        self.move = n % (size - 1)


    def __repr__(self) -> str:
        return f'N({self.n}, b: {self.before.n}, a: {self.after.n}, m: {self.move})'


def parse(s):
    for line in s.split('\n'):
        yield int(line)


def make_ring(ns):
    size = len(ns)
    start = Node(ns[0], None, None, size)
    nodes = [start]
    before = start
    for n in ns[1:-1]:
        node = Node(n, before, None, size)
        before.after = node
        before = node
        nodes.append(node)
    end = Node(ns[-1], before, start, size)
    before.after = end
    nodes.append(end)
    start.before = end
    return nodes


def move_node(n):
    '''
    Move node `n` d steps, where id is the value of the node. If d positive, move after,
    otherwise, move before.
    '''
    d = n.move
    assert d >= 0
    if d == 0:
        return

    # this pair need to be joined together after moving n.
    before, after = n.before, n.after
    before.after = after
    after.before = before

    new_before = shift(n, d)
    new_after = new_before.after
    n.before = new_before
    n.after = new_after
    new_before.after = n
    new_after.before = n


def shift(n, d):
    '''
    Returns the node d positions from n.'''
    assert d >= 0
    if d == 0:
        return n
    result = None
    current = n
    for _ in range(d):
        result = current.after
        current = result
    return result


def get_zero(ring):
    for node in ring:
        if node.n == 0:
            return node
    raise ValueError


def calculate_sum(ring):
    zero = get_zero(ring)

    x1 = shift(zero, 1000)
    x2 = shift(x1, 1000)
    x3 = shift(x2, 1000)

    return sum([x1.n, x2.n, x3.n])


def print_ring_from_zero(ring):
    node = get_zero(ring)
    ns = []
    for _ in range(len(ring)):
        ns.append(node.n)
        node = node.after
    print(ns)


def part1(ring):
    for node in ring:
        assert node.before is not None, 'before'
        assert node.after is not None, 'after'

    for node in ring:
        move_node(node)

    return calculate_sum(ring)


def part2(ring):
    for _ in range(10):
        for n in ring:
            move_node(n)

    return calculate_sum(ring)



def main():
    s = get_input('20')
    # s = TEST.strip()
    ns = list(parse(s))

    ring1 = make_ring(ns)
    p1 = part1(ring1)

    N = 811_589_153
    ns2 = [N*n for n in ns]
    ring2 = make_ring(ns2)
    p2 = part2(ring2)

    print('Part 1:', p1)
    print('Part 2:', p2)


def test():
    s = get_input('20')
    # s = TEST.strip()
    ns = list(parse(s))
    r = make_ring(ns)
    print(r)
    n = r[0]
    print(n)
    n = shift(n, -8)
    print(n)


if __name__ == '__main__':
    main()
    # test()
