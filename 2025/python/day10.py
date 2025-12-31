
import heapq

test = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''


source = test.strip()
source = open('day10.txt', 'r').read().strip()


def distance(lights, end_lights):
    return sum(1 if l == el else 0 for (l, el) in zip(lights, end_lights))


def switch(lights, buttons) -> tuple:
    x = tuple(not l if i in buttons else l for (i, l) in enumerate(lights))
    # print('\t', 'switch', lights, '->', x, 'buttons', buttons)
    return x


def search(lights, buttons):
    # print('searching', lights, buttons)
    l = tuple([False]*len(lights))
    q = [(0, l)]
    explored = set([l])
    while q:
        n, l1 = heapq.heappop(q)
        # print('\t', 'search', n, l1)
        if l1 == lights:
            return n
        for b in buttons:
            l2 = switch(l1, b)
            if l2 not in explored:
                explored.add(l2)
                heapq.heappush(q, (n + 1, l2))
    raise ValueError


t = 0
for line in source.split('\n'):
    # print(line)
    l1, l2 = line.split(']')
    l1 = l1[1:]
    l2, l3 = l2.split('{')
    l3 = l3[:-1]

    lights = tuple(True if s == '#' else False for s in l1)
    # print(lights)

    buttons = l2.strip().split(' ')
    buttons = [b.strip('()').split(',') for b in buttons]
    buttons = [set(map(int, b)) for b in buttons]
    # print(buttons)

    n = search(lights, buttons)
    t += n
    # print(n)
    # print('---')

print(t)