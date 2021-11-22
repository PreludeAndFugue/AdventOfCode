#!python3

'''
Chinese remainder theorem
'''

from math import prod
from mathshelp import chinese_remainder

INPUT = 'day13.txt'

TEST_INPUT_1 = '''939
7,13,x,x,59,x,31,19
'''
TEST_INPUT_2 = '''BLA
17,x,13,19
'''
TEST_INPUT_3 = '''BLA
67,7,59,61
'''
TEST_INPUT_4 = '''BLA
67,x,7,59,61
'''
TEST_INPUT_5 = '''BLA
67,7,x,59,61
'''
TEST_INPUT_6 = '''BLA
1789,37,47,1889
'''


def get_input1(input):
    timestamp, buses = input.strip().split('\n')
    timestamp = int(timestamp)
    buses = [int(b) for b in buses.split(',') if b != 'x']
    return timestamp, buses


def get_input2(input):
    buses = input.strip().split('\n')[1]
    buses = [(i, int(b)) for i, b in enumerate(buses.split(',')) if b != 'x']
    return buses


def wait(bus, timestamp):
    return bus - (timestamp % bus)


def _part1(timestamp, buses):
    waits = {wait(bus, timestamp): bus for bus in buses}
    min_wait = min(waits.keys())
    return waits[min_wait] * min_wait


def test1():
    timestamp, buses = get_input1(TEST_INPUT_1)
    return _part1(timestamp, buses)


def part1():
    timestamp, buses = get_input1(open(INPUT, 'r').read())
    return _part1(timestamp, buses)


def _part2(buses):
    buses = [((bus[1] - bus[0]) % bus[1], bus[1]) for bus in buses]
    return chinese_remainder(buses)


def test2():
    buses1 = get_input2(TEST_INPUT_1)
    assert _part2(buses1) == 1068781
    buses2 = get_input2(TEST_INPUT_2)
    assert _part2(buses2) == 3417
    buses3 = get_input2(TEST_INPUT_3)
    assert _part2(buses3) == 754018
    buses4 = get_input2(TEST_INPUT_4)
    assert _part2(buses4) == 779210
    buses5 = get_input2(TEST_INPUT_5)
    assert _part2(buses5) == 1261476
    buses6 = get_input2(TEST_INPUT_6)
    assert _part2(buses6) == 1202161486


def part2():
    buses = get_input2(open(INPUT, 'r').read())
    return _part2(buses)


def main():
    assert test1() == 295

    p = part1()
    print(p)

    test2()

    p = part2()
    print(p)


if __name__ == "__main__":
    main()
