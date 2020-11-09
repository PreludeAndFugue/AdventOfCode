#!python3

'''
The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant.

The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
'''

SOURCE = [
    [],
    ['Pr-G', 'Pr-M', 'Ru-G', 'Ru-M'],
    ['Pl-M', 'St-M'],
    ['Th-G', 'Th-M', 'Pl-G', 'St-G']
]

TEST = [
    [],
    ['L-G'],
    ['H-G'],
    ['H-M', 'L-M']
]

TEST1 = [
    ('L-G', 3),
    ('H-G', 2),
    ('H-M', 1), ('L-M', 1)
]

TEST2 = {
    4: (),
    3: ('L-G',),
    2: ('H-G',),
    1: ('H-M', 'L-M')
}

TEST3 = '''
4---
3--LG
2--HG
1-E-HM-LM
'''


def distance(items):
    d = 0
    for _, floor in items:
        d += (4 - floor)
    return d


def valid_moves(items):
    pass


def test():
    print(TEST2)
    x = set([TEST2])
    print(distance(TEST1))


if __name__ == '__main__':
    test()
