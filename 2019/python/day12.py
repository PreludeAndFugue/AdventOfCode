#!python3

'''
The x positions and velocities are independent of the y and z values.

For part 2, find the periods of the x, y, and z parameters
indepentently. Will then be able to work out the period

Input

<x=5, y=13, z=-3>
<x=18, y=-7, z=13>
<x=16, y=3, z=4>
<x=0, y=8, z=8>
'''

from itertools import combinations

from maths import lcm

COORDS = ['x', 'y', 'z']

TEST01 = [
    (-1, 0, 2),
    (2, -10, -7),
    (4, -8, 8),
    (3, 5, -1)
]


TEST02 = [
    (-8, -10, 0),
    (5, 5, 10),
    (2, -7, 3),
    (9, -8, -3)
]


INPUT = [
    (5, 13, -3),
    (18, -7, 13),
    (16, 3, 4),
    (0, 8, 8),
]


class MoonCoord(object):
    def __init__(self, c1, c2, c3, c4):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.v1 = 0
        self.v2 = 0
        self.v3 = 0
        self.v4 = 0


    def time_step(self):
        self._apply_gravity()
        self._apply_velocity()


    def potential_energy(self, index):
        return abs(self.__dict__[f'c{index}'])


    def kinetic_energy(self, index):
        return abs(self.__dict__[f'v{index}'])


    def state(self):
        return (self.c1, self.c2, self.c3, self.c4, self.v1, self.v2, self.v3, self.v4)


    def _apply_gravity(self):
        for x, y in self._combinations():
            c1 = self.__dict__[x[0]]
            c2 = self.__dict__[y[0]]
            d1, d2 = self._diffs(c1, c2)
            self.__dict__[x[1]] += d1
            self.__dict__[y[1]] += d2


    def _apply_velocity(self):
        self.c1 += self.v1
        self.c2 += self.v2
        self.c3 += self.v3
        self.c4 += self.v4


    def _combinations(self):
        items = [('c1', 'v1'), ('c2', 'v2'), ('c3', 'v3'), ('c4', 'v4')]
        for x, y in combinations(items, 2):
            yield x, y


    def _diffs(self, c1, c2):
        if c1 < c2:
            return 1, -1
        elif c1 == c2:
            return 0, 0
        else:
            return -1, 1


    def __repr__(self):
        return f'({self.c1}, {self.v1}), ({self.c2}, {self.v2}), ({self.c3}, {self.v3}), ({self.c4}, {self.v4})'


def parse(_input):
    moon_coords = {}
    for coord, cs in zip(COORDS, zip(*_input)):
        moon_coords[coord] = MoonCoord(*cs)
    return moon_coords


def total_energy(moons):
    e = 0
    for index in '1234':
        p = 0
        k = 0
        for m in moons.values():
            p += m.potential_energy(index)
            k += m.kinetic_energy(index)
        e += p * k
    return e


def test1():
    moons = parse(TEST01)
    assert part1(moons, 10) == 179


def test2():
    moons = parse(TEST02)
    assert part1(moons, 100) == 1940


def test3():
    moons = parse(TEST01)
    assert part2(moons) == 2772


def test4():
    moons = parse(TEST02)
    assert part2(moons) == 4686774924


def part1(moons, steps):
    for _ in range(1, steps + 1):
        for mc in moons.values():
            mc.time_step()
    e = total_energy(moons)
    return e


def part2(moons):
    ns = []
    for m in moons.values():
        states = {m.state(): 0}
        for i in range(500000):
            m.time_step()
            state = m.state()
            if state in states:
                ns.append(i)
                break
            states[state] = i
    ns = [n + 1 for n in ns]
    a, b, c = ns
    return lcm(lcm(a, b), c)


def main():
    test1()
    test2()

    moons = parse(INPUT)
    p1 = part1(moons, 1000)
    print(f'Part 1: {p1}')

    test3()
    test4()

    p2 = part2(moons)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
