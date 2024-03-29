from collections import Counter, defaultdict
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

T1 = 24
T2 = 32

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
        return [new_state]
        # states.append(new_state)

    max_robots_obsidian = blueprint[6]
    # make obsidian robot
    if ore >= ob_ore and clay >= ob_clay and robot_obsidian < max_robots_obsidian:
        new_robots = robot_ore, robot_clay, robot_obsidian + 1, robot_geode
        new_material = ore - ob_ore, clay - ob_clay, obsidian, geode
        new_state = new_robots, new_material
        states.append(new_state)
        # if we can build an obsidian robot, don't look at other possible new states
        # states.append(new_state)
        return [new_state]
        # return states

    max_robots_clay = blueprint[4]
    # make clay robot
    if ore >= clay_ore and robot_clay < max_robots_clay:
        new_robots = robot_ore, robot_clay + 1, robot_obsidian, robot_geode
        new_material = ore - clay_ore, clay, obsidian, geode
        new_state = new_robots, new_material
        states.append(new_state)

    max_robots_ore = max(blueprint[1], blueprint[2], blueprint[3], blueprint[5])
    # make ore robot
    if ore >= ore_ore and robot_ore < max_robots_ore:
        new_robots = robot_ore + 1, robot_clay, robot_obsidian, robot_geode
        new_material = ore - ore_ore, clay, obsidian, geode
        new_state = new_robots, new_material
        states.append(new_state)

    return states


def run(blueprint, T):
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
    # negative of number of geodes, time
    start = 0, 0, robots, material

    q = [start]
    seen = set()
    best_quality_level = 0
    best_example = None
    best_geode_count = 0

    # the most number of geodes produced for a particular time.
    t_geodes = defaultdict(int)

    # i = 0

    while q:
        state = heapq.heappop(q)
        geode_count, t, robots, material = state
        geode_count = -geode_count

        # print(t, robots, material)
        if geode_count < t_geodes[t]:
            continue
        else:
            t_geodes[t] = geode_count

        # i += 1
        # if i % 1_000_000 == 0:
        #     print(i, len(q))
        #     print(t, robots, material, best_quality_level)

        # don't need to perform the final step: creating a new robot is pointless because
        # it doesn't add to the number of geodes created.
        if t == T - 1:
            final_material = robots[0] + material[0], robots[1] + material[1], robots[2] + material[2], robots[3] + material[3]
            ql = quality_level(robots, final_material, blueprint)
            if ql > best_quality_level:
                best_quality_level = ql
                best_example = robots, final_material
            best_geode_count = max(final_material[3], best_geode_count)

        else:
            for nrobots, nmaterial in next_robots_material(robots, material, blueprint):

                # print(nrobots, nmaterial)
                # print('new material', robots)
                total_material = robots[0] + nmaterial[0], robots[1] + nmaterial[1], robots[2] + nmaterial[2], robots[3] + nmaterial[3]
                new_geode_count = total_material[3]
                # input()

                nstate = -new_geode_count, t + 1, nrobots, total_material
                check = nrobots, total_material
                if check not in seen:
                    heapq.heappush(q, nstate)
                    seen.add(check)

    # print(best_example, best_quality_level, best_geode_count)
    return best_quality_level, best_geode_count


def part1(blueprints, T):
    n = 0
    g = 1
    for i, b in enumerate(blueprints):
        # print('blueprint:', i + 1)
        n1, g1 = run(b, T)
        n += n1
        g *= g1
    return n, g


def main():
    s = get_input('19')
    # s = TEST1.strip()
    blueprints = [b for b in parse(s)]
    b1 = blueprints[0]

    # p1 = run(b1, T1)
    # p1 = part1(blueprints, T1)

    # p1, p2 = part1(blueprints, T1)
    p1, p2 = part1(blueprints[:3], T2)

    # print('Part 1:', p1)
    print('Part 2:', p2)


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
