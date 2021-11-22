#!python3

'''
depth: 9171
target: 7,721

Use Djikstra's algorithm for part 2
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Practical_optimizations_and_infinite_graphs

'''

DEPTH = 9_171
MODULO = 20_183
X = 7
Y = 721

TEST_DEPTH = 510
TEST_X = 10
TEST_Y = 10

# equipment
CLIMBING_GEAR = 'climbing_gear'
TORCH = 'torch'
NEITHER = 'neither'


class Map(object):
    def __init__(self, depth, target_x, target_y):
        self.depth = depth
        self.target_x = target_x
        self.target_y = target_y
        self.geologic_indexes = {}


    def get_geologic_index(self, x, y):
        if (x, y) in self.geologic_indexes:
            return self.geologic_indexes[(x, y)]
        if x == 0 and y == 0:
            self.geologic_indexes[(x, y)] = 0
            return 0
        if x == self.target_x and y == self.target_y:
            self.geologic_indexes[(x, y)] = 0
            return 0
        if y == 0:
            g_i = 16807 * x
            self.geologic_indexes[(x, y)] = g_i
            return g_i
        if x == 0:
            g_i = 48271 * y
            self.geologic_indexes[(x, y)] = g_i
            return g_i
        g_i = self.get_erosion_level(x - 1, y) * self.get_erosion_level(x, y - 1)
        self.geologic_indexes[(x, y)] = g_i
        return g_i


    def get_erosion_level(self, x, y):
        g_i = self.get_geologic_index(x, y)
        return (g_i + self.depth) % MODULO


    def risk_level(self, x, y):
        return self.get_erosion_level(x, y) % 3


    def total_risk_level(self, x, y):
        total = 0
        for i in range(x + 1):
            for j in range(y + 1):
                total += self.risk_level(i, j)
        return total


class Node(object):
    def __init__(self, x, y, risk_level, equipment, time):
        self.x = x
        self.y = y
        self.risk_level = risk_level
        self.equipment = equipment
        self.time = time


class UniformCostSearch(object):
    risk_level_equipment = {
        0: [CLIMBING_GEAR, TORCH],
        1: [CLIMBING_GEAR, NEITHER],
        2: [TORCH, NEITHER]
    }

    def __init__(self, start, goal, map):
        '''
        start: a node
        goal: a location (x, y)
        nodes: dictionary of Nodes where the keys are tuples - (x, y, equipment).
        '''
        self.start = start
        self.goal = goal
        self.nodes = {}
        self.map = map


    def _get_neighbours(self, node):
        pass


    def _get_equipment(self, risk_level):
        return UniformCostSearch.risk_level_equipment[risk_level]


def test1():
    map = Map(TEST_DEPTH, TEST_X, TEST_Y)
    r = map.total_risk_level(TEST_X, TEST_Y)
    assert r == 114


def part1():
    map = Map(DEPTH, X, Y)
    return map.total_risk_level(X, Y)


def test2():
    map = Map(TEST_DEPTH, TEST_X, TEST_Y)
    start = Node(0, 0, 0, TORCH, 0)
    goal = (TEST_X, TEST_Y)
    search = UniformCostSearch(start, goal, map)


def main():
    test1()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
