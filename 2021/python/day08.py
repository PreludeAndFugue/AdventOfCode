#!python3

from itertools import chain

from helpers import BASE


TEST01 = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
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


def main():
    test_data = list(parse(TEST01))
    all_test_values = list(chain.from_iterable(x[1] for x in test_data))

    data = list(parse(open(BASE + 'day08.txt', 'r').read()))
    all_values = list(chain.from_iterable(x[1] for x in data))

    t1 = part1(all_test_values)
    assert t1 == 26

    p1 = part1(all_values)
    print(f'Part 1: {p1}')


if __name__ == '__main__':
    main()
