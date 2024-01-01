base_path = '../day{}.txt'

def get_input(d):
    path = base_path.format(d)
    return open(path, 'r').read().strip()


def manhattan2(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


def manhattan3(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)


def intersection(r1: range, r2: range):
    '''Returns the intersection of two ranges. If the intersection is empty return None'''
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop)) or None
