from help import get_input


TEST = '''1
2
-3
3
-2
0
4'''


class Node:
    def __init__(self, n, before, after):
        self.n = n
        self.before = before
        self.after = after


    def __repr__(self) -> str:
        return f'N({self.n}, b: {self.before.n}, a: {self.after.n})'


def parse(s):
    for line in s.split('\n'):
        yield int(line)


def make_ring(ns):
    start = Node(ns[0], None, None)
    nodes = [start]
    before = start
    for n in ns[1:-1]:
        node = Node(n, before, None)
        before.after = node
        before = node
        nodes.append(node)
    end = Node(ns[-1], before, start)
    before.after = end
    nodes.append(end)
    start.before = end
    return nodes


def move_node(n):
    '''
    Move node `n` d steps, where id is the value of the node. If d positive, move after,
    otherwise, move before.
    '''
    d = n.n
    if d == 0:
        return

    # this pair need to be joined together after moving n.
    before, after = n.before, n.after

    if d > 0:
        new_before = shift(n, d)
        new_after = new_before.after
        n.before = new_before
        n.after = new_after
        new_before.after = n
        new_after.before = n
    else:
        new_after = shift(n, d)
        new_before = new_after.before
        n.before = new_before
        n.after = new_after
        new_before.after = n
        new_after.before = n

    before.after = after
    after.before = before


def shift(n, d):
    '''
    Returns the node d positions from n. Positive, move after, otherwise, move before.'''
    if d == 0:
        return n
    result = None
    current = n
    for _ in range(abs(d)):
        if d < 0:
            result = current.before
        else:
            result = current.after
        current = result
    return result


def part1(ring):
    for node in ring:
        assert node.before is not None, 'before'
        assert node.after is not None, 'after'

    for node in ring:
        move_node(node)

    zero = None
    for node in ring:
        if node.n == 0:
            zero = node
            break

    x1 = shift(zero, 1000)
    x2 = shift(x1, 1000)
    x3 = shift(x2, 1000)

    return sum([x1.n, x2.n, x3.n])


def main():
    s = get_input('20')
    # s = TEST.strip()
    ns = list(parse(s))
    ring = make_ring(ns)

    p1 = part1(ring)

    print('Part 1:', p1)


def test():
    # s = get_input('20')
    s = TEST.strip()
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
