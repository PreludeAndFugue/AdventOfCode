#!python3

'''Data for day 23.'''

from collections import defaultdict

INPUT = '''set b 65
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23'''


INPUT_2 = '''set b 106500
set c 123500
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -6'''


def parse_input(input):
    '''Parse input string.'''
    return list(parse_row(row.strip()) for row in input.strip().split('\n'))


def parse_row(row):
    '''Parse input row.'''
    cmd, *parts = row.split(' ')
    parts = [part if part.isalpha() else int(part) for part in parts]
    parts.insert(0, cmd)
    return parts



class Program(object):

    def __init__(self, instructions, registers):
        self.instructions = instructions
        self.registers = registers
        self.position = 0
        self.mul_count = 0


    def run(self):
        '''Run the program.'''
        while True:
            if self.position < 0 or self.position >= len(self.instructions):
                print(f'break: position out of bounds.')
                break

            instruction = self.instructions[self.position]
            print(self.position, instruction)
            self._do_cmd(instruction)

            print(self.registers)

            # self.value_of_h(instruction)

            # input()


    def next(self):
        self.position += 1


    def _check_alpha(self, value):
        '''Check if value is alpha, then find numeric value.'''
        if isinstance(value, int):
            return value
        return self.registers[value]


    def _do_cmd(self, instruction):
        cmd_name = 'cmd_' + instruction[0]
        getattr(self, cmd_name)(*instruction[1:])


    def cmd_set(self, register, value):
        '''Set command.'''
        value = self._check_alpha(value)
        self.registers[register] = value
        self.next()


    def cmd_sub(self, register, value):
        '''Sub command.'''
        value = self._check_alpha(value)
        current_value = self.registers[register]
        self.registers[register] = current_value - value
        self.next()


    def cmd_mul(self, register, value):
        '''Multiply command.'''
        self.mul_count += 1
        value = self._check_alpha(value)
        current_value = self.registers[register]
        self.registers[register] = current_value * value
        self.next()


    def cmd_jnz(self, register, value):
        '''Jump command.'''
        jump_value = self._check_alpha(value)
        register_value = self._check_alpha(register)
        if register_value != 0:
            self.position += jump_value
        else:
            self.next()


    def value_of_h(self, instruction):
        register = instruction[1]
        if register == 'h':
            print(self.registers['h'])
            input()


instructions = parse_input(INPUT)
instructions2 = parse_input(INPUT_2)
