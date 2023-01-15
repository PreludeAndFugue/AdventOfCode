
import heapq
from day17 import temp_scan, read_scan, make_map, draw_map, export_map, INPUT, TEST_INPUT, TEST_2


CLAY = '#'
WATER = '~'
FLOW = '|'
EMPTY = '.'
START = '+'


class Map():
    def __init__(self, clay):
        self.locations = clay
        self.y_max = max(y for _, y in clay.keys())
        self.start = self._find_start(clay)


    def get_neighbours(self, location):
        '''
        Tries to get a neighbour for a location.
        - first try down
        - then try left
        - then try right
        '''

        x, y = location

        if y >= self.y_max:
            return []

        below = x, y + 1
        below_content = self.get(below)
        # print('below', below, below_content)
        if below[1] <= self.y_max and below_content == EMPTY:
            return [below]

        neighbours = []

        left = x - 1, y
        below_left = x - 1, y + 1
        left_content = self.get(left)
        below_left_content = self.get(below_left)
        # print('left', left, left_content)
        if left_content == EMPTY and below_content != FLOW:
            neighbours.append(left)

        right = x + 1, y
        below_right = x + 1, y + 1
        right_content = self.get(right)
        below_right_content = self.get(below_right)
        # print('right', right, right_content)
        if right_content == EMPTY and below_content != FLOW:
            neighbours.append(right)

        return neighbours


    def set(self, location, value):
        self.locations[location] = value


    def get(self, location):
        return self.locations.get(location, '.')


    def _find_start(self, locations):
        for location, value in locations.items():
            if value == START:
                return location
        raise ValueError


def dfs(M):
    q = [(0, M.start)]
    heapq.heapify(q)
    seen = set()

    max_d = 0
    max_location = None

    locations = []

    while q:
        d, location = heapq.heappop(q)
        # print(d, location)
        # input()
        if d > max_d:
            max_d = d
            max_location = location

        neighbours = [n for n in M.get_neighbours(location) if n not in seen]

        if not neighbours:
            # locations.append(location)
            return d, location, locations

        for neighbour in neighbours:
            if neighbour in seen:
                continue
            heapq.heappush(q, (d + 1, neighbour))
            seen.add(neighbour)

    return max_d, max_location, locations


def fill(location, M):
    if is_leaky(location, M):
        M.set(location, FLOW)
    else:
        M.set(location, WATER)


def is_leaky(location, M):
    '''
        ..X....#
        .#######
    '''
    is_leaky_left = True
    is_leaky_right = True
    x, y = location
    l = x
    while True:
        l -= 1
        left = l, y
        below_left = l, y + 1
        left_content = M.get(left)
        below_left_content = M.get(below_left)
        if below_left_content == EMPTY or below_left_content == FLOW:
            return True
        if left_content == CLAY:
            is_leaky_left = False
            break

    r = x
    while True:
        r += 1
        right = r, y
        below_right = r, y + 1
        right_content = M.get(right)
        below_right_content = M.get(below_right)
        if below_right_content == EMPTY or below_right_content == FLOW:
            return True
        if right_content == CLAY:
            is_leaky_right = False
            break

    return is_leaky_left or is_leaky_right


def main():
    # scan = read_scan(TEST_INPUT)
    clay, start, y_max = temp_scan(TEST_2)

    # r = open(INPUT, 'r').read().strip()
    # scan = read_scan(r)

    # clay, _, y_max = make_map(scan)
    M = Map(clay)

    while True:
        d, location, locations = dfs(M)
        if location == M.start:
            break
        print(location)
        # print(locations)
        fill(location, M)
        # for l in locations:
        #     fill(l, M)

        print(draw_map(M.locations, dict()))
        input()

    count = 0
    for v in M.locations.values():
        if v == WATER or v == FLOW:
            count += 1
    print(count)
    export_map(M.locations, dict())



if __name__ == '__main__':
    main()

