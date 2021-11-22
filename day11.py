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

from itertools import chain, combinations


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


def update_state(elevator, floors):
    f_old = floors[elevator]
    for de in (-1, 1):

        # shouldn't be able to go to a state where all lower floors are empty.

        new_elevator = elevator + de
        print('new elevator: ', new_elevator)
        if new_elevator < 0 or new_elevator > 3:
            continue
        c2 = combinations(f_old, 2)
        c1 = combinations(f_old, 1)
        for c in chain(c2, c1):
            print(new_elevator, c)
            f_new = floors[new_elevator]

            f_old_update = tuple(x for x in f_old if x not in c)
            if not is_valid_floor(f_old_update):
                continue

            f_new_update = f_new + c
            if not is_valid_floor(f_new_update):
                continue

            l_floors = list(floors)
            l_floors[elevator] = f_old_update
            l_floors[new_elevator] = f_new_update
            yield (new_elevator, tuple(l_floors))


def make_repr(elevator, floors):
    f0 = '.'.join(sorted(floors[0]))
    f1 = '.'.join(sorted(floors[1]))
    f2 = '.'.join(sorted(floors[2]))
    f3 = '.'.join(sorted(floors[3]))
    return f'{elevator} | {f0} | {f1} | {f2} | {f3}'


def is_valid_floor(floor):
    # print('floor', floor)
    generators = set(x[:-2] for x in floor if x.endswith('-G'))
    chips = [x[:-2] for x in floor if x.endswith('-M')]
    # print(generators)
    # print(chips)
    for chip in chips:
        if generators and chip not in generators:
            return False
    return True


def distance(items):
    d = 0
    for _, floor in items:
        d += (4 - floor)
    return d


def test():
    f = (0, 1, 2, 3)
    f2 = combinations(f, 2)
    f1 = combinations(f, 1)
    for x in chain(f2, f1):
        print(x)


def test1():
    elevator = 0
    f0 = ('H-M', 'L-M')
    f1 = ('H-G',)
    f2 = ('L-G',)
    f3 = ()
    floors = (f0, f1, f2, f3)
    r = make_repr(elevator, floors)
    print(r)


def test2():
    elevator = 0
    f0 = ('H-M', 'L-M')
    f1 = ('H-G',)
    f2 = ('L-G',)
    f3 = ()
    floors = (f0, f1, f2, f3)
    for elevator, floors in update_state(elevator, floors):
        print(make_repr(elevator, floors))


def test3():
    elevator = 0
    f0 = ('H-M', 'L-M')
    f1 = ('H-G',)
    f2 = ('L-G',)
    f3 = ()
    floors = (f0, f1, f2, f3)
    goal_state = make_repr(4, ((), (), (), ('H-M', 'L-M', 'H-G', 'L-G')))
    print('goal state', goal_state)
    seen = set()
    to_check = [(elevator, floors)]
    while to_check:
        input()
        elevator, floors = to_check.pop()
        print('to check:', elevator, floors)
        state = make_repr(elevator, floors)
        if state == goal_state:
            print('done')
        if state in seen:
            print('state in seen - ignore')
            continue
        seen.add(state)
        for neighbour in update_state(elevator, floors):
            print('\tadd neighbour', neighbour)
            to_check.append(neighbour)


if __name__ == '__main__':
    # test()
    # test1()
    # test2()
    test3()
