#!python3

'''
depth: 9171
target: 7,721
'''

DEPTH = 9_171
MODULO = 20_183
X = 7
Y = 721

TEST_DEPTH = 510
TEST_X = 10
TEST_Y = 10


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
        total = 0
        for i in range(x + 1):
            for j in range(y + 1):
                total += self.get_erosion_level(i, j) % 3
        return total


def test1():
    map = Map(TEST_DEPTH, TEST_X, TEST_Y)
    r = map.risk_level(TEST_X, TEST_Y)
    assert r == 114


def part1():
    map = Map(DEPTH, X, Y)
    return map.risk_level(X, Y)


def main():
    test1()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
