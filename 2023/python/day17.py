
import heapq

from help import get_input

'''
https://www.reddit.com/r/adventofcode/comments/18kipuy/2023_day_17_why_do_most_people_dijkstras_work/

You need to account for the minimum and maximum straight-line distance you can travel --
there's no way around that. But you can account for it in two different places...

Include it in the description of the node you're at -- you have an x,y coordinate, a
direction of travel to get here, and the number of moves in that direction you've made.
With that information, you can figure out your continuations. For part 1, the starting
node is connected to two nodes, which could be described like:
    (1,0) east, 1 square and (0,1) south, 1 square
include it in the connections on the graph. I can travel east 1-3 squares, or i can travel
south 1-3 squares. Those are all directly connected to the starting square. So you have
six nodes connected to the starting node --
    (1,0) east, (2,0) east, (3,0) east, (0,1) south, (0,2) south, (0,3) south.
Now when you travel to one of those nodes, you no longer consider continuing straight --
all of the straight-line continuations are already in your boundary nodes as one-step with
a given cost. You only need consider turning 90° right or left, then traveling 1-3 nodes
in that direction.


https://www.reddit.com/r/adventofcode/comments/18khohi/2023_day_17_why_can_you_only_cache_pos_dir_in/

From how I understand it there are two different ways to set up the state graph, on which
we search the shortest path.

Either we do (pos, dir, chain) and every state has at most 3 neighbors, representing a
single step in a direction.

Or we just do (pos, dir) and assume it is the beginning of a straight section and it
neighbors are every state that can be reached in a straight line from the current position
that is orthogonal to the previous straight.

Both are possible, but #2 results in a smaller (but more connected) graph and should be
faster to search.


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

TEST_2 = '''111111111111
999999999991
999999999991
999999999991
999999999991'''

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


def make_map(d):
    map_ = {}
    for r, line in enumerate(d.split('\n')):
        for c, n in enumerate(line):
            # print(r, c, n)
            map_[(r, c)] = int(n)
    return map_


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


def get_next_2(state, map_):
    h, p, d, l = state
    if l < 3:
        # continue straight on
        r, c = p
        dr, dc = d
        pp = r + dr, c + dc
        hh = map_.get(pp, None)
        if hh is not None:
            yield h + hh, pp, d, l + 1
    else:
        if l < 10:
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


# d = get_input('17')
# d = TEST.strip()
d = TEST_2.strip()

map_ = make_map(d)


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

    i += 1
    if i % 100_000 == 0:
        print(state)
        print(len(check))

    # print('state', state)
    _, p, _, l = state

    if p == end_p and l > 2:
        print('done', h)
        break

    # s = state[0], state[1]
    if state in seen:
        # print('\tin seen', state)
        continue

    seen.add(state)

    # for new_state in get_next(state, map_):
    for new_state in get_next_2(state, map_):
        # print('\tnext', new_state)
        h, (r, c), d, l = new_state
        ns = h, (r, c), d, l
        heapq.heappush(check, ns)

