#!python3

from helpers import BASE

TEST01 = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''


class InvalidLine(ValueError):
    pass


OPEN = '([{<'
CLOSE = ')]}>'
POINTS1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
POINTS2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def parse_line(line):
    stack = []
    for x in line:
        if x in OPEN:
            stack.append(x)
        elif x in CLOSE:
            y = stack.pop()
            i = OPEN.index(y)
            j = CLOSE.index(x)
            if i != j:
                raise InvalidLine(x)
    return stack


def score_2(stack):
    items = [MAP[x] for x in reversed(stack)]
    score = 0
    for x in items:
        score *= 5
        score += POINTS2[x]
    return score


def part1(lines):
    invalid_close = []
    for line in lines:
        try:
            _ = parse_line(line)
        except InvalidLine as error:
            invalid_close.append(str(error))
    return sum(POINTS1[a] for a in invalid_close)


def part2(lines):
    incomplete = []
    for line in lines:
        try:
            stack = parse_line(line)
            incomplete.append(stack)
        except InvalidLine:
            pass
    scores = sorted(score_2(s) for s in incomplete)
    return scores[len(scores) // 2]


def main():
    test_lines = TEST01.strip().split('\n')
    lines = open(BASE + 'day10.txt', 'r').read().strip().split('\n')

    t1 = part1(test_lines)
    assert t1 == 26397

    p1 = part1(lines)
    print(f'Part 1: {p1}')

    t2 = part2(test_lines)
    assert t2 == 288957

    p2 = part2(lines)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
