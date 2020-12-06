#!python3

INPUT = 'day06.txt'
TEST_INPUT = '''abc

a
b
c

ab
ac

a
a
a
a

b'''


def part1(input):
    total = 0
    for group in input.split('\n\n'):
        answers = set()
        for line in group.split('\n'):
            answers.update(list(line.strip()))
        total += len(answers)
    return total


def main():
    assert part1(TEST_INPUT) == 11

    p = part1(open(INPUT, 'r').read())
    print(p)



if __name__ == "__main__":
    main()
