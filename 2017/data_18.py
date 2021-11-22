#!python3

'''Data for day 18.'''

from collections import defaultdict

INPUT = '''set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 618
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19'''


TEST_INPUT = '''snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d'''


def parse_input(input):
    '''Parse input string.'''
    return list(parse_row(row.strip()) for row in input.strip().split('\n'))


def parse_row(row):
    '''Parse input row.'''
    cmd, *parts = row.split(' ')
    parts = [part if part.isalpha() else int(part) for part in parts]
    parts.insert(0, cmd)
    return parts


def _check_alpha(value, program):
    '''Check if value is alpha, then find numeric value.'''
    if isinstance(value, int):
        return value
    return program.registers[value]


def cmd_snd(program, value):
    '''Sound command.'''
    value = _check_alpha(value, program)
    program.sound(value)
    program.next()


def cmd_snd2(program, value):
    '''Send message.'''
    value = _check_alpha(value, program)
    other_program_number = 1 if program.number == 0 else 0
    program.queues[other_program_number].append(value)
    program.send_count += 1
    program.next()

    # print(program.queues)
    # input()


def cmd_set(program, register, value):
    '''Set command.'''
    value = _check_alpha(value, program)
    program.registers[register] = value
    program.next()


def cmd_add(program, register, value):
    '''Add command.'''
    value = _check_alpha(value, program)
    current_value = program.registers[register]
    program.registers[register] = current_value + value
    program.next()


def cmd_mul(program, register, value):
    '''Multiply command.'''
    value = _check_alpha(value, program)
    current_value = program.registers[register]
    program.registers[register] = current_value * value
    program.next()


def cmd_mod(program, register, value):
    '''Modulus command.'''
    value = _check_alpha(value, program)
    current_value = program.registers[register]
    program.registers[register] = current_value % value
    program.next()


def cmd_rcv(program, register):
    '''Recover command.'''
    value = program.registers[register]
    print('cmd: rcv - stop')
    if value:
        program.stop()


def cmd_rcv2(program, register):
    '''Receive a message.'''
    # print('receive', program.number)
    if not program.queues[program.number]:
        program.nothing_to_receive = True
        # print('nothing to receive')
        return
    value = program.queues[program.number].pop(0)
    program.registers[register] = value
    program.next()


def cmd_jgz(program, register, value):
    '''Jump command.'''
    jump_value = _check_alpha(value, program)
    register_value = _check_alpha(register, program)
    # register_value = program.registers[register]
    if register_value > 0:
        program.position += jump_value
    else:
        program.position += 1


class Program(object):
    '''The program.'''

    CMDS = {
        'snd': cmd_snd,
        'set': cmd_set,
        'add': cmd_add,
        'mul': cmd_mul,
        'mod': cmd_mod,
        'rcv': cmd_rcv,
        'jgz': cmd_jgz
    }


    def __init__(self, instructions):
        self.last_sound_freq = None
        self.position = 0
        self.registers = defaultdict(int)
        self.instructions = instructions
        self.running = True


    def run(self):
        '''Run the program.'''
        while self.running:
            if self.position < 0 or self.position >= len(self.instructions):
                print('break: position out of bounds')
                break
            instruction = self.instructions[self.position]
            cmd = Program.CMDS[instruction[0]]

            # print('run', self.position, instruction, self.registers)
            # input()

            cmd(self, *instruction[1:])


    def sound(self, value):
        '''Play sound.'''
        self.last_sound_freq = value


    def next(self):
        self.position += 1


    def stop(self):
        self.running = False


class Program2(object):
    '''Program for part 2.'''

    CMDS = {
        'snd': cmd_snd2,
        'set': cmd_set,
        'add': cmd_add,
        'mul': cmd_mul,
        'mod': cmd_mod,
        'rcv': cmd_rcv2,
        'jgz': cmd_jgz
    }

    def __init__(self, n, instructions, queues):
        self.number = n
        self.queue = []
        self.position = 0
        self.registers = defaultdict(int)
        self.registers['p'] = n
        self.instructions = instructions
        self.queues = queues
        self.send_count = 0
        self.nothing_to_receive = False
        self.running = True


    def run(self):
        '''Run the program.'''
        while self.running:
            self.nothing_to_receive = False

            if self.position < 0 or self.position >= len(self.instructions):
                self.running = False
                print(f'break {self.number}: position out of bounds')
                break

            instruction = self.instructions[self.position]
            cmd = Program2.CMDS[instruction[0]]

            # print('run:', self.number, self.position, instruction, self.registers)
            # input()

            cmd(self, *instruction[1:])
            if self.nothing_to_receive:
                break


    def next(self):
        self.position += 1


    def stop(self):
        self.running = False


instructions = parse_input(INPUT)
test_instructions = parse_input(TEST_INPUT)
