#!python3

from collections import defaultdict, Counter
from itertools import combinations, permutations

from helpers import BASE
from day19helpers import ROTATIONS

'''
https://www.euclideanspace.com/maths/algebra/matrix/transforms/examples/index.htm

https://i.imgur.com/PT87dU0.png
'''

TEST01 = '''--- scanner 0 ---
-1,-1,1
-2,-2,2
-3,-3,3
-2,-3,1
5,6,-4
8,0,7

--- scanner 0 ---
1,-1,1
2,-2,2
3,-3,3
2,-1,3
-5,4,-6
-8,-7,0

--- scanner 0 ---
-1,-1,-1
-2,-2,-2
-3,-3,-3
-1,-3,-2
4,6,5
-7,0,8

--- scanner 0 ---
1,1,-1
2,2,-2
3,3,-3
1,3,-2
-4,-6,5
7,0,8

--- scanner 0 ---
1,1,1
2,2,2
3,3,3
3,1,2
-6,-4,-5
0,7,-8'''


TEST02 = '''--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14'''


def parse(string):
    for scanner in string.strip().split('\n\n'):
        parts = scanner.split('\n')
        name = parts[0]
        name = name.strip('- scanner')
        coords = parts[1:]
        coords = [tuple(map(int, c.split(','))) for c in coords]
        yield int(name), coords


def diff(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return x1 - x2, y1 - y2, z1 - z2


def diffs(coords):
    return set((x1 - x2, y1 - y2, z1 - z2) for (x1, y1, z1), (x2, y2, z2) in combinations(coords, 2))


def overlap(coords1, coords2):
    '''
    If two sets of coordinates overlap then return the vector different between the two
    sets.
    '''
    for rotation in ROTATIONS:
        c2_rotated = [rotation(*c) for c in coords2]
        counter = Counter()
        for c1 in coords1:
            for c2 in c2_rotated:
                d = diff(c1, c2)
                counter.update([d])
        x, m = counter.most_common(1)[0]
        if m >= 12:
            return translate_coords(c2_rotated, x), x
    return None, None


def translate_coords(coords, vector):
    dx, dy, dz = vector
    return [(x + dx, y + dy, z + dz) for (x, y, z) in coords]


def manhattan_distance(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


def test1():
    all_sets = set()
    for _, coords in parse(TEST01.strip()):
        all_sets.add(frozenset(coords))
    test = all_sets.pop()
    match_count = 0
    for rotation in ROTATIONS:
        rotated = set([rotation(*t) for t in test])
        for x in all_sets:
            if rotated == x:
                match_count += 1
    assert match_count == 4


def part1(string):
    scanners = {n: coords for n, coords in parse(string)}
    final_coords = set(scanners[0])
    scanner_ids = [id for id in scanners.keys() if id != 0]
    scanner_positions = [(0, 0, 0)]
    while scanner_ids:
        s_id = scanner_ids.pop(0)
        c2 = scanners[s_id]
        c2_rotated, offset = overlap(final_coords, c2)
        if c2_rotated is not None:
            final_coords = final_coords.union(c2_rotated)
            scanner_positions.append(offset)
        else:
            scanner_ids.append(s_id)
    return len(final_coords), scanner_positions


def part2(scanner_positions):
    distances = []
    for s1, s2 in combinations(scanner_positions, 2):
        distances.append(manhattan_distance(s1, s2))
    return max(distances)


def main():
    data = open(BASE + 'day19.txt', 'r').read()


    t1, t1_coords = part1(TEST02.strip())
    assert t1 == 79

    t2 = part2(t1_coords)
    assert t2 == 3621

    p1, p1_coords = part1(data)
    print(f'Part 1: {p1}')

    p2 = part2(p1_coords)
    print(f'Part 2: {p2}')



if __name__ == '__main__':
    main()
