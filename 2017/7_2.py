#!python3

'''Day 7, part 2.'''

from collections import defaultdict

import data_7


def calculate_weights(programs, base_program):
    '''Calculate weights of programs.'''
    # print('calculating weight for item', base_program)
    children = programs[base_program.name].children
    child_weights = 0
    for child_name in children:
        child = programs[child_name]
        child_weights += calculate_weights(programs, base_program=child)
    base_program.tower_weight = base_program.weight + child_weights
    return base_program.tower_weight


def find_wrong_weight(programs, base_program):
    '''Find program with wrong weight.

    Use levels starting from 0
    '''
    program = base_program
    while True:
        child_names = program.children
        children = [programs[name] for name in child_names]
        print(children)

        program = find_wrong_child(children)

        if program is None:
            break

        print(program)
        print('\n\n\n')


def find_wrong_child(children):
    '''Find the child with the wrong tower weight.'''
    tower_weight_counter = defaultdict(list)
    for child in children:
        tower_weight_counter[child.tower_weight].append(child)

    for weight, children in tower_weight_counter.items():
        if len(children) == 1:
            return children[0]


def main():
    '''Main entry point.'''
    programs = data_7.data
    # programs = data_7.test_data
    base_name = 'gmcrj'
    # base_name = 'tknk'

    programs_dict = {program.name: program for program in programs}
    base_program = programs_dict[base_name]

    calculate_weights(programs_dict, base_program)
    find_wrong_weight(programs_dict, base_program)


if __name__ == '__main__':
    main()
