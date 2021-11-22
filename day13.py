#!python3

from queue import Queue

INPUT = 1352
GOAL = 31, 39

TEST_INPUT = 10
TEST_GOAL = 7, 4

def is_open(x, y):
    n = x*x + 3*x + 2*x*y + y + y*y
    n += INPUT
    b = bin(n)
    c = b.count('1')
    return not (c % 2)


def neighbours(x, y):
    result = []
    for d in (-1, 1):
        x1 = x + d
        if x1 >= 0:
            result.append((x1, y))
        y1 = y + d
        if y1 >= 0:
            result.append((x, y1))
    return result


def draw_locations():
    rows = []
    for y in range(7):
        row = []
        for x in range(10):
            o = is_open(x, y)
            if o:
                row.append('.')
            else:
                row.append('#')
        rows.append(''.join(row))
    rows = '\n'.join(rows)
    print(rows)


def main1():
    goal = GOAL
    location = 1, 1
    seen = set([location])
    queue = Queue()
    queue.put((location, 0))
    while queue:
        v, d = queue.get()
        if v == goal:
            return v, d
        for n in neighbours(*v):
            if n not in seen:
                seen.add(n)
                if is_open(*n):
                    queue.put((n, d + 1))


def main2():
    location = 1, 1
    seen = set([location])
    near = set([location])
    queue = Queue()
    queue.put((location, 0))
    while not queue.empty():
        v, d = queue.get()
        if d <= 50:
            near.add(v)
        for n in neighbours(*v):
            if n not in seen:
                seen.add(n)
                if is_open(*n):
                    queue.put((n, d + 1))
    return near


if __name__ == '__main__':
    x = main1()
    print(x)
    y = main2()
    print(len(y))
