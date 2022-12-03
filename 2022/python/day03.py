from help import get_input

d = '03'

TEST = '''
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''


def priority(ch):
    if ch.islower():
        return ord(ch) - 96
    else:
        return ord(ch) - 38


def part1(parts):
    total = 0
    for part in parts:
        l = len(part) // 2
        p1 = part[:l]
        p2 = part[l:]
        s = set(p1) & set(p2)
        total += priority(s.pop())
    return total


def part2(parts):
    total = 0
    collection = []
    for i, part in enumerate(parts):
        collection.append(part)
        if i % 3 == 2:
            s1 = set(collection[0])
            s1 = s1.intersection(*collection[1:])
            total += priority(s1.pop())
            collection = []
    return total


def main():
    s = get_input(d).split('\n')
    # s = TEST.strip().split('\n')
    p1 = part1(s)
    p2 = part2(s)

    print('Part 1:', p1)
    print('Part 2:', p2)


if __name__ == '__main__':
    main()
