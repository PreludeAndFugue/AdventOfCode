#!python3

'''Day 7, part 1.'''

import data_7


def find_base(programs):
    '''Find the program at the base of the tower.'''
    program_names = set(program.name for program in programs)
    for program in programs:
        program_names = program_names - set(program.children)
    return program_names.pop()


def main():
    '''Main entry point.'''
    data = data_7.data
    name = find_base(data)
    print(name)


if __name__ == '__main__':
    main()
