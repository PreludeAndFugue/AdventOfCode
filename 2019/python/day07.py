#!python3

from itertools import permutations

from computer import IntcodeComputer, Console
from helpers import BASE


TEST01 = '''3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'''
TEST02 = '''3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'''
TEST03 = '''3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'''


def amp(program, phases):
    console = Console([])
    amps = [IntcodeComputer(program.copy(), console) for _ in range(5)]
    _output = 0

    for amp, phase in zip(amps, phases):
        console.write(phase)
        console.write(_output)
        amp.run()
        _output = console.readline()

    return _output


def find_max(program):
    results = []
    for perm in permutations('01234'):
        a = amp(program, perm)
        results.append(int(a))
    return max(results)


def test1():
    test_program_1 = list(map(int, TEST01.strip().split(',')))
    test_program_2 = list(map(int, TEST02.strip().split(',')))
    test_program_3 = list(map(int, TEST03.strip().split(',')))

    t1 = find_max(test_program_1)
    assert t1 == 43210

    t2 = find_max(test_program_2)
    assert t2 == 54321

    t3 = find_max(test_program_3)
    assert t3 == 65210


def main():
    program = list(map(int, open(BASE + 'day07.txt', 'r').read().strip().split(',')))

    p1 = find_max(program)
    print(f'Part 1: {p1}')


if __name__ == '__main__':
    main()
