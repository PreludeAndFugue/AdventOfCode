'''
Too high: 9636715593780
'''


from help import get_input
from functools import reduce
from operator import add, mul

TEST01 = '''123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  '''

source = TEST01
source = get_input(6)


def part1() -> int:
    lines: list[list[str]] = []
    for line in source.split('\n'):
        lines.append(line.split())
    transposed = list(zip(*lines))
    total = 0
    for line in transposed:
        l = len(line)
        op = add if line[l - 1] == '+' else mul
        initial = 0 if line[l - 1] == '+' else 1
        ns = list(map(int, line[:l - 1]))
        t = reduce(op, ns, initial)
        total += t
    return total


def part2():
    lines = source.split('\n')
    l = max(len(line) for line in lines)
    lines = [line + ' '*(l - len(line)) for line in lines]
    lines = [list(s) for s in lines]
    for l in lines:
        l.reverse()
    transposed = list(zip(*lines))

    stack = []
    total = 0
    for row in transposed:
        last = row[-1]
        n = ''.join(row[:-1]).strip()
        if n == '':
            continue
        n = int(n)
        stack.append(n)
        if last != ' ':
            op = add if last == '+' else mul
            initial = 0 if last == '+' else 1
            t = reduce(op, stack, initial)
            total += t
            stack = []
    return total


if __name__ == '__main__':
    p1 = part1()
    print(p1)
    p2 = part2()
    print(p2)
