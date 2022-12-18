
from help import get_input


TEST = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''


def parse(s):
    for line in s.split('\n'):
        yield tuple(map(int, line.split(',')))


def all_neighbours(c):
    x, y, z = c
    for dx in (-1, 1):
        yield x + dx, y, z
    for dy in (-1, 1):
        yield x, y + dy, z
    for dz in (-1, 1):
        yield x, y, z + dz


def neighbours(c, cubes, xmin, xmax, ymin, ymax, zmin, zmax):
    '''Neighbours of a cube that are not lava.'''
    for n in all_neighbours(c):
        if n in cubes:
            continue
        nx, ny, nz = n
        if nx < xmin or xmax < nx:
            continue
        if ny < ymin or ymax < ny:
            continue
        if nz < zmin or zmax < nz:
            continue
        yield n



def fill(start, cubes, xmin, xmax, ymin, ymax, zmin, zmax):
    '''Find outside cubes using a flood fill algorithm'''
    q = [start]
    seen = set()

    while q:
        c = q.pop()

        if c in seen:
            continue
        seen.add(c)

        for n in neighbours(c, cubes, xmin, xmax, ymin, ymax, zmin, zmax):
            q.append(n)

    return seen


def touch_outside_count(c, outside):
    count = 0
    for n in all_neighbours(c):
        if n in outside:
            count += 1
    return count


def main():
    s = get_input('18')
    # s = TEST.strip()
    cubes = set(parse(s))

    xs = [c[0] for c in cubes]
    ys = [c[1] for c in cubes]
    zs = [c[2] for c in cubes]

    xmin = min(xs) - 1
    xmax = max(xs) + 1
    ymin = min(ys) - 1
    ymax = max(ys) + 1
    zmin = min(zs) - 1
    zmax = max(zs) + 1

    start = xmin, ymin, zmin
    outside = fill(start, cubes, xmin, xmax, ymin, ymax, zmin, zmax)

    count = 0
    for c in cubes:
        count += touch_outside_count(c, outside)

    print('Part 2:', count)


if __name__ == '__main__':
    main()
