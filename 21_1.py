#!python3

from itertools import chain, combinations, product

'''
Hit Points: 104
Damage: 8
Armor: 1
'''

BOSS_HIT_POINTS = 104
BOSS_DAMAGE = 8
BOSS_ARMOUR = 1

HIT_POINTS = 100

# cost, damage, armour
WEAPONS = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
]

def get_weapon():
    for w in WEAPONS:
        yield [w]


# cost, damage, armour
ARMOUR = [
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5)
]

def get_armour():
    yield []
    for a in ARMOUR:
        yield [a]


#cost, damage, armour
RINGS = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3)
]

def get_rings():
    yield []
    for r in RINGS:
        yield [r]
    for x in combinations(RINGS, 2):
        yield list(x)


def get_items():
    w = get_weapon()
    a = get_armour()
    r = get_rings()
    # print(r)
    for p in product(w, a, r):
        yield list(chain(*p))


class Player(object):
    def __init__(self, hit_points, damage, armour):
        self.hit_points = hit_points
        self.damage = damage
        self.armour = armour


    @property
    def is_dead(self):
        return self.hit_points <= 0


    def hit(self, other):
        damage = self.damage - other.armour
        damage = 1 if damage < 1 else damage
        other.hit_points -= damage


    @classmethod
    def make_boss(cls):
        return cls(BOSS_HIT_POINTS, BOSS_DAMAGE, BOSS_ARMOUR)


    @classmethod
    def make_player(cls, items):
        damage = sum(item[1] for item in items)
        armour = sum(item[2] for item in items)
        return cls(HIT_POINTS, damage, armour)


    def __repr__(self):
        return f'Player({self.hit_points}, {self.damage}, {self.armour})'


def play(player, boss):
    '''Returns True if player wins.'''
    while True:
        player.hit(boss)
        if boss.is_dead:
            return True
        boss.hit(player)
        if player.is_dead:
            return False


def test():
    player = Player(8, 5, 5)
    boss = Player(12, 7, 2)
    result = play(player, boss)
    print(result)


def part1():
    results = []
    for items in get_items():
        cost = sum(item[0] for item in items)
        player = Player.make_player(items)
        boss = Player.make_boss()
        result = play(player, boss)
        if result:
            results.append(cost)
    print(min(results))


def part2():
    results = []
    for items in get_items():
        cost = sum(item[0] for item in items)
        player = Player.make_player(items)
        boss = Player.make_boss()
        result = play(player, boss)
        if not result:
            results.append(cost)
    print(max(results))



if __name__ == '__main__':
    part1()
    part2()
