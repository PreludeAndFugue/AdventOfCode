#!python3

'''Data for day 22.'''

from enum import Enum


INPUT = '''...##.#.#.####...###.....
..#..##.#...#.##.##.#..#.
.#.#.#.###....#...###....
.#....#..####.....##.#..#
##.#.#.#.#..#..#.....###.
#...##....##.##.#.##.##..
.....###..###.###...#####
######.####..#.#......##.
#..###.####..####........
#..######.##....####...##
...#.##.#...#.#.#.#..##.#
####.###..#####.....####.
#.#.#....#.####...####...
##...#..##.##....#...#...
......##..##..#..#..####.
.##..##.##..####..##....#
.#..#..##.#..##..#...#...
#.#.##.....##..##.#####..
##.#.......#....#..###.#.
##...#...#....###..#.#.#.
#....##...#.#.#.##..#..##
#..#....#####.....#.##.#.
.#...#..#..###....###..#.
..##.###.#.#.....###.....
#.#.#.#.#.##.##...##.##.#'''


TEST_INPUT = '''..#
#..
...'''

class NodeState(Enum):
    CLEAN = 1
    WEAKENED = 2
    INFECTED = 3
    FLAGGED = 4

    def new_state(self):
        if self == NodeState.CLEAN:
            return NodeState.WEAKENED
        if self == NodeState.WEAKENED:
            return NodeState.INFECTED
        if self == NodeState.INFECTED:
            return NodeState.FLAGGED
        if self == NodeState.FLAGGED:
            return NodeState.CLEAN


def middle(n):
    if n % 2:
        return int((n - 1)/2)
    else:
        return int(n/2)


def find_centre(grid):
    rows = grid.strip().split('\n')
    col_count = len(rows[0])
    row_count = len(rows)
    return middle(row_count), middle(col_count)


def grid_to_dict(grid):
    grid_dict = dict()
    for i, row in enumerate(grid.strip().split('\n')):
        for j, col in enumerate(list(row)):
            if col == '#':
                grid_dict[(j, i)] = NodeState.INFECTED
    return grid_dict


grid = grid_to_dict(INPUT)
virus_position = find_centre(INPUT)

test_grid = grid_to_dict(TEST_INPUT)
test_virus_position = find_centre(TEST_INPUT)


class Model(object):

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    RIGHT_TURN = {
        UP: RIGHT,
        RIGHT: DOWN,
        DOWN: LEFT,
        LEFT: UP
    }

    LEFT_TURN = {
        UP: LEFT,
        LEFT: DOWN,
        DOWN: RIGHT,
        RIGHT: UP
    }

    REVERSE = {
        UP: DOWN,
        LEFT: RIGHT,
        RIGHT: LEFT,
        DOWN: UP
    }


    def __init__(self, grid, virus_position):
        self.grid = grid
        self.virus_position = virus_position
        self.virus_direction = Model.UP
        self.infect_count = 0


    def run(self, n):
        for _ in range(n):
            self._update_direction()
            self._update_node()
            self._move()


    def _update_direction(self):
        node = self.grid.get(self.virus_position, NodeState.CLEAN)
        if node == NodeState.CLEAN:
            self.virus_direction = Model.LEFT_TURN[self.virus_direction]
        if node == NodeState.WEAKENED:
            pass
        if node == NodeState.INFECTED:
            self.virus_direction = Model.RIGHT_TURN[self.virus_direction]
        if node == NodeState.FLAGGED:
            self.virus_direction = Model.REVERSE[self.virus_direction]


    def _update_node(self):
        node_state = self.grid.get(self.virus_position, NodeState.CLEAN)
        new_state = node_state.new_state()
        self.grid[self.virus_position] = new_state
        if new_state == NodeState.INFECTED:
            # print('current node clean, infecting', self.virus_position)
            self.infect_count += 1
        else:
            # print('current node infected, cleaning', self.virus_position)
            pass


    def _move(self):
        self.virus_position = self.virus_position[0] + self.virus_direction[0], self.virus_position[1] + self.virus_direction[1]
