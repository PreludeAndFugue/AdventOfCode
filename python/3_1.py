#!python3

'''3.1

Typical claim format:
#1 @ 126,902: 29x28
'''

from collections import namedtuple
from itertools import combinations
import re

TEST = '''#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2'''

INPUT = '3.txt'

Claim = namedtuple('Claim', ['id', 'x', 'y', 'dx', 'dy'])

pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)\n')


def get_test_input():
    results = []
    for line in TEST.split('\n'):
        results.append(parse_line(line + '\n'))
    return results


def get_input():
    results = []
    with open(INPUT, 'r') as f:
        for line in f: 
            results.append(parse_line(line))
    return results
    
    
def parse_line(line):
    match = pattern.fullmatch(line)
    return Claim(*[int(x) for x in match.groups()])
    
    
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
    
    
def main():
    claims = get_input()
    points_in_claims = set()
    overlap_points = set()
    for claim in claims:
        points = points_in_claim(claim)
        overlap_points.update(points_in_claims.intersection(points))
        points_in_claims.update(points)
    print(len(overlap_points))
    return claims, overlap_points
    
    
def main2(claims, overlap_points):
    for claim in claims:
        points = points_in_claim(claim)
        if not overlap_points.intersection(points):
            print(claim)
    
    
def test():
    all_points = set()
    overlap_points = set()
    for claim in get_test_input():
        points = points_in_claim(claim)
        overlap_points.update(all_points.intersection(points))
        all_points.update(points)
    print(len(overlap_points))
    
    
    
if __name__ == '__main__':
    test()
    claims, overlap_points = main()
    main2(claims, overlap_points)
    