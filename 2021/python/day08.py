#!python3

from itertools import chain, permutations

from helpers import BASE


TEST01 = '''
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''

TEST02 = '''acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'''


NUMBERS = {
    'cf': 1,

    'acf': 7,

    'bcdf': 4,

    'acdeg': 2,
    'acdfg': 3,
    'abdfg': 5,

    'abcefg': 0,
    'abdefg': 6,
    'abcdfg': 9,

    'abcdefg': 8,
}


def parse(string):
    for line in string.strip().split('\n'):
        patterns, value = line.split(' | ')
        yield patterns.split(), value.split()


def part1(all_values):
    count = 0
    for value in all_values:
        l = len(value)
        if l == 2 or l == 3 or l == 4 or l == 7:
            count += 1
    return count


def solve_patterns(patterns):
    numbers = {
        1: [set(p) for p in patterns if len(p) == 2][0],
        7: [set(p) for p in patterns if len(p) == 3][0],
        4: [set(p) for p in patterns if len(p) == 4][0],
        235: [set(p) for p in patterns if len(p) == 5],
        609: [set(p) for p in patterns if len(p) == 6]
    }
    def remove_letter(numbers, x):
        for number in numbers.keys():
            numbers[number] = numbers[number] - set(x)
    for two, three, five in permutations(numbers[235], 3):
        for six, zero, nine in permutations(numbers[609], 3):
            test_numbers = {
                1: numbers[1],
                7: numbers[7],
                4: numbers[4],
                2: two,
                3: three,
                5: five,
                6: six,
                0: zero,
                9: nine,
            }
            # print(test_numbers)
            a = test_numbers[7] - test_numbers[1]
            remove_letter(test_numbers, a)
            g = test_numbers[9] - a - test_numbers[4]
            remove_letter(test_numbers, g)
            d = test_numbers[3] - test_numbers[1] - a - g
            remove_letter(test_numbers, d)
            e = test_numbers[0] - test_numbers[9]
            remove_letter(test_numbers, e)
            c = test_numbers[2]
            remove_letter(test_numbers, c)
            f = test_numbers[1]
            remove_letter(test_numbers, f)
            b = test_numbers[0]
            result = {
                'a': a,
                'g': g,
                'd': d,
                'e': e,
                'c': c,
                'f': f,
                'b': b,
            }
            x = all(True if len(v) == 1 else False for v in result.values())
            if x:
                return {v.pop(): k for k, v in result.items()}
    raise ValueError('no match')


def part2(data):
    total = 0
    for patterns, values in data:
        solution = solve_patterns(patterns)
        translation = str.maketrans(solution)
        fixed_values = [''.join(sorted(s.translate(translation))) for s in values]
        numbers = [NUMBERS[f] for f in fixed_values]
        n = sum(n * 10 ** i for i, n in enumerate(reversed(numbers)))
        total += n
    return total


def main():
    test_data = list(parse(TEST01))
    all_test_values = list(chain.from_iterable(x[1] for x in test_data))

    data = list(parse(open(BASE + 'day08.txt', 'r').read()))
    all_values = list(chain.from_iterable(x[1] for x in data))

    t1 = part1(all_test_values)
    assert t1 == 26

    p1 = part1(all_values)
    print(f'Part 1: {p1}')

    t2 = part2(test_data)
    assert t2 == 61229

    p2 = part2(data)
    print(f'Part 2 {p2}')


if __name__ == '__main__':
    main()
