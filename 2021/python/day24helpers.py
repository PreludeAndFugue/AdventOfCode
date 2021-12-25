#!python3

class ALU(object):
    def __init__(self, program, input_numbers):
        self.program = program
        self.input_numbers = input_numbers
        self.memory = {'w': 0, 'x': 0, 'y': 0, 'z': 0}


    def run(self):
        for line in self.program.split('\n'):
            # print(line)
            if line.startswith('inp'):
                self._input(line)
            elif line.startswith('add'):
                self._add(line)
            elif line.startswith('mul'):
                self._mul(line)
            elif line.startswith('div'):
                self._div(line)
            elif line.startswith('mod'):
                self._mod(line)
            elif line.startswith('eql'):
                self._eql(line)
            else:
                raise ValueError
            # print(self.memory)


    def _input(self, line):
        a = line.split(' ')[1]
        self.memory[a] = next(self.input_numbers)


    def _add(self, line):
        _, a, b = line.split(' ')
        b = self.memory[b] if b.isalpha() else int(b)
        self.memory[a] = self.memory[a] + b


    def _mul(self, line):
        _, a, b = line.split(' ')
        b = self.memory[b] if b.isalpha() else int(b)
        self.memory[a] = b * self.memory[a]


    def _div(self, line):
        _, a, b = line.split(' ')
        b = self.memory[b] if b.isalpha() else int(b)
        self.memory[a] = self.memory[a] // b


    def _mod(self, line):
        _, a, b = line.split(' ')
        b = self.memory[b] if b.isalpha() else int(b)
        self.memory[a] = self.memory[a] % b


    def _eql(self, line):
        _, a, b = line.split(' ')
        b = self.memory[b] if b.isalpha() else int(b)
        if self.memory[a] == b:
            self.memory[a] = 1
        else:
            self.memory[a] = 0


def test1():
    program = '''inp x
mul x -1'''.strip()
    for n in [-20, -10, -4, -1, 0, 1, 4, 10, 20]:
        a = ALU(program, iter([n]))
        a.run()
        assert a.memory['x'] == -n


def test2():
    program = '''inp z
inp x
mul z 3
eql z x'''.strip()
    numbers = [(1, 1), (3, 1), (1, 3), (6, 2), (2, 6), (-1, -3)]
    answer = [0, 0, 1, 0, 1, 1]
    for _input, output in zip(numbers, answer):
        a = ALU(program, iter(_input))
        a.run()
        assert a.memory['z'] == output


def test3():
    program = '''inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2'''.strip()
    numbers = [0, 1, 2, 3, 4, 8, 15, 16, 17]
    answers = [
        {'w': 0, 'x': 0, 'y': 0, 'z': 0},
        {'w': 0, 'x': 0, 'y': 0, 'z': 1},
        {'w': 0, 'x': 0, 'y': 1, 'z': 0},
        {'w': 0, 'x': 0, 'y': 1, 'z': 1},
        {'w': 0, 'x': 1, 'y': 0, 'z': 0},
        {'w': 1, 'x': 0, 'y': 0, 'z': 0},
        {'w': 1, 'x': 1, 'y': 1, 'z': 1},
        {'w': 0, 'x': 0, 'y': 0, 'z': 0},
        {'w': 0, 'x': 0, 'y': 0, 'z': 1},
    ]
    for n, answer in zip(numbers, answers):
        a = ALU(program, iter([n]))
        a.run()
        assert a.memory == answer


def main():
    test1()
    test2()
    test3()


if __name__ == '__main__':
    main()
