
from help import get_input

from operator import add, mul


TEST = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''


class Monkey:
    def __init__(self, n, items, operation, test, true, false):
        self.n = n
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspect_count = 0


    def update_worry_levels(self):
        # print('update worry levels: ', end='')
        # print(self.items, end='')
        # print(' -> ', end='')
        self.items = [self.operation(item) // 3 for item in self.items]
        # print(self.items)
        self.inspect_count += len(self.items)


    def throw_items(self, monkeys):
        # print('throw')
        for item in self.items:
            if item % self.test == 0:
                # print(f'\tthrow {item} to {self.true}')
                monkeys[self.true].items.append(item)
            else:
                # print(f'\tthrow {item} to {self.false}')
                monkeys[self.false].items.append(item)
        self.items = []


    def __repr__(self):
        return f'M({self.n}, items={self.items}, op={self.operation}, test={self.test}, true={self.true}, false={self.false})'


def make_operation(s):
    parts = s.split(' ')
    operator = add if parts[1] == '+' else mul
    if parts[2] == 'old':
        return lambda x: operator(x, x)
    else:
        n = int(parts[2])
        return lambda x: operator(x, n)

def make_monkey(s):
    lines = [l.strip() for l in s.split('\n')]
    n = int(lines[0].split(' ')[1].strip(':'))
    items = list(map(int, lines[1][15:].split(', ')))
    operation = make_operation(lines[2][17:])
    test = int(lines[3].split(' ')[-1])
    true = int(lines[4].split(' ')[-1])
    false = int(lines[5].split(' ')[-1])
    return Monkey(n, items, operation, test, true, false)


def round(monkeys):
    monkey_ids = sorted(monkeys.keys())
    for id_ in monkey_ids:
        monkey = monkeys[id_]
        # print(monkey)
        monkey.update_worry_levels()
        monkey.throw_items(monkeys)


def part1(monkeys):
    for _ in range(20):
        round(monkeys)
        # input()
        # for m in monkeys.values():
            # print(m)
        # input()
    counts = list(reversed(sorted(m.inspect_count for m in monkeys.values())))[:2]
    return mul(*counts)


def main():
    s = get_input('11')
    # s = TEST
    monkeys = [make_monkey(m) for m in s.split('\n\n')]
    monkeys = {m.n: m for m in monkeys}

    p1 = part1(monkeys)
    print('Part 1:', p1)


if __name__ == '__main__':
    main()
