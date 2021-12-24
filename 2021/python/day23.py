#!python3
'''
Part 1
------

When testing part 1:
13127: too high [12521]

Part 2
------

46941: too low
47661: too low

When testing part 2:
42099: too low [44169]
'''

from collections import defaultdict
import heapq

'''
23233: too high
23053: too high

19493: not right answer
19299: not right answer
19099: not right answer
19071: not right answer
'''

NAMES = set('ABCD')
NAMES_LOWER = set('abcd')
MAX = 1_000_000_000

MOVE_COST = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

GOAL_COLUMNS = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9
}

PART2 = '''
#############
#...........#
###D#C#B#C###
  #D#C#B#A#
  #D#B#A#C#
  #D#A#A#B#
  #########'''.strip()

PART2_GOAL = '''
#############
#...........#
###a#b#c#d###
  #a#b#c#d#
  #a#b#c#d#
  #a#b#c#d#
  #########'''.strip()

PART1 = '''
#############
#...........#
###D#C#B#C###
  #D#A#A#B#
  #########'''.strip()

PART1_GOAL = '''
#############
#...........#
###a#b#c#d###
  #a#b#c#d#
  #########'''.strip()


TEST = '''
#############
#...........#
###B#C#B#D###
  #a#D#c#A#
  #########'''.strip()


TEST2 = '''
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #a#D#c#A#
  #########'''.strip()


def manhattan(l1, l2):
    r1, c1 = l1
    r2, c2 = l2
    return abs(r1 - r2) + abs(c1 - c2)


def node_locations(map_):
    '''Find the locations of upper case characters in map.'''
    for r, row in enumerate(map_.split('\n')):
        for c, element in enumerate(row):
            if element in NAMES:
                yield element, (r, c)


def make_goals(goal_map):
    '''Make goal locations for nodes based on goal map.'''
    goals = defaultdict(list)
    for r, row in enumerate(goal_map.split('\n')):
        for c, element in enumerate(row):
            if element in NAMES_LOWER:
                goals[element.upper()].append((r, c))
    return goals


def get_open_neighbours(location, map_):
    r, c = location
    map_list = map_.split('\n')
    locations = [
        (r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)
    ]
    for r_new, c_new in locations:
        a = map_list[r_new][c_new]
        if a == '.':
            yield r_new, c_new


MAP_DEPTH = 5
def update_map(map_, old_location, new_location, node):
    rows = map_.split('\n')
    layout = [[ch for ch in row] for row in rows]
    r_old, c_old = old_location
    r_new, c_new = new_location

    # Prune invalid map configurations, etc

    below = layout[r_new + 1][c_new]
    c_goal = GOAL_COLUMNS[node]

    if below == '.':
        return None
    if r_old == 1:
        if r_new == 1:
            # Once an amphipod stops moving in the hallway, it will stay in
            # that spot until it can move into a room.
            return None
        if r_new > 1:
            # Amphipods will never move from the hallway into a room unless
            # that room is their destination room and that room contains no
            # amphipods which do not also have that room as their own
            # destination.
            if c_new != c_goal:
                return None
            if below == '.' or below.isupper():
                return None

    if r_new == 1 and below.islower():
        return None

    if c_new != c_old:
        if r_new > 1:
            if c_new != c_goal:
                return None
        if below == '.' or below.isupper():
            return None
    else:
        if r_new < r_old:
            return None

    layout[r_new][c_new] = node.lower() if c_new != c_old and r_new > 1 else node
    layout[r_old][c_old] = '.'
    return '\n'.join(''.join(row) for row in layout)


def bfs(node, location, map_):
    '''A breadth first search of possible neighbouring maps for
    a node at location.'''
    seen = set()
    to_check = [(location, 0)]
    valid = []
    while to_check:
        check, d = to_check.pop(0)
        for new_location in get_open_neighbours(check, map_):
            if new_location not in seen:
                new_d = d + MOVE_COST[node]
                valid.append((new_location, new_d))
                to_check.append((new_location, new_d))
        seen.add(check)
    for new_location, d in valid:
        new_map = update_map(map_, location, new_location, node)
        if new_map:
            yield new_map, d


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return reversed(path)


def astar(start, goal, h):
    def get_neighbours(map_):
        '''Get all (cost, neighbour) pairs of map.'''
        for node, location in node_locations(map_):
            for new_map, d in bfs(node, location, map_):
                yield new_map, d

    goals = make_goals(goal)

    open_set = set([start])
    came_from = {}
    open_set_heap = []
    heapq.heappush(open_set_heap, (0, start))

    g_score = {start: 0}
    f_score = {start: h(start, goals)}

    i = 1
    while open_set:
        d, current = heapq.heappop(open_set_heap)
        open_set.remove(current)

        # if i % 10000 == 0:
        #     l = len(open_set)
        #     print(i, 'len open set', l, l / i)
        #     print('cost', d)
        #     print(current)
        #     print()
        # i += 1

        if current == goal:
            return g_score[current], reconstruct_path(came_from, current)

        for neighbour, d in get_neighbours(current):
            tentative_g_score = g_score.get(current, MAX) + d
            if tentative_g_score < g_score.get(neighbour, MAX):
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f = tentative_g_score + h(neighbour, goals)
                f_score[neighbour] = f
                if neighbour not in open_set:
                    open_set.add(neighbour)
                    heapq.heappush(open_set_heap, (f, neighbour))

    raise ValueError("Couldn't find path")


def heuristic(map_, goals):
    '''Cost of node to goal.'''
    i = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    cost = 0
    for node, location in node_locations(map_):
        node_i = i[node]
        i[node] += 1
        goal_location = goals[node][node_i]
        d = manhattan(location, goal_location)
        c = d * MOVE_COST[node]
        cost += c
    return cost


def part1():
    # cost, path = astar(TEST, PART1_GOAL, heuristic)
    cost, _ = astar(PART1, PART1_GOAL, heuristic)
    return cost


def part2():
    # cost, path = astar(TEST2, PART2_GOAL, heuristic)
    cost, _ = astar(PART2, PART2_GOAL, heuristic)
    return cost


def main():
    # test()
    # test1()
    p1 = part1()
    print(f'Part 1: {p1}')


    p2 = part2()
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()