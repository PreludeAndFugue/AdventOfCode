
import sys

class IntcodeError(Exception):
    pass


class IntcodeComputer(object):
    def __init__(self, program):
        self.memory = program
        self.pointer = 0


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
            elif opcode_n == 99:
                break
            else:
                raise IntcodeError


    def _add(self, mode1, mode2, mode3):
        '''Opcode 1'''
        assert mode3 == 0
        p1 = self.memory[self.pointer + 1]
        p2 = self.memory[self.pointer + 2]
        p3 = self.memory[self.pointer + 3]
        n1 = self.memory[p1] if mode1 == 0 else p1
        n2 = self.memory[p2] if mode2 == 0 else p2
        n = n1 + n2
        self.memory[p3] = n
        self.pointer += 4


    def _multiply(self, mode1, mode2, mode3):
        '''Opcode 2'''
        assert mode3 == 0
        p1 = self.memory[self.pointer + 1]
        p2 = self.memory[self.pointer + 2]
        p3 = self.memory[self.pointer + 3]
        n1 = self.memory[p1] if mode1 == 0 else p1
        n2 = self.memory[p2] if mode2 == 0 else p2
        n = n1 * n2
        self.memory[p3] = n
        self.pointer += 4


    def _input(self, mode1, mode2, mode3):
        '''Opcode 3'''
        assert mode1 == 0 and mode2 == 0 and mode3 == 0
        n = int(sys.stdin.readline().strip())
        p1 = self.memory[self.pointer + 1]
        self.memory[p1] = n
        self.pointer += 2


    def _output(self, mode1, mode2, mode3):
        '''Opcode 4'''
        assert mode2 == 0 and mode3 == 0
        p1 = self.memory[self.pointer + 1]
        n = self.memory[p1] if mode1 == 0 else p1
        sys.stdout.write(f'{n}\n')
        self.pointer += 2


    def _jump_if_true(self, mode1, mode2, mode3):
        '''Opcode 5'''
        assert mode3 == 0
        p1 = self.memory[self.pointer + 1]
        n = self.memory[p1] if mode1 == 0 else p1
        if n != 0:
            p2 = self.memory[self.pointer + 2]
            new_p = self.memory[p2] if mode2 == 0 else p2
            self.pointer = new_p
        else:
            self.pointer += 3


    def _jump_if_false(self, mode1, mode2, mode3):
        '''Opcode 6'''
        assert mode3 == 0
        p1 = self.memory[self.pointer + 1]
        n = self.memory[p1] if mode1 == 0 else p1
        if n == 0:
            p2 = self.memory[self.pointer + 2]
            new_p = self.memory[p2] if mode2 == 0 else p2
            self.pointer = new_p
        else:
            self.pointer += 3


    def _less_than(self, mode1, mode2, mode3):
        '''Opcode 7'''
        assert mode3 == 0
        p1 = self.memory[self.pointer + 1]
        p2 = self.memory[self.pointer + 2]
        p3 = self.memory[self.pointer + 3]
        n1 = self.memory[p1] if mode1 == 0 else p1
        n2 = self.memory[p2] if mode2 == 0 else p2
        self.memory[p3] = 1 if n1 < n2 else 0
        self.pointer += 4


    def _equals(self, mode1, mode2, mode3):
        '''Opcode 8'''
        assert mode3 == 0
        p1 = self.memory[self.pointer + 1]
        p2 = self.memory[self.pointer + 2]
        p3 = self.memory[self.pointer + 3]
        n1 = self.memory[p1] if mode1 == 0 else p1
        n2 = self.memory[p2] if mode2 == 0 else p2
        self.memory[p3] = 1 if n1 == n2 else 0
        self.pointer += 4
