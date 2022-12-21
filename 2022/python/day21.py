
from operator import add, sub, mul, floordiv

from help import get_input

TEST = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''


OP = {
    '/': floordiv,
    '+': add,
    '-': sub,
    '*': mul
}

def parse(s):
    result = {}
    for line in s.split('\n'):
        parts = line.split(' ')
        name = parts[0][:-1]
        if len(parts) == 2:
            result[name] = int(parts[1])
        else:
            name1 = parts[1]
            op = OP[parts[2]]
            name2 = parts[3]
            assert name1.isalpha()
            assert name2.isalpha()
            result[name] = (op, name1, name2)
    return result


def evaluate(monkey, monkeys):
    result = monkeys[monkey]
    if isinstance(result, int):
        return result
    if isinstance(result, tuple):
        op, n1, n2 = result
        return op(evaluate(n1, monkeys), evaluate(n2, monkeys))
    else:
        raise ValueError


def test(humn, monkeys):
    monkeys['humn'] = humn
    _, m1, m2 = monkeys['root']
    m1 = evaluate(m1, monkeys)
    m2 = evaluate(m2, monkeys)
    if m1 < m2:
        return -1
    elif m1 > m2:
        return 1
    else:
        return 0


def part2(monkeys):
    lower = -5589789975037200
    upper = 5589789975037200
    while lower < upper:
        n = (upper + lower) // 2
        t = test(n, monkeys)
        if t < 0:
            upper = n - 1
        elif t > 0:
            lower = n + 1
        else:
            return n


def main():
    s = get_input('21')
    # s = TEST.strip()
    monkeys = parse(s)

    p1 = evaluate('root', monkeys)
    p2 = part2(monkeys)

    print('Part 1:', p1)
    print('Part 2:', p2)


if __name__ == '__main__':
    main()
