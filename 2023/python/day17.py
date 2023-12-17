
import heapq

from help import get_input

'''
Answers
- 1081 too high
'''

TEST = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''


# d = get_input('17')
d = TEST.strip()

map_ = {}
for r, line in enumerate(d.split('\n')):
    for c, n in enumerate(line):
        # print(r, c, n)
        map_[(r, c)] = int(n)

LEFT = {
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
    (1, 0): (0, 1)
}
RIGHT = {
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1)
}

def get_next(state, map_):
    h, p, d, l = state
    if l < 2:
        # continue straight on
        r, c = p
        dr, dc = d
        pp = r + dr, c + dc
        hh = map_.get(pp, None)
        if hh is not None:
            yield h + hh, pp, d, l + 1
    # turn left
    dd = LEFT[d]
    r, c = p
    dr, dc = dd
    pp = r + dr, c + dc
    hh = map_.get(pp, None)
    if hh is not None:
        yield h + hh, pp, dd, 0
    # turn right
    dd = RIGHT[d]
    r, c = p
    dr, dc = dd
    pp = r + dr, c + dc
    hh = map_.get(pp, None)
    if hh is not None:
        yield h + hh, pp, dd, 0

start_p = 0, 0
end_p = max(k for k in map_.keys())
# print(start_p, end_p)

# heat, position, direction, step count
start_state = (0, start_p, (0, 1), 0)
check = [start_state]
seen = set()
heapq.heapify(check)

i = 0
while check:
    state = heapq.heappop(check)

    h, (r, c), d, l = state
    state = h, (-r, -c), d, l

    i += 1
    if i % 100_000 == 0:
        print(state)
        print(len(check))

    # print('state', state)
    _, p, _, _ = state

    if p == end_p:
        print('done', h)
        break

    # s = state[0], state[1]
    if state in seen:
        # print('\tin seen', state)
        continue

    seen.add(state)

    for new_state in get_next(state, map_):
        # print('\tnext', new_state)
        h, (r, c), d, l = new_state
        ns = h, (-r, -c), d, l
        heapq.heappush(check, ns)

