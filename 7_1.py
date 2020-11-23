#!python3

'''Day 7, part 1.

For part 2 change value for b to the answer to part 1.
    956 ->b

'''

import data_7


def part1():
    data = data_7.data_dict
    result = data['a'].run(data)
    print(result)
    return result


def part2(result):
    data = data_7.fresh_data()
    instruction_b = data_7.Instruction(data_7.NOOP, result, None)
    data['b'] = instruction_b
    result = data['a'].run(data)
    print(result)


if __name__ == '__main__':
    result = part1()

    part2(result)
