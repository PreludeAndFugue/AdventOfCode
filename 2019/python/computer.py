class IntcodeError(Exception):
    pass


class IntcodeComputer(object):
    def __init__(self, program):
        self.memory = program
        self.pointer = 0


    def run(self):
        while True:
            opcode = self.memory[self.pointer]
            if opcode == 1:
                self._add()
            elif opcode == 2:
                self._multiply()
            elif opcode == 99:
                break
            else:
                raise IntcodeError


    def _add(self):
        p1 = self.memory[self.pointer + 1]
        p2 = self.memory[self.pointer + 2]
        p3 = self.memory[self.pointer + 3]
        n1 = self.memory[p1]
        n2 = self.memory[p2]
        n = n1 + n2
        self.memory[p3] = n
        self.pointer += 4


    def _multiply(self):
        p1 = self.memory[self.pointer + 1]
        p2 = self.memory[self.pointer + 2]
        p3 = self.memory[self.pointer + 3]
        n1 = self.memory[p1]
        n2 = self.memory[p2]
        n = n1 * n2
        self.memory[p3] = n
        self.pointer += 4
