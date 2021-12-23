#!python3
'''
Part 1
------

When testing part 1:
13127: too high [12521]

Part 2
------

46941: too low

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

# Nodes cannot stop on these open positions
INVALID_POSITIONS = set([
    (1, 3), (1, 5), (1, 7), (1, 9)
])

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
  #A#D#C#A#
  #########'''.strip()


TEST2 = '''
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
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

    # print(r_new, MAP_DEPTH)

    below = layout[r_new + 1][c_new]
    c_goal = GOAL_COLUMNS[node]

    if below == '.':
        return None
    if r_old == 1:
        if r_new > 1:
            if c_new != c_goal:
                return None
            if below == '.' or below.isupper():
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


    # if r_old > 1 and r_new < r_old:
    #     if below == '.':
    #         return None

    # If moving to the bottom layer, then this node shouldn't move
    # back out
    layout[r_new][c_new] = node.lower() if c_new != c_old and r_new > 1 else node

    # if r_new == MAP_DEPTH - 1:
    #     below = layout[MAP_DEPTH][c_new]
    #     if below.isupper():
    #         return None

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
        # if new_location in INVALID_POSITIONS:
        #     continue
        new_map = update_map(map_, location, new_location, node)
        if new_map:
            yield new_map, d


def astar(start, goal, h):
    def get_neighbours(map_):
        '''Get all (cost, neighbour) pairs of map.'''
        for node, location in node_locations(map_):
            for new_map, d in bfs(node, location, map_):
                yield new_map, d

    goals = make_goals(goal)

    open_set = set([start])
    open_set_heap = []
    heapq.heappush(open_set_heap, (0, start))

    g_score = {start: 0}
    f_score = {start: h(start, goals)}

    i = 1
    while open_set:
        # current = get_cheapest()
        d, current = heapq.heappop(open_set_heap)
        open_set.remove(current)

        if i % 10000 == 0:
            l = len(open_set)
            print(i, 'len open set', l, l / i)
            print('cost', d)
            print(current)
            print()
            # input()
        i += 1
        # print(len(open_set))
        # input()

        if current == goal:
            print(current)
            return g_score[current]

        # open_set.remove(current)

        for neighbour, d in get_neighbours(current):
            # print(neighbour, d)
            # input()
            tentative_g_score = g_score.get(current, MAX) + d
            if tentative_g_score < g_score.get(neighbour, MAX):
                g_score[neighbour] = tentative_g_score
                f = tentative_g_score + h(neighbour, goals)
                f_score[neighbour] = f
                if neighbour not in open_set:
                    open_set.add(neighbour)
                    heapq.heappush(open_set_heap, (f, neighbour))
            #         print('adding to open set')
            # input()

    raise ValueError("Couldn't find path")


def heuristic(map_, goals):
    '''Cost of node to goal.'''
    i = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    cost = 0
    for node, location in node_locations(map_):
        # print(node, location)
        node_i = i[node]
        i[node] += 1
        goal_location = goals[node][node_i]
        # print('\t', goal_location)
        d = manhattan(location, goal_location)
        # print('\t', d)
        c = d * MOVE_COST[node]
        cost += c
        # print('\t', c)
    return cost


def test():
    map_ = '''
#############
#...........#
###.#A#.#.###
  #.#A#.#.#
  #########'''.strip()
    for new_map, d in bfs('A', (2, 5), map_):
        print(new_map)
        print(d)
        print()


def part1():
    cost = astar(TEST, PART1_GOAL, heuristic)
    # cost = astar(PART1, PART1_GOAL, heuristic)
    print(cost)


def part2():
    cost = astar(TEST2, PART2_GOAL, heuristic)
    # cost = astar(PART2, PART2_GOAL, heuristic)
    print(cost)


def main():
    # test()
    # test1()
    part1()
    # part2()


if __name__ == '__main__':
    main()