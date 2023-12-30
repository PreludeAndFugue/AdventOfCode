
'''
Typical claim format:
#1 @ 126,902: 29x28
'''

from collections import namedtuple
import re

from help import get_input

TEST = '''#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2'''

Claim = namedtuple('Claim', ['id', 'x', 'y', 'dx', 'dy'])

pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')


def parse(d):
    for line in d.split('\n'):
        match = pattern.fullmatch(line)
        yield Claim(*[int(x) for x in match.groups()])


def points_in_claim(claim):
    points = set()
    for x in range(claim.x, claim.x + claim.dx):
        for y in range(claim.y, claim.y + claim.dy):
            points.add((x, y))
    return points


def get_overlap(claim1, claim2):
    '''Return set of coords of points in overlap.'''
    points1 = points_in_claim(claim1)
    points2 = points_in_claim(claim2)
    return points1.intersection(points2)


def part1(claims):
    points_in_claims = set()
    overlap_points = set()
    for claim in claims:
        points = points_in_claim(claim)
        overlap_points.update(points_in_claims.intersection(points))
        points_in_claims.update(points)
    return overlap_points


def part2(claims, overlap_points):
    for claim in claims:
        points = points_in_claim(claim)
        if not overlap_points.intersection(points):
            return claim.id


def main():
    d = get_input('03')
    claims = list(parse(d))

    p1 = part1(claims)
    print(len(p1))

    p2 = part2(claims, p1)
    print(p2)


if __name__ == '__main__':
    main()
