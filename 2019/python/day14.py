#!python3

from collections import defaultdict

from helpers import BASE

ORE = 'ORE'
FUEL = 'FUEL'

TEST01 = '''10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL'''


TEST02 = '''9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL'''


TEST03 = '''157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT'''


TEST04 = '''2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF'''


TEST05 = '''171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX'''

'''
{'BHXH': 3048, 'KTJDG': 3201, 'VRPVC': 32981, 'CNZTR': 69552}
3048 / 4 = 762 -> 762 * 114 = 86,868
3201 / 9 = 355.7 -> 356 -> 356 * 189 = 67,284
32981 / 7 = 4711.6 -> 4712 -> 4712 * 121 = 570,152
69552 / 8 = 8,694 -> 8,694 * 171 = 1,486,674

total = 2,210,978
'''


def parse(string):
    mapping = {}
    for line in string.strip().split('\n'):
        lhs, rhs = line.split(' => ')
        r1, r2 = rhs.split(' ')
        left = defaultdict(int)
        for l in lhs.split(', '):
            l1, l2 = l.split(' ')
            left[l2] = int(l1)
        mapping[r2, int(r1)] = left
    return mapping


def test1():
    m1 = parse(TEST01)
    t1 = part1(m1)
    assert t1 == 31

    m2 = parse(TEST02)
    t2 = part1(m2)
    assert t2 == 165

    m3 = parse(TEST03)
    t3 = part1(m3)
    assert t3 == 13312

    m4 = parse(TEST04)
    assert part1(m4) == 180697

    m5 = parse(TEST05)
    assert part1(m5) == 2210736


def reaction_has_chemicals(reaction):
    '''Do any chemicals in the fuel reaction have positive amounts.'''
    for chemical, amount in reaction.items():
        if chemical != ORE and amount > 0:
            return True
    return False


def get_chemicals(reaction):
    '''Get the chemicals from the fuel recation that have a positive amount.'''
    for chemical, amount in reaction.items():
        if chemical != ORE and amount > 0:
            yield chemical


def get_reaction_for_chemical(chemical, reactions):
    '''Get a reaction which has the chemical on the lhs.'''
    for (ch, amount), reaction in reactions.items():
        if ch == chemical:
            return amount, reaction
    return None


def part1(reactions):
    fuel = reactions.pop(('FUEL', 1))
    while reaction_has_chemicals(fuel):
        for chemical in get_chemicals(fuel):
            amount, reaction = get_reaction_for_chemical(chemical, reactions)
            if reaction is None:
                continue
            fuel[chemical] -= amount
            for ch, amount in reaction.items():
                fuel[ch] += amount
            break
    return fuel['ORE']


def main():
    test1()

    mapping = parse(open(BASE + 'day14.txt', 'r').read())
    p1 = part1(mapping)
    print(f'Part 1: {p1}')


if __name__ == '__main__':
    main()
