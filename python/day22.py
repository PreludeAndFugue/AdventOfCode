#!python3

from collections import deque

INPUT = 'day22.txt'

TEST_INPUT = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
'''

def get_input(input):
    p1, p2 = input.strip().split('\n\n')
    p1 = list(map(int, p1.strip().split('\n')[1:]))
    p2 = list(map(int, p2.strip().split('\n')[1:]))
    return p1, p2


def move(p1, p2):
    n1 = p1.popleft()
    n2 = p2.popleft()
    if n1 > n2:
        p1.append(n1)
        p1.append(n2)
    elif n1 < n2:
        p2.append(n2)
        p2.append(n1)
    else:
        raise Exception('Same values')


def get_winner(p1, p2):
    if p1 and p2:
        raise Exception
    if p1:
        return p1
    elif p2:
        return p2
    else:
        raise Exception


def score(p):
    p.reverse()
    total = 0
    for i, n in enumerate(p, start=1):
        total += i * n
    return total


def game(p1, p2):
    while p1 and p2:
        move(p1, p2)
    w = get_winner(p1, p2)
    s = score(w)
    return s


def test1():
    p1, p2 = get_input(TEST_INPUT)
    p1 = deque(p1)
    p2 = deque(p2)
    g = game(p1, p2)
    assert g == 306


def part1():
    p1, p2 = get_input(open(INPUT, 'r').read())
    p1 = deque(p1)
    p2 = deque(p2)
    g = game(p1, p2)
    return g


def main():
    test1()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
