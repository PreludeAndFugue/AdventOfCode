#!python3

from collections import defaultdict
import heapq
from itertools import combinations

from helpers import BASE

TEST01 = '''#########
#b.A.@.a#
#########'''

TEST02 = '''########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################'''

TEST03 = '''########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################'''

TEST04 = '''#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################'''

TEST05 = '''########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################'''


class State(object):
    def __init__(self, current_key, previous_keys):
        self.current_key = current_key
        self.previous_keys = previous_keys

    def __eq__(self, other):
        return self.current_key == other.current_key and self.previous_keys == other.previous_keys

    def __hash__(self):
        return hash((self.current_key, self.previous_keys))

    def all_keys(self):
        return self.previous_keys.union(self.current_key)

    def __repr__(self):
        previous = ''.join(sorted(self.previous_keys))
        return f'State({self.current_key}, {previous})'


def parse(string):
    map_ = {}
    keys = {}
    for y, line in enumerate(string.strip().split('\n')):
        for x, ch in enumerate(line):
            if ch == '#':
                continue
            elif ch == '.':
                map_[x, y] = ch
            elif ch.islower():
                keys[ch] = x, y
                map_[x, y] = ch
            elif ch == '@':
                keys[ch] = x, y
                map_[x, y] = ch
            elif ch.isupper():
                map_[x, y] = ch
            else:
                raise ValueError
    return map_, keys


def get_neighbours(x, y, map_):
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x_new = x + dx
        y_new = y + dy
        if (x_new, y_new) in map_:
            yield (x_new, y_new), map_[x_new, y_new]


def bfs(map_, start, goal):
    seen = set()
    to_check = [(start,)]
    while to_check:
        path = to_check.pop(0)
        location = path[-1]
        if location == goal:
            return path
        if location not in seen:
            for n_location, n in get_neighbours(*location, map_):
                new_path = path + (n_location,)
                to_check.append(new_path)
            seen.add(location)


def get_doors(map_, path):
    doors = set()
    for p in path:
        d = map_[p]
        if d.isupper():
            doors.add(d.lower())
    return doors


def make_new_map(map_, keys):
    new_map = defaultdict(list)
    for k1, k2 in combinations(keys.keys(), 2):
        start = keys[k1]
        goal = keys[k2]
        path = bfs(map_, start, goal)
        doors = get_doors(map_, path)
        new_map[k1].append((k2, len(path) - 1, doors))
        new_map[k2].append((k1, len(path) - 1, doors))
    return new_map


def get_neighbours2(state, map_):
    # print('get neighbours 2:', state)
    key = state.current_key
    keys = state.previous_keys
    keys = keys.union(set([key]))
    for next_key, d, blocking_keys in map_[key]:
        # print('\t\t', next_key, d, blocking_keys)
        if next_key in keys:
            continue
        remaining_keys = blocking_keys - keys
        if not remaining_keys:
            new_state = State(next_key, state.all_keys())
            # print('\t\tgetting', new_state, d)
            yield new_state, d


def dijkstra(map_, keys, start_key):
    '''
    Item: (cost, distance, key, all_keys)
    Start: (0, 0, '@', set())

    cost = distance - len(all_keys)

    '''
    all_keys = set(keys.keys())
    start_state = State('@', frozenset())
    cost_state = defaultdict(set)
    cost_state[0].add(start_state)
    state_cost = {start_state: 0}
    seen = set()
    queue = [0]


    print('initial cost state', cost_state)


    while queue:
        cost = heapq.heappop(queue)
        state = cost_state[cost].pop()
        # print('pop from queue')
        # print(cost, ':', state)
        # input()

        if state.all_keys() == all_keys:
            return cost

        if state in seen:
            # print('already seen', state)
            continue

        for next_state, next_cost in get_neighbours2(state, map_):
            # print('\t', 'next state', next_state, next_cost)
            # input()

            total_cost = cost + next_cost
            if next_state in state_cost:
                test_cost = state_cost[next_state]
                if test_cost >= total_cost:
                    continue
                else:
                    cost_state[total_cost].add(next_state)
                    state_cost[next_state] = total_cost
                    heapq.heappush(queue, total_cost)
            else:
                cost_state[total_cost].add(next_state)
                state_cost[next_state] = total_cost
                heapq.heappush(queue, total_cost)

        # print('cost state', cost_state)
        # print('state cost', state_cost)
        # print('queue', queue)
        # print()
        # input()

        # print(queue)



def test1():
    map_, keys = parse(TEST04)

    new_map = make_new_map(map_, keys)
    print(new_map)


    d = dijkstra(new_map, keys, '@')
    print(d)


def main():
    # test1()

    map_, keys = parse(open(BASE + 'day18.txt', 'r').read())
    print(map_)
    print(keys)
    new_map = make_new_map(map_, keys)
    print(new_map)
    d = dijkstra(new_map, keys, '@')
    print(d)


if __name__ == '__main__':
    main()
