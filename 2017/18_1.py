#!python3

'''Day 18, part 1.'''

from data_18 import instructions, Program


if __name__ == '__main__':
    program = Program(instructions)
    program.run()

    print(program.last_sound_freq)