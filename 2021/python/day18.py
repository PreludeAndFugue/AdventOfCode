#!python3

from itertools import permutations
from math import ceil

from helpers import BASE

TEST01 = '''[[[[[9,8],1],2],3],4]'''
TEST02 = '''[7,[6,[5,[4,[3,2]]]]]'''
TEST03 = '''[[6,[5,[4,[3,2]]]],1]'''
TEST04 = '''[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'''

TEST05 = '''[[1,9],[8,5]]'''

TEST06 = '''[1,1]
[2,2]
[3,3]
[4,4]'''

TEST07 = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]'''

TEST08 = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''

TEST09 = '''[1,1]
[2,2]
[3,3]
[4,4]
[5,5]'''

TEST10 = '''[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]'''


def explode(string):
    stack = []
    test = iter(string)
    depth = 0

    # Find the first pair at depth 4.
    while True:
        try:
            x = next(test)
        except StopIteration:
            # Couldn't find any depth 4 pairs.
            return string, False
        if x == '[':
            if depth == 4:
                break
            depth += 1
        elif x == ']':
            depth -= 1
        elif x.isdigit():
            if stack[-1].isdigit():
                x = stack.pop() + x
        stack.append(x)

    # Parse the numbers in the pair at depth 4.
    left = 0
    while True:
        l = next(test)
        if l.isdigit():
            left = 10 * left + int(l)
        else:
            break
    right = 0
    while True:
        r = next(test)
        if r.isdigit():
            right = 10 * right + int(r)
        else: break

    # Add the left number of the pair to the first number
    # before the pair.
    for i in range(len(stack) - 1, -1, -1):
        c = stack[i]
        if c.isdigit():
            n = int(c) + left
            stack[i] = str(n)
            break

    # Replace the pair with '0'.
    stack.append('0')

    # Add the right number of the pair to the first number
    # after the pair.
    x = ''
    for c in test:
        if c.isdigit():
            x += c
        else:
            if x != '':
                n = int(x) + right
                stack.append(str(n))
                stack.append(c)
                break
            else:
                stack.append(c)

    for c in test:
        stack.append(c)

    return ''.join(stack), True


def split(string):
    stack = []
    test = iter(string)
    did_split = False
    for c in test:
        if c.isdigit():
            if stack[-1].isdigit():
                previous = stack.pop()
                n = int(previous + c)
                stack.append('[')
                stack.append(str(n // 2))
                stack.append(',')
                stack.append(str(int(ceil(n / 2))))
                stack.append(']')
                did_split = True
                break
            else:
                stack.append(c)
        else:
            stack.append(c)
    result = ''.join(stack) + ''.join(test)
    return result, did_split


def reduce(string):
    should_repeat = True
    while should_repeat:
        while should_repeat:
            string, should_repeat = explode(string)
        string, should_repeat = split(string)
    return string


def magnitude(string):
    def _magnitude(pairs):
        left = pairs[0]
        right = pairs[1]
        if isinstance(left, int):
            if isinstance(right, int):
                return 3 * left + 2 * right
            else:
                return 3 * left + _magnitude(right)
        else:
            if isinstance(right, int):
                return 3 * _magnitude(left) + 2 * right
            else:
                return 3 * _magnitude(left) + 2 * _magnitude(right)

    pairs = eval(string)
    return _magnitude(pairs)


def add(left, right):
    return f'[{left},{right}]'


def add_reduce(left, right):
    return reduce(add(left, right))


def add_reduce_n(string):
    numbers = string.strip().split('\n')
    n = numbers[0]
    for m in numbers[1:]:
        n = add_reduce(n, m)
    return n


def part1(string):
    n = add_reduce_n(string)
    return magnitude(n)


def part2(string):
    ns = string.strip().split('\n')
    largest_magnitude = 0
    for n, m in permutations(ns, 2):
        x = add_reduce(n, m)
        m = magnitude(x)
        largest_magnitude = max(largest_magnitude, m)
    return largest_magnitude


def main():
    t1, did_explode = explode(TEST01)
    assert t1 == '[[[[0,9],2],3],4]'
    assert did_explode

    t2, did_explode = explode(TEST02)
    assert t2 == '[7,[6,[5,[7,0]]]]'
    assert did_explode

    t3, did_explode = explode(TEST03)
    assert t3 == '[[6,[5,[7,0]]],3]'
    assert did_explode

    t4, did_explode = explode(TEST04)
    assert t4 == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
    assert did_explode

    t5, did_explode = explode('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
    assert t5 == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'
    assert did_explode

    t6, did_explode = explode('[1,2]')
    assert t6 == '[1,2]'
    assert not did_explode

    t7, did_explode = explode('[[1,2],3]')
    assert t7 == '[[1,2],3]'
    assert not did_explode

    t8, did_explode = explode('[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]')
    assert t8 == '[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]'
    assert not did_explode

    t9 = magnitude('[9,1]')
    assert t9 == 29

    t10 = magnitude('[1,9]')
    assert t10 == 21

    t11 = magnitude('[[9,1],[1,9]]')
    assert t11 == 129

    t12 = magnitude('[[1,2],[[3,4],5]]')
    assert t12 == 143

    t13 = magnitude('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
    assert t13 == 1384

    t14 = magnitude('[[[[1,1],[2,2]],[3,3]],[4,4]]')
    assert t14 == 445

    t15 = magnitude('[[[[3,0],[5,3]],[4,4]],[5,5]]')
    assert t15 == 791

    t16 = magnitude('[[[[5,0],[7,4]],[5,5]],[6,6]]')
    assert t16 == 1137

    t17 = magnitude('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')
    assert t17 == 3488

    t18, did_split = split('[[[[0,7],4],[15,[0,13]]],[1,1]]')
    assert t18 == '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'
    assert did_split == True

    t19, did_split = split('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]')
    assert t19 == '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'
    assert did_split == True

    t20, did_split = split('[[1,2],[[3,4],5]]')
    assert t20 == '[[1,2],[[3,4],5]]'
    assert did_split == False

    t21, did_split = split('[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]')
    assert t21 == '[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]'
    assert did_split == False

    t22 = add('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]')
    assert t22 == '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'

    t23 = reduce('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
    assert t23 == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'

    t24 = add_reduce('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]')
    assert t24 == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'

    t26 = add_reduce_n(TEST07)
    assert t26 == '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'

    t27 = add_reduce_n(TEST08)
    assert t27 == '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'

    t28 = part1(TEST07)
    assert t28 == 3488

    t29 = part1(TEST08)
    assert t29 == 4140

    input_string = open(BASE + 'day18.txt', 'r').read()

    p1 = part1(input_string)
    print(f'Part 1: {p1}')

    t30 = part2(TEST08)
    assert t30 == 3993

    p2 = part2(input_string)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
