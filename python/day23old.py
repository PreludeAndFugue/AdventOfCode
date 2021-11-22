#!python3

'''
Trying a deque.
'''

from collections import deque

INPUT = '792845136'
TEST_INPUT = '389125467'


def create_deque(input):
    q = deque(map(int, list(input)))
    return q


def create_deque2(input):
    q = create_deque(input)
    other_values = range(10, 1_000_001)
    q.extend(other_values)
    return q


def insert_label(n, others, size):
    i = (n - 2) % size
    while (i + 1) in others:
        i = (i - 1) % size
    return i + 1


def rotate_to_n(q, n):
    print('rotate to', n)
    i = 0
    while q[-1] != n:
        i -= 1
        q.rotate(-1)
    print('rotated q', q)
    return i


def move(q, size):
    n = q[0]
    q.rotate(-1)
    removed = []
    for _ in range(3):
        removed.append(q.popleft())
    m = insert_label(n, removed, size)
    # m_i = q.index(m)

    i = rotate_to_n(q, m)
    q.extend(removed)
    q.rotate(i - 4)

    # print('insert label', m)
    # print('index m', m_i)
    # q.rotate(-m_i - 1)
    # print(q)
    # q.extend(removed)
    # print(q)
    # q.rotate(m_i + 4)


def test1():
    q = create_deque(TEST_INPUT)
    size = len(q)
    for _ in range(10):
        print(q)
        move(q, size)

    i1 = q.index(1)
    q.rotate(-i1)
    q.popleft()
    x = ''.join(map(str, q))

    assert x == '92658374'


def test2():
    q = create_deque(TEST_INPUT)
    size = len(q)
    for _ in range(100):
        move(q, size)

    i1 = q.index(1)
    q.rotate(-i1)
    q.popleft()
    x = ''.join(map(str, q))

    assert x == '67384529'


def part1():
    q = create_deque(INPUT)
    size = len(q)
    for _ in range(100):
        move(q, size)

    i1 = q.index(1)
    q.rotate(-i1)
    q.popleft()
    x = ''.join(map(str, q))
    return x


def part2():
    q = create_deque2(INPUT)
    size = len(q)
    for _ in range(10_000):
        move(q, size)


def main():
    test1()
    test2()

    p = part1()
    print(p)

    part2()
    print(p)


if __name__ == "__main__":
    main()
