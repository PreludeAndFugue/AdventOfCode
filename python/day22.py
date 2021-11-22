#!python3

from collections import deque

INPUT = 'day22.txt'

TEST_INPUT_1 = '''Player 1:
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

TEST_INPUT_2 = '''Player 1:
43
19

Player 2:
2
29
14
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


def score(p):
    p.reverse()
    total = 0
    for i, n in enumerate(p, start=1):
        total += i * n
    return total


def game1(p1, p2):
    while p1 and p2:
        move(p1, p2)
    s = score(p1) + score(p2)
    return s


def game_state(p1, p2):
    return '|'.join([str(p1), str(p2)])


GAME_NO = 1

def game2(n, p1, p2):
    global GAME_NO
    # print(f'\n=== Game {n} ===\n')
    round = 1
    previous_states = set()

    while p1 and p2:

        # input()

        # print(f'--Round {round} (Game {n})--')
        current_state = game_state(p1, p2)
        if current_state in previous_states:
            # print('Repetition - player 1 wins')
            return 1
        else:
            previous_states.add(current_state)

        n1 = p1.popleft()
        n2 = p2.popleft()

        # print(n1, p1, n2, p2)

        if len(p1) >= n1 and len(p2) >= n2:
            # Recurse
            p1_copy = deque(list(p1.copy())[:n1])
            p2_copy = deque(list(p2.copy())[:n2])

            GAME_NO = GAME_NO + 1
            result = game2(GAME_NO, p1_copy, p2_copy)

            # print(f'...anyway back to game {n}')

            if result == 1:
                # print(f'Player 1 wins round {round} of game {n}')
                p1.append(n1)
                p1.append(n2)
            else:
                # print(f'Player 2 wins round {round} of game {n}')
                p2.append(n2)
                p2.append(n1)

        else:
            if n1 > n2:
                # print(f'Player 1 wins round {round} of game {n}')
                p1.append(n1)
                p1.append(n2)
            else:
                # print(f'Player 2 wins round {round} of game {n}')
                p2.append(n2)
                p2.append(n1)

        round += 1

    # Someone has an empty deck

    if p1:
        # print(f'The winner of game {n} is player 1')
        return 1
    else:
        # print(f'The winner of game {n} is player 2')
        return 2


def test1(p1, p2):
    p1 = deque(p1)
    p2 = deque(p2)
    g = game1(p1, p2)
    assert g == 306


def part1(p1, p2):
    p1 = deque(p1)
    p2 = deque(p2)
    g = game1(p1, p2)
    return g


def test2(p1, p2):
    GAME_NO = 1
    p1 = deque(p1)
    p2 = deque(p2)
    game2(GAME_NO, p1, p2)
    s2 = score(p2)
    assert s2 == 291


def part2(p1, p2):
    GAME_NO = 1
    p1 = deque(p1)
    p2 = deque(p2)
    game2(GAME_NO, p1, p2)
    s1 = score(p1)
    s2 = score(p2)
    return s1 + s2


def main():
    p1_test, p2_test = get_input(TEST_INPUT_1)
    p1, p2 = get_input(open(INPUT, 'r').read())

    test1(p1_test, p2_test)

    p = part1(p1, p2)
    print(p)

    test2(p1_test, p2_test)

    p = part2(p1, p2)
    print(p)


if __name__ == "__main__":
    main()
