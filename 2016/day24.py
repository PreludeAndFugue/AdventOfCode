#!python3

from itertools import combinations, permutations
from queue import Queue


INPUT = 'day24.txt'
TEST_INPUT = '''###########
#0.1.....2#
#.#######.#
#4.......3#
###########'''


def create_maze(input):
    maze = {}
    for i, row in enumerate(input.strip().split('\n')):
        for j, e in enumerate(row):
            maze[(j, i)] = e
    return maze


def print_maze(maze):
    keys = list(maze.keys())
    max_x = max(k[0] for k in keys)
    max_y = max(k[1] for k in keys)
    result = []
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            row.append(maze[(x, y)])
        result.append(''.join(row))
    print('\n'.join(result))


def get_locations(maze):
    locations = []
    for v in maze.values():
        if v.isdecimal():
            locations.append(int(v))
    return sorted(locations)


def get_neighbours(maze, x, y):
    neighbours = []
    for dx in [-1, 1]:
        k = (x + dx, y)
        m = maze.get(k, '#')
        if m != '#':
            neighbours.append(k)
    for dy in [-1, 1]:
        k = (x, y + dy)
        m = maze.get(k, '#')
        if m != '#':
            neighbours.append(k)
    return neighbours



def shortest_path(maze, m, n):
    '''The shortest path between numbers m and n.'''
    start = [k for k, v in maze.items() if v == str(m)][0]
    goal = [k for k, v in maze.items() if v == str(n)][0]
    q = Queue()
    seen = set()
    q.put((start, 0))
    while not q.empty():
        k, d = q.get()
        if k == goal:
            return d
        if k in seen:
            continue
        seen.add(k)
        for n in get_neighbours(maze, *k):
            q.put((n, d + 1))


def all_shortest_paths(maze, numbers):
    paths = {}
    for m, n in combinations(numbers, 2):
        s = shortest_path(maze, m, n)
        paths[(m, n)] = s
        paths[(n, m)] = s
    return paths


def get_path_length(nodes, paths):
    n1 = 0
    d = 0
    for n2 in nodes:
        d += paths[(n1, n2)]
        n1 = n2
    return d


def shortest_total_path(other_locations, paths):
    lengths = []
    for p in permutations(other_locations):
        l = get_path_length(p, paths)
        lengths.append(l)
    return min(lengths)


def shortest_total_path_back_home(other_locations, paths):
    lengths = []
    for p in permutations(other_locations):
        last = p[-1]
        l = get_path_length(p, paths) + paths[(last, 0)]
        lengths.append(l)
    return min(lengths)


def part1(maze):
    locations = get_locations(maze)
    other_locations = [l for l in locations if l != 0]
    paths = all_shortest_paths(maze, locations)
    return shortest_total_path(other_locations, paths)


def part2(maze):
    locations = get_locations(maze)
    other_locations = [l for l in locations if l != 0]
    paths = all_shortest_paths(maze, locations)
    return shortest_total_path_back_home(other_locations, paths)



def main():
    maze = create_maze(open(INPUT, 'r').read())
    p = part1(maze)
    print(p)

    p = part2(maze)
    print(p)


if __name__ == '__main__':
    main()
