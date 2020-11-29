#!python3


INPUT = 3_014_387


class Elf(object):
    def __init__(self, position):
        self.position = position
        self.next = None


    def steal(self):
        # print(self.position, 'stealing from', self.next.position)
        after_next = self.next.next
        if after_next.position == self.position:
            self.next = None
        else:
            self.next = after_next


    def __repr__(self):
        n = '?' if self.next is None else self.next.position
        return f'Elf({self.position}, next: {n})'


def make_ring(n):
    elfs = [Elf(i) for i in range(1, n + 1)]
    for e1, e2 in zip(elfs, elfs[1:] + [elfs[0]]):
        e1.next = e2
    return elfs


def part1():
    elfs = make_ring(INPUT)
    elf = elfs[0]
    while True:
        elf.steal()
        if elf.next is None:
            break
        elf = elf.next
    return elf.position



def main():
    p = part1()
    print(p)


if __name__ == '__main__':
    main()
