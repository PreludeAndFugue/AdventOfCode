
import heapq
from itertools import combinations

'''
The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant.
'''


# elevator, HG, HM, LG, LM
# start = (1, 2, 1, 3, 1)
# goal = (4, 4, 4, 4, 4)

# elevator: thulium, plutonium, strontium, promethium, ruthenium
# generator, microchip pairs
# start = (1, 1, 1, 1, 2, 1, 2, 3, 3, 3, 3)
# goal = (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)

# part 2
start = (1, 1, 1, 1, 2, 1, 2, 3, 3, 3, 3, 1, 1, 1, 1)
goal = (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)


def is_valid_state_2(state):
    # for i in range(1, len(state), 2)
    if state[1] != state[2]:
        if state[2] == state[3]:
            return False
    if state[3] != state[4]:
        if state[4] == state[1]:
            return False
    return True


def is_valid_state_5(state):
    if state[1] != state[2]:
        for i in [3, 5, 7, 9]:
            if state[2] == state[i]:
                return False
    if state[3] != state[4]:
        for i in [1, 5, 7, 9]:
            if state[4] == state[i]:
                return False
    if state[5] != state[6]:
        for i in [1, 3, 7, 9]:
            if state[6] == state[i]:
                return False
    if state[7] != state[8]:
        for i in [1, 3, 5, 9]:
            if state[8] == state[i]:
                return False
    if state[9] != state[10]:
        for i in [1, 3, 5, 7]:
            if state[10] == state[i]:
                return False
    return True


def is_valid_state_7(state):
    if state[1] != state[2]:
        for i in [3, 5, 7, 9, 11, 13]:
            if state[2] == state[i]:
                return False
    if state[3] != state[4]:
        for i in [1, 5, 7, 9, 11, 13]:
            if state[4] == state[i]:
                return False
    if state[5] != state[6]:
        for i in [1, 3, 7, 9, 11, 13]:
            if state[6] == state[i]:
                return False
    if state[7] != state[8]:
        for i in [1, 3, 5, 9, 11, 13]:
            if state[8] == state[i]:
                return False
    if state[9] != state[10]:
        for i in [1, 3, 5, 7, 11, 13]:
            if state[10] == state[i]:
                return False
    if state[9] != state[10]:
        for i in [1, 3, 5, 7, 9, 13]:
            if state[12] == state[i]:
                return False
    if state[9] != state[10]:
        for i in [1, 3, 5, 7, 9, 11]:
            if state[14] == state[i]:
                return False
    return True


def goal_distance(state):
    return 4 * len(state) - sum(state)


def neighbours_of_state(state):
    elevator = state[0]
    keys = []
    for i, n in enumerate(state[1:], start=1):
        if state[i] == elevator:
            keys.append(i)

    can_move_down = any((n - elevator) < 0 for n in state)

    # Move 1
    for key in keys:
        if elevator < 4:
            # Move up
            new_state = list(state)
            new_state[0] += 1
            new_state[key] += 1
            new_state = tuple(new_state)
            if is_valid_state_7(new_state):
                yield new_state

        if elevator > 1 and can_move_down:
            # Move down
            new_state = list(state)
            new_state[0] -= 1
            new_state[key] -= 1
            new_state = tuple(new_state)
            if is_valid_state_7(new_state):
                yield new_state

    # Move 2 items
    if len(keys) > 1:
        for key1, key2 in combinations(keys, 2):
            if elevator < 4:
                # Move up
                new_state = list(state)
                new_state[0] += 1
                new_state[key1] += 1
                new_state[key2] += 1
                new_state = tuple(new_state)
                if is_valid_state_7(new_state):
                    yield new_state

            if elevator > 1 and can_move_down:
                # Move down
                new_state = list(state)
                new_state[0] -= 1
                new_state[key1] -= 1
                new_state[key2] -= 1
                new_state = tuple(new_state)
                if is_valid_state_7(new_state):
                    yield new_state


def print_state(state):
    rows = []
    for i in range(4, 0, -1):
        row = [f'F{i}']
        if state[0] == i:
            row.append('E')
        else:
            row.append('.')
        for s in state[1:]:
            if s == i:
                row.append('x')
            else:
                row.append('.')
        rows.append(' '.join(row))
    st = '\n'.join(rows)
    print(st)



def search():
    q = []
    heapq.heapify([])
    heapq.heappush(q, (0, start))
    seen = set()

    while q:
        c, state = heapq.heappop(q)

        # print(c, state)
        # print('q size', len(q))
        # print_state(state)
        # input()

        if state == goal:
            return c

        for n_state in neighbours_of_state(state):

            # print('\tneighbour')
            # print('\t', n_state)
            # print_state(n_state)
            if n_state in seen:
                continue

            seen.add(n_state)
            heapq.heappush(q, (c + 1, n_state))



def main():
    n = search()
    print(n)


if __name__ == '__main__':
    main()

