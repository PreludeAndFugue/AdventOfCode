#!python3

'''
Input
Hit Points: 55
Damage: 8
'''


class Spell(object):
    def __init__(self, name, cost, damage, armour, hit_points, mana, turns):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armour = armour
        self.hit_points = hit_points
        self.mana = mana
        self.turns = turns


    def apply(self, wizard, boss):
        boss.damage -= self.damage
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


class Player(object):
    @property
    def is_dead(self):
        return self.hit_points <= 0


class Wizard(Player):
    def __init__(self, hit_points, mana):
        self.hit_points = hit_points
        self.mana = mana


class Boss(Player):
    def __init__(self, hit_points, damage):
        self.hit_points = hit_points
        self.damage = damage


    def attack(self, wizard, spells):
        armour = [s.armour for s in spells]
        damage = self.damage - armour
        damage = 1 if damage < 1 else damage
        wizard.hit_points -= damage





class Game(object):
    def __init__(self, wizard, boss):
        self.cost = 0
        self.player_turn = True
        self.wizard = wizard
        self.boss = boss
        self.spells = []


    def make_turn(self):
        if self.player_turn:
            for spell in self.spells:
                spell.apply(self.wizard, self.boss)
            if self.boss.is_dead:
                return
        else:
            for spell in self.spells:
                spell.apply(self.wizard, self.boss)
            if self.boss.is_dead:
                return
            self.boss.attack(self.wizard, self.spells)

        self.player_turn = not self.player_turn



def test1():
    w = Wizard(10, 250)
    b = Boss(13, 8)
    print(w.is_dead)
    print(b.is_dead)


def main():
    test1()


if __name__ == '__main__':
    main()
