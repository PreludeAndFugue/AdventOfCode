
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


def main():
    s = get_input('21')
    # s = TEST.strip()
    monkeys = parse(s)

    p1 = evaluate('root', monkeys)
    print('Part 1:', p1)


if __name__ == '__main__':
    main()
