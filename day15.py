#!python3

'''
Disc #1 has 13 positions; at time=0, it is at position 11.
Disc #2 has  5 positions; at time=0, it is at position  0.
Disc #3 has 17 positions; at time=0, it is at position 11.
Disc #4 has  3 positions; at time=0, it is at position  0.
Disc #5 has  7 positions; at time=0, it is at position  2.
Disc #6 has 19 positions; at time=0, it is at position 17.

Disc #1 has 13 positions; at time=1, it is at position 12.
Disc #2 has  5 positions; at time=2, it is at position  2.
Disc #3 has 17 positions; at time=3, it is at position 14.
Disc #4 has  3 positions; at time=4, it is at position  1.
Disc #5 has  7 positions; at time=5, it is at position  0.
Disc #6 has 19 positions; at time=6, it is at position  4.

TEST
----
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.

Disc #1 has 5 positions; at time=1, it is at position 0.
Disc #2 has 2 positions; at time=2, it is at position 1.
'''

class Disc(object):
    def __init__(self, positions, time, position):
        self.positions = positions
        self.time = time
        self.position = position


    def increment(self, t=1):
        self.time += t
        self.position = (self.position + t) % self.positions


    @property
    def is_open(self):
        return self.position == 0


    def __repr__(self):
        return f'Disc({self.position}, {self.positions}, t={self.time})'


DISCS = [
    (13, 11),
    (5, 0),
    (17, 11),
    (3, 0),
    (7, 2),
    (19, 17)
]

TEST_DISCS = [
    (5, 4),
    (2, 1)
]


def make_discs(disc_input):
    discs = []
    for i, d in enumerate(disc_input):
        disc = Disc(d[0], 0, d[1])
        disc.increment(i + 1)
        discs.append(disc)
    return discs


def shift_to_position_zero(discs):
    '''Shifts all discs in time so that the disc with most positions is at position 0.'''
    disc_dict = {d.positions: d for d in discs}
    n = max(disc_dict.keys())
    offset = n - disc_dict[n].position
    # print('offset', offset)
    for d in discs:
        d.increment(offset)
    return n


def offset_discs(discs, n):
    for d in discs:
        d.increment(n)


def part1():
    discs = make_discs(DISCS)
    n = shift_to_position_zero(discs)
    if all(d.is_open for d in discs):
        return discs[0].time - 1
    while True:
        offset_discs(discs, n)
        if all(d.is_open for d in discs):
            return discs[0].time - 1


def main():
    n = part1()
    print(n)


if __name__ == '__main__':
    main()
