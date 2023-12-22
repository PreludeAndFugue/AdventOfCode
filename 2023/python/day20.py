
from collections import deque
from math import lcm

from help import get_input

'''
button -low-> broadcaster
broadcaster -low-> a
broadcaster -low-> b
broadcaster -low-> c
a -high-> b
b -high-> c
c -high-> inv
inv -low-> a
a -low-> b
b -low-> c
c -low-> inv
inv -high-> a
'''

TEST = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''

TEST_2 = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
'''


class Broadcaster:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations

    def receive(self, pulse, from_module, modules):
        for d in self.destinations:
            module = modules[d]
            yield module, pulse, self

    def __repr__(self) -> str:
        return f'Broadcaster({self.name}, {self.destinations})'


class FlipFlop:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations
        self._on = False

    def receive(self, pulse, from_module, modules):
        if pulse:
            pass
        else:
            self._on = not self._on
            for d in self.destinations:
                module = modules[d]
                yield module, self._on, self

    def __repr__(self) -> str:
        return f'FlipFlop({self.name}, {self.destinations}, {self._on})'


class Conjunction:
    def __init__(self, name , destinations):
        self.name = name
        self.destinations = destinations
        self._state = {}

    def receive(self, pulse, from_module, modules):
        self._state[from_module.name] = pulse
        new_pulse = self._get_pulse()
        for d in self.destinations:
            module = modules.get(d, None)
            m = module if module is not None else d
            yield m, new_pulse, self

    def _get_pulse(self):
        if all(self._state.values()):
            return False
        else:
            return True

    def __repr__(self) -> str:
        return f'Conjunction({self.name}, {self.destinations}, {self._state})'


def make_modules(d):
    modules = {}
    for line in d.split('\n'):
        x, y = line.split(' -> ')
        y = y.split(', ')
        if x.startswith('%'):
            name = x[1:]
            m = FlipFlop(name, y)
        elif x.startswith('&'):
            name = x[1:]
            m = Conjunction(name, y)
        elif x.startswith('broadcaster'):
            name = x
            m = Broadcaster(x, y)
        modules[name] = m
    for m in modules.values():
        if isinstance(m, Conjunction):
            continue
        for d in m.destinations:
            dm = modules[d]
            if isinstance(dm, Conjunction):
                dm._state[m.name] = False

    return modules


def run(modules, i):
    broadcaster = modules['broadcaster']
    receivers = deque([(broadcaster, False, 'button')])

    low = 0
    high = 0

    while receivers:
        module, pulse, from_module = receivers.popleft()

        if pulse:
            high += 1
        else:
            low += 1

        if isinstance(module, str):
            continue

        if not isinstance(from_module, str):
            if from_module.name == 'xl' and pulse:
                print(i)

        for result in module.receive(pulse, from_module, modules):
            receivers.append(result)

    return high, low

def part1(d):
    modules = make_modules(d)

    low_total = 0
    high_total = 0
    for i in range(1, 1001):
        high, low = run(modules, i)
        high_total += high
        low_total += low

    return low_total*high_total


def part2():
    '''
    rx <- df <- (gp, ln, xp, xl)

    The number of button presses for each module to send a high pulse. When do they
    all send a high pulse to df? When all high pulses sent to df, it will send a low
    pulse. Use lcm.
    gp: 3833
    ln: 4021
    xp: 4057
    xl: 4051
    '''

    return lcm(3833, 4021, 4057, 4051)


def main():
    d = get_input('20')
    # d = TEST.strip()
    # d = TEST_2.strip()

    p1 = part1(d)
    print(p1)

    p2 = part2()
    print(p2)


if __name__ == '__main__':
    main()
