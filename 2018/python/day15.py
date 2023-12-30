import heapq

from help import get_input

'''
Part 2
------
469120 too high (incorrect method)
58141 too low
'''

TEST_1 = '''
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
'''

TEST_2 = '''
#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
'''

TEST_3 = '''
#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######
'''

TEST_4 = '''
#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######
'''

TEST_5 = '''
#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######
'''

TEST_6 = '''
#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########
'''

DIRS = [
    # reading order
    (-1, 0), (0, -1), (0, 1), (1, 0)
]

GOBLIN = 'G'
ELF = 'E'


class Unit:
    def __init__(self, p, type_):
        self.p = p
        self.type = type_
        self.attack_power = 3
        self.hit_points = 200

    @property
    def is_alive(self):
        return self.hit_points > 0

    @property
    def is_goblin(self):
        return self.type == GOBLIN

    def move(self, opponent):
        path_start = opponent.path_start
        if path_start is not None:
            # move nearer opponent
            # print('\tmoving', self, path_start)
            self.p = path_start
        dr = abs(self.p[0] - opponent.unit.p[0])
        dc = abs(self.p[1] - opponent.unit.p[1])
        if dr + dc <= 1:
            opponent.unit.hit_points -= self.attack_power

    def __repr__(self) -> str:
        return f'{self.type}({self.hit_points}, {self.p})'


class Opponent:
    def __init__(self, unit, path):
        self.unit = unit
        self.path = path

    @property
    def score(self):
        return len(self.path), self.unit.hit_points

    @property
    def path_start(self):
        if self.path:
            return self.path[0]
        else:
            return None

    def __lt__(self, other):
        return self.score < other.score

    def __repr__(self) -> str:
        return f'{self.unit}, {self.path}'


class Game:
    def __init__(self, units, map_):
        self.units = units
        self.map = map_
        self.round = 0

    def update_elfs(self, attack_power):
        for unit in self.units:
            if unit.type == ELF:
                unit.attack_power = attack_power

    def play(self):
        while not self._is_done():
            self._round()
            self._sort_units()

            # print(self.round)
            # self.print()
            # print(self.units)
            # input()
        # print('done')
        # print(self.round)
        # print(self.units)

    def result(self):
        hit_points = sum(u.hit_points for u in self.units if u.hit_points > 0)
        return self.round*hit_points

    def _round(self):
        for unit in self.units:
            if not unit.is_alive:
                continue
            if self._is_done():
                return
            opponent = self._get_opponent(unit)
            # print('unit', unit, 'opponent', opponent)
            if opponent is None:
                continue
            unit.move(opponent)
        self.round += 1

    def _is_done(self):
        goblins = self._get_alive_goblins()
        if not goblins:
            return True
        elfs = self._get_alive_elfs()
        if not elfs:
            return True
        return False

    def _get_alive_units(self):
        return [u for u in self.units if u.is_alive]

    def _get_alive_goblins(self):
        return [u for u in self.units if u.is_goblin and u.is_alive]

    def _get_alive_elfs(self):
        return [u for u in self.units if not u.is_goblin and u.is_alive]

    def _sort_units(self):
        self.units.sort(key=lambda u: u.p)

    def _get_opponent(self, unit):
        others = self._get_alive_elfs() if unit.is_goblin else self._get_alive_goblins()
        unit_ps = set(u.p for u in self._get_alive_units())
        total_map = self.map - unit_ps
        opponents = []
        for other in others:
            current_map = total_map | set([other.p])
            path = dijkstra(unit.p, other.p, current_map)
            if path is not None:
                opponents.append(Opponent(other, path))
        if not opponents:
            return None
        opponents.sort()
        return opponents[0]

    def print(self):
        rs = set(p[0] for p in self.map)
        cs = set(p[1] for p in self.map)
        r_min = min(rs)
        r_max = max(rs)
        c_min = min(cs)
        c_max = max(cs)
        e_locations = set(u.p for u in self._get_alive_elfs())
        g_locations = set(u.p for u in self._get_alive_goblins())
        rows = []
        for r in range(r_min, r_max + 1):
            row = []
            for c in range(c_min, c_max + 1):
                p = r, c
                if p in e_locations:
                    row.append('E')
                elif p in g_locations:
                    row.append('G')
                elif p in self.map:
                    row.append('.')
                else:
                    row.append('#')
            rows.append(''.join(row))
        print('\n'.join(rows))


def parse(d):
    map_ = set()
    units = []
    for r, row in enumerate(d.split('\n')):
        for c, ch in enumerate(row):
            # print(r, c, ch)
            if ch == '.':
                map_.add((r, c))
            elif ch == 'E' or ch == 'G':
                unit = Unit((r, c), ch)
                units.append(unit)
                map_.add((r, c))
            elif ch == '#':
                pass
            else:
                raise ValueError
    return map_, units


def make_path(end, prev):
    path = []
    p = end
    while p is not None:
        path.append(p)
        p = prev.get(p, None)
    return list(reversed(path))[1:-1]


def dijkstra(start, end, map_):
    # print('\tdijkstra', start, end)
    dist = {}
    prev = {}
    for p in map_:
        dist[p] = 1_000_000_000
        prev[p] = None
    dist[start] = 0

    seen = set()
    q = [(0, start)]

    while q:
        # print('\t', q)
        # input()
        d, p = heapq.heappop(q)

        if p == end:
            return make_path(p, prev)

        if p in seen:
            continue
        seen.add(p)

        for dr, dc in DIRS:
            pp = p[0] + dr, p[1] + dc
            if pp not in map_:
                continue
            dd = d + 1
            if dd < dist[pp]:
                dist[pp] = dd
                prev[pp] = p
            heapq.heappush(q, (dd, pp))
    return None


def test1():
    map_, units = parse(TEST_1.strip())
    g = Game(units, map_)
    g.play()
    assert g.round == 47
    assert g.result() == 27730

    map_, units = parse(TEST_2.strip())
    g = Game(units, map_)
    g.play()
    assert g.round == 37
    assert g.result() == 36334

    map_, units = parse(TEST_3.strip())
    g = Game(units, map_)
    g.play()
    assert g.round == 46
    assert g.result() == 39514

    map_, units = parse(TEST_4.strip())
    g = Game(units, map_)
    g.play()
    assert g.round == 35
    assert g.result() == 27755

    map_, units = parse(TEST_5.strip())
    g = Game(units, map_)
    g.play()
    assert g.round == 54
    assert g.result() == 28944

    map_, units = parse(TEST_6.strip())
    g = Game(units, map_)
    g.play()
    assert g.round == 20
    assert g.result() == 18740

    print('tests pass')


def test2():
    map_, units = parse(TEST_1.strip())
    g = Game(units, map_)
    g.update_elfs(15)
    g.play()
    assert g.round == 29
    assert g.result() == 4988

    map_, units = parse(TEST_3.strip())
    g = Game(units, map_)
    g.update_elfs(4)
    g.play()
    assert g.round == 33
    assert g.result() == 31284

    map_, units = parse(TEST_4.strip())
    g = Game(units, map_)
    g.update_elfs(15)
    g.play()
    assert g.round == 37
    assert g.result() == 3478

    map_, units = parse(TEST_5.strip())
    g = Game(units, map_)
    g.update_elfs(12)
    g.play()
    assert g.round == 39
    assert g.result() == 6474

    map_, units = parse(TEST_6.strip())
    g = Game(units, map_)
    g.update_elfs(34)
    g.play()
    assert g.round == 30
    assert g.result() == 1140

    print('tests 2 pass')

    assert part2(TEST_1.strip(), 13) == 4988
    assert part2(TEST_3.strip(), 2) == 31284
    assert part2(TEST_4.strip(), 12) == 3478
    assert part2(TEST_5.strip(), 10) == 6474
    assert part2(TEST_6.strip(), 31) == 1140


def part2(d, start_hit_power):
    hit_power = start_hit_power
    while True:
        map_, units = parse(d)
        g = Game(units, map_)
        g.update_elfs(hit_power)
        g.play()
        if any(not u.is_alive for u in g.units if not u.is_goblin):
            print('hit power too low', hit_power)
            hit_power += 1
        else:
            return g.result()


def main():
    d = get_input('15')
    # d = TEST_1.strip()
    # d = TEST_2.strip()
    # d = TEST_3.strip()
    # d = TEST_4.strip()
    # d = TEST_5.strip()
    # d = TEST_6.strip()
    map_, units = parse(d)
    # print(map_)
    # print(units)

    test1()
    test2()

    # g = Game(units, map_)

    # g.update_elfs(13)

    # g.play()
    # print([u for u in g.units if not u.is_goblin and not u.is_alive])
    # print(g.result(), g.round)

    p2 = part2(d, 10)
    print(p2)


if __name__ == '__main__':
    main()
