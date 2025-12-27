from functools import reduce
from math import dist
from itertools import combinations
from operator import mul

from help import get_input

TEST01 = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''

source = TEST01.strip()
source = get_input(8)


def part1():
    points = []
    for line in source.split('\n'):
        p = tuple(map(int, line.split(',')))
        points.append(p)
    points.sort()
    points1 = []
    for p1, p2 in combinations(points, 2):
        d = dist(p1, p2)
        # print(p1, p2, dist(p1, p2))
        points1.append((d, p1, p2))
    points1.sort()

    C = len(points)
    N = 1000
    groups = []
    for d, p1, p2 in points1:
        # print(d, p1, p2)
        added_to_groups = []
        for group in groups:
            if p1 in group or p2 in group:
                group.add(p1)
                group.add(p2)
                # print('\tadding to group', group)
                added_to_groups.append(group)

        if len(added_to_groups) > 1:
            new_group = set()
            for g in added_to_groups:
                new_group.update(g)
                groups.remove(g)
            groups.append(new_group)

        if not added_to_groups:
            # print('\t2creating new group')
            groups.append(set([p1, p2]))

        if len(groups) == 1:
            g = groups[0]
            if len(g) == C:
                print(p1, p2)
                x1 = p1[0]
                x2 = p2[0]
                # part 2
                print(x1*x2)
                break

    # print(groups)
    sizes = [len(g) for g in groups]
    sizes.sort(reverse=True)
    # print(sizes)
    n = reduce(mul, sizes[:3], 1)
    return n


if __name__ == '__main__':
    p1 = part1()
    print(p1)
