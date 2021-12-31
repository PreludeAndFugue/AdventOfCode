
from collections import defaultdict


MODE_POSITION = 0
MODE_IMMEDIATE = 1
MODE_RELATIVE = 2


def read_program(file_path):
    return list(map(int, open(file_path, 'r').read().strip().split(',')))


class IntcodeError(Exception):
    pass


class IntcodeComputer(object):
    def __init__(self, program, console):
        memory = defaultdict(int)
        for i, n in enumerate(program):
            memory[i] = n
        self.memory = memory
        self.console = console
        self.pointer = 0
        self.relative_base = 0


    def run(self):
        while True:
            opcode = self.memory[self.pointer]
            # print('opcode', opcode)
            opcode_n = opcode % 100
            mode1 = (opcode // 100) % 10
            mode2 = (opcode // 1000) % 10
            mode3 = (opcode // 10000) % 10
            if opcode_n == 1:
                self._add(mode1, mode2, mode3)
            elif opcode_n == 2:
                self._multiply(mode1, mode2, mode3)
            elif opcode_n == 3:
                self._input(mode1, mode2, mode3)
            elif opcode_n == 4:
                self._output(mode1, mode2, mode3)
            elif opcode_n == 5:
                self._jump_if_true(mode1, mode2, mode3)
            elif opcode_n == 6:
                self._jump_if_false(mode1, mode2, mode3)
            elif opcode_n == 7:
                self._less_than(mode1, mode2, mode3)
            elif opcode_n == 8:
                self._equals(mode1, mode2, mode3)
            elif opcode_n == 9:
                self._adjust_relative_base(mode1, mode2, mode3)
            elif opcode_n == 99:
                break
            else:
                raise IntcodeError


    def _add(self, mode1, mode2, mode3):
        '''Opcode 1'''
        p1 = self.memory[self.pointer + 1]
        p2 = self.memory[self.pointer + 2]
        p3 = self.memory[self.pointer + 3]
        n1 = self._get(p1, mode1)
        n2 = self._get(p2, mode2)
        n = n1 + n2
        if mode3 == MODE_RELATIVE:
            p3 += self.relative_base
        self.memory[p3] = n
        self.pointer += 4


    def _multiply(self, mode1, mode2, mode3):
        '''Opcode 2'''
        p1 = self.memory[self.pointer + 1]
        p2 = self.memory[self.pointer + 2]
        p3 = self.memory[self.pointer + 3]
        n1 = self._get(p1, mode1)
        n2 = self._get(p2, mode2)
        n = n1 * n2
        if mode3 == MODE_RELATIVE:
            p3 += self.relative_base
        self.memory[p3] = n
        self.pointer += 4


    def _input(self, mode1, mode2, mode3):
        '''Opcode 3'''
        assert mode2 == 0 and mode3 == 0
        # n = int(sys.stdin.readline().strip())
        n = int(self.console.readline().strip())
        p1 = self.memory[self.pointer + 1]
        if mode1 == MODE_RELATIVE:
            p1 += self.relative_base
        self.memory[p1] = n
        self.pointer += 2


    def _output(self, mode1, mode2, mode3):
        '''Opcode 4'''
        assert mode2 == 0 and mode3 == 0
        p1 = self.memory[self.pointer + 1]
        n = self._get(p1, mode1)
        # sys.stdout.write(f'{n}\n')
        self.console.write(f'{n}')
        self.pointer += 2


    def _jump_if_true(self, mode1, mode2, mode3):
        '''Opcode 5'''
        assert mode3 == 0
        p1 = self.memory[self.pointer + 1]
        n = self._get(p1, mode1)
        if n != 0:
            p2 = self.memory[self.pointer + 2]
            new_p = self._get(p2, mode2)
            self.pointer = new_p
        else:
            self.pointer += 3


    def _jump_if_false(self, mode1, mode2, mode3):
        '''Opcode 6'''
        assert mode3 == 0
        p1 = self.memory[self.pointer + 1]
        n = self._get(p1, mode1)
        if n == 0:
            p2 = self.memory[self.pointer + 2]
            new_p = self._get(p2, mode2)
            self.pointer = new_p
        else:
            self.pointer += 3


    def _less_than(self, mode1, mode2, mode3):
        '''Opcode 7'''
        p1 = self.memory[self.pointer + 1]
        p2 = self.memory[self.pointer + 2]
        p3 = self.memory[self.pointer + 3]
        n1 = self._get(p1, mode1)
        n2 = self._get(p2, mode2)
        if mode3 == MODE_RELATIVE:
            p3 += self.relative_base
        self.memory[p3] = 1 if n1 < n2 else 0
        self.pointer += 4


    def _equals(self, mode1, mode2, mode3):
        '''Opcode 8'''
        p1 = self.memory[self.pointer + 1]
        p2 = self.memory[self.pointer + 2]
        p3 = self.memory[self.pointer + 3]
        n1 = self._get(p1, mode1)
        n2 = self._get(p2, mode2)
        if mode3 == MODE_RELATIVE:
            p3 += self.relative_base
        self.memory[p3] = 1 if n1 == n2 else 0
        self.pointer += 4


    def _adjust_relative_base(self, mode1, mode2, mode3):
        '''Opcode 9'''
        assert mode2 == 0 and mode3 == 0
        p1 = self.memory[self.pointer + 1]
        n1 = self._get(p1, mode1)
        self.relative_base += n1
        self.pointer += 2


    def _get(self, p, mode):
        if mode == MODE_POSITION:
            return self.memory[p]
        if mode == MODE_IMMEDIATE:
            return p
        if mode == MODE_RELATIVE:
            return self.memory[p + self.relative_base]


class Console(object):
    def __init__(self, buffer):
        self.pointer = 0
        self.buffer = [str(b) for b in buffer]

    def readline(self):
        s = self.buffer[self.pointer]
        self.pointer += 1
        return s

    def write(self, s):
        self.buffer.append(str(s))


def test1():
    '''Day 9 test'''
    program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    c = Console([])
    ic = IntcodeComputer(program, c)
    ic.run()
    program1 = [int(b) for b in c.buffer]
    assert program1 == program


def test2():
    '''Day 9 test'''
    program = [1102,34915192,34915192,7,4,7,99,0]
    c = Console([])
    ic = IntcodeComputer(program, c)
    ic.run()
    x = c.readline()
    assert len(x) == 16


def test3():
    '''Day 9 test'''
    program = [104,1125899906842624,99]
    c = Console([])
    ic = IntcodeComputer(program, c)
    ic.run()
    x = c.readline()
    assert x == '1125899906842624'


def main():
    test1()
    test2()
    test3()


if __name__ == '__main__':
    main()
