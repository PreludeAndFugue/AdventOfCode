from collections import Counter
from functools import cache
import heapq

from help import get_input

TEST = '''Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.'''

TEST1 = '''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'''

T = 24

def parse(s):
    for line in s.split('\n'):
        x = line.split()
        parts = x[1][:-1], x[6], x[12], x[18], x[21], x[27], x[30]
        yield tuple(map(int, parts))


def quality_level(robots, material, blueprint):
    id_ = blueprint[0]
    geodes = material[3]
    return id_ * geodes


@cache
def next_robots_material(robots, material, blueprint):
    '''
    State: robots and materials
    '''
    ore, clay, obsidian, geode = material
    robot_ore, robot_clay, robot_obsidian, robot_geode = robots

    states = [(robots, material)]

    _, ore_ore, clay_ore, ob_ore, ob_clay, g_ore, g_ob = blueprint

    # make geode robot
    if ore >= g_ore and obsidian >= g_ob:
        new_robots = robot_ore, robot_clay, robot_obsidian, robot_geode + 1
        new_material = ore - g_ore, clay, obsidian - g_ob, geode
        new_state = new_robots, new_material
        states.append(new_state)
        # if we can build a geode robot, don't look at other possible new states
        return states

    # make obsidian robot
    if ore >= ob_ore and clay >= ob_clay:
        new_robots = robot_ore, robot_clay, robot_obsidian + 1, robot_geode
        new_material = ore - ob_ore, clay - ob_clay, obsidian, geode
        new_state = new_robots, new_material
        states.append(new_state)
        # if we can build a geode robot, don't look at other possible new states
        return states

    # make clay robot
    if ore >= clay_ore:
        new_robots = robot_ore, robot_clay + 1, robot_obsidian, robot_geode
        new_material = ore - clay_ore, clay, obsidian, geode
        new_state = new_robots, new_material
        states.append(new_state)

    # make ore robot
    if ore >= ore_ore:
        new_robots = robot_ore + 1, robot_clay, robot_obsidian, robot_geode
        new_material = ore - ore_ore, clay, obsidian, geode
        new_state = new_robots, new_material
        states.append(new_state)

    return states


def run(blueprint):
    '''
    Blueprint:
        id, ore robot cost (ore), clay robot cost (ore), obsidian robot cost (ore, clay),
        geode robot cost (ore, obsidian)
        id, ore_ore, clay_ore, ob_ore, ob_clay, g_ore, g_ob
    '''
    # ore, clay, obsidian, geode
    robots = 1, 0, 0, 0
    # ore, clay, obsidian, geode
    material = 0, 0, 0, 0
    # first item is time
    start = 0, robots, material

    q = [start]
    seen = set()
    best_quality_level = 0
    # best_example = None

    # i = 0

    while q:
        state = heapq.heappop(q)
        t, robots, material = state

        # i += 1
        # if i % 1_000_000 == 0:
        #     print(i, len(q))
        #     print(t, robots, material, best_quality_level)

        if t == T:
            ql = quality_level(robots, material, blueprint)
            if ql > best_quality_level:
                best_quality_level = ql
                # best_example = robots, material

        else:
            for nrobots, nmaterial in next_robots_material(robots, material, blueprint):

                # print(nrobots, nmaterial)
                # print('new material', robots)
                total_material = robots[0] + nmaterial[0], robots[1] + nmaterial[1], robots[2] + nmaterial[2], robots[3] + nmaterial[3]
                # input()

                nstate = t + 1, nrobots, total_material
                check = nrobots, total_material
                if check not in seen:
                    heapq.heappush(q, nstate)
                    seen.add(check)

    # print(best_example)
    return best_quality_level


def part1(blueprints):
    n = 0
    for i, b in enumerate(blueprints):
        # print('blueprint:', i + 1)
        n += run(b)
    return n


def main():
    s = get_input('19')
    # s = TEST1.strip()
    blueprints = [b for b in parse(s)]
    # b1 = blueprints[1]

    # p1 = run(b1)
    p1 = part1(blueprints)

    print('Part 1:', p1)


def test1():
    blueprint = 1, 4, 2, 3, 14, 2, 7
    robots = 1, 0, 0, 0
    material = 0, 0, 0, 0
    n = next_robots_material(robots, material, blueprint)
    assert len(n) == len(set(n))
    c = Counter(n)
    assert len(n) == len(set(c.keys()))


if __name__ == '__main__':
    main()
    # test1()
