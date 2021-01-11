#!python3

'''
Input
Hit Points: 55
Damage: 8


Answers
-------
854: too low
874: too low
894: too low
907: not right answer
914: ?
927: ?
934: ?
947: ?
953: correct - updated model to make sure that Wizard can't buy spell currently in use.
967: ?
974: ?
987: ?
'''

from copy import deepcopy

class Spell(object):
    def __init__(self, name, cost, damage, armour, hit_points, mana, turns):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armour = armour
        self.hit_points = hit_points
        self.mana = mana
        self.turns = turns


    def is_instant(self):
        return self.name in ('magic_missile', 'drain')


    def apply(self, wizard, boss):
        boss.hit_points -= self.damage
        wizard.hit_points += self.hit_points
        wizard.mana += self.mana
        self.turns -= 1


    @classmethod
    def magic_missile(cls):
        return cls('magic_missile', 53, 4, 0, 0, 0, 0)

    @classmethod
    def drain(cls):
        return cls('drain', 73, 2, 0, 2, 0, 0)

    @classmethod
    def shield(cls):
        return cls('shield', 113, 0, 7, 0, 0, 6)

    @classmethod
    def poison(cls):
        return cls('poison', 173, 3, 0, 0, 0, 6)

    @classmethod
    def recharge(cls):
        return cls('recharge', 229, 0, 0, 0, 101, 5)


    @classmethod
    def get_all(cls):
        return [cls.magic_missile(), cls.drain(), cls.shield(), cls.poison(), cls.recharge()]


    def __repr__(self):
        if self.name in ('magic_missile', 'drain'):
            return f'{self.name}'
        else:
            return f'{self.name}(t: {self.turns})'


class Player(object):
    @property
    def is_dead(self):
        return self.hit_points <= 0


class Wizard(Player):
    def __init__(self, hit_points, mana):
        self.hit_points = hit_points
        self.mana = mana


    def can_buy_spell(self, spell, spells):
        names = [s.name for s in spells]
        if spell.name in names:
            return False
        return self.mana >= spell.cost


    def __repr__(self):
        return f'W(h: {self.hit_points}, m: {self.mana})'


    # def __deepcopy__(self, memo):
    #     return Wizard(self.hit_points, self.mana)


class Boss(Player):
    def __init__(self, hit_points, damage):
        self.hit_points = hit_points
        self.damage = damage


    def attack(self, wizard, spells):
        armour = sum(s.armour for s in spells)
        damage = self.damage - armour
        damage = 1 if damage < 1 else damage
        wizard.hit_points -= damage


    def __repr__(self):
        return f'B(h: {self.hit_points}, d: {self.damage})'


class Game(object):
    def __init__(self, wizard, boss):
        self.cost = 0
        self.is_player_turn = True
        self.wizard = wizard
        self.boss = boss
        self.spells = []


    def make_turn(self):
        if self.is_over():
            return [self]
        if self.is_player_turn:
            self.is_player_turn = not self.is_player_turn
            # part 2
            self.wizard.hit_points -=1

            new_games = self._player_turn()
            return new_games
        else:
            self._boss_turn()
            self.is_player_turn = not self.is_player_turn
            return [self]


    def is_over(self):
        return self.wizard.is_dead or self.boss.is_dead


    def is_win(self):
        return not self.wizard.is_dead and self.boss.is_dead


    def _player_turn(self):
        self._apply_spells()
        if self.boss.is_dead:
            return [self]
        return self._choose_spells()


    def _boss_turn(self):
        self._apply_spells()
        if self.boss.is_dead:
            return
        self.boss.attack(self.wizard, self.spells)


    def _apply_spells(self):
        for spell in self.spells:
            spell.apply(self.wizard, self.boss)
        self.spells = [spell for spell in self.spells if spell.turns > 0]


    def _choose_spells(self):
        new_games = []
        has_bought_spell = False
        for spell in Spell.get_all():
            if self.wizard.can_buy_spell(spell, self.spells):
                has_bought_spell = True
                g = deepcopy(self)
                g._buy_spell(spell)
                new_games.append(g)
        if has_bought_spell:
            return new_games
        else:
            return [self]


    def _buy_spell(self, spell):
        self.cost += spell.cost
        self.wizard.mana -= spell.cost
        # print('wizard mana', self.wizard.mana)
        if spell.is_instant():
            spell.apply(self.wizard, self.boss)
        else:
            self.spells.append(spell)


    def __repr__(self):
        return f'cost: {self.cost}, player turn: {self.is_player_turn}\n{self.wizard}, {self.boss}\n{self.spells}\n'


class MetaGame(object):
    def __init__(self, game):
        self.games = [game]
        self.min_cost = 1_000_000_000_000


    def make_turn(self):
        new_games = []
        for game in self.games:
            for g in game.make_turn():
                if g.is_over():
                    if g.cost < self.min_cost and g.is_win():
                        self.min_cost = g.cost
                        print(g)
                else:
                    if g.cost < self.min_cost:
                        new_games.append(g)
        self.games = new_games


    def are_all_done(self):
        return not self.games


    def __repr__(self):
        parts = []
        for i, g in enumerate(self.games, start=1):
            parts.append(f'Game {i}')
            parts.append(repr(g))
        return '\n'.join(parts)


def test1():
    w = Wizard(10, 250)
    b = Boss(13, 8)
    g = Game(w, b)
    m = MetaGame(g)
    while not m.are_all_done():
        m.make_turn()
    assert m.min_cost == 226


def test2():
    w = Wizard(10, 250)
    b = Boss(14, 8)
    g = Game(w, b)
    m = MetaGame(g)
    while not m.are_all_done():
        m.make_turn()
    assert m.min_cost == 641


def part1():
    w = Wizard(50, 500)
    b = Boss(55, 8)
    g = Game(w, b)
    m = MetaGame(g)
    while not m.are_all_done():
        m.make_turn()
    return m.min_cost


def main():
    # test1()
    # test2()

    p = part1()
    print(p)


if __name__ == '__main__':
    main()
