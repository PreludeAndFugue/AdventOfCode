#!python3

'''Day  25, part 1.'''

from collections import defaultdict
from enum import Enum


class MachineState(Enum):
    '''The turing machine states.'''
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6


class TuringMachine(object):
    '''The turing machine.'''

    def __init__(self, position):
        self.position = position
        self.tape = defaultdict(int)
        self.state = MachineState.A
        self.state_machine = {
            MachineState.A: self._do_a,
            MachineState.B: self._do_b,
            MachineState.C: self._do_c,
            MachineState.D: self._do_d,
            MachineState.E: self._do_e,
            MachineState.F: self._do_f
        }

    def step(self):
        '''Run a single step of the turing machine.'''
        self.state_machine[self.state]()


    def check_sum(self):
        return sum(self.tape.values())


    def _do_a(self):
        if self.tape[self.position] == 0:
            self._update(1, 1, MachineState.B)
        else:
            self._update(0, -1, MachineState.E)


    def _do_b(self):
        if self.tape[self.position] == 0:
            self._update(1, -1, MachineState.C)
        else:
            self._update(0, 1, MachineState.A)


    def _do_c(self):
        if self.tape[self.position] == 0:
            self._update(1, -1, MachineState.D)
        else:
            self._update(0, 1, MachineState.C)


    def _do_d(self):
        if self.tape[self.position] == 0:
            self._update(1, -1, MachineState.E)
        else:
            self._update(0, -1, MachineState.F)


    def _do_e(self):
        if self.tape[self.position] == 0:
            self._update(1, -1, MachineState.A)
        else:
            self._update(1, -1, MachineState.C)


    def _do_f(self):
        if self.tape[self.position] == 0:
            self._update(1, -1, MachineState.E)
        else:
            self._update(1, 1, MachineState.A)


    def _update(self, value, position, state):
        self.tape[self.position] = value
        self.position += position
        self.state = state


if __name__ == '__main__':
    tm = TuringMachine(0)

    print(tm.tape)

    for _ in range(12_208_951):
        tm.step()
        # print(tm.tape)

    print(tm.check_sum())