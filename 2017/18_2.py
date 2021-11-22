#!python3

'''Day 18, part 2.'''

from data_18 import instructions, test_instructions, Program2


def can_run(program0, program1, queuen):
    '''Check that programs can keep running.'''
    if not program0.running and not program1.running:
        return False
    if empty_queues(queues) and program0.nothing_to_receive and program1.nothing_to_receive:
        return False
    return True


def empty_queues(queues):
    '''Are both queues empty.'''
    return not queues[0] and not queues[1]


if __name__ == '__main__':
    queues = {
        0: [],
        1: []
    }
    program0 = Program2(0, instructions, queues)
    program1 = Program2(1, instructions, queues)

    while can_run(program0, program1, queues):
        program0.run()
        program1.run()

    print(program1.send_count)
