
from collections import deque
from enum import Enum

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

class Type(Enum):
    BROADCASTER = 1
    FLIP_FLOP = 2
    CONJUCTION = 3


class Broadcaster:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations

    def receive(self, pulse, from_module, modules):
        fname = from_module if isinstance(from_module, str) else from_module.name
        p = '-high->' if pulse else '-low->'
        print(fname, p, self.name)

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
        fname = from_module if isinstance(from_module, str) else from_module.name
        p = '-high->' if pulse else '-low->'
        print(fname, p, self.name)

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
        fname = from_module if isinstance(from_module, str) else from_module.name
        p = '-high->' if pulse else '-low->'
        print(fname, p, self.name)

        self._state[from_module.name] = pulse
        new_pulse = self._get_pulse(modules)
        for d in self.destinations:
            module = modules.get(d, None)
            m = module if module is not None else d
            yield m, new_pulse, self

    def _get_pulse(self, modules):
        # print('Conjuction get pulse', self.name, self._state)
        checks = []
        for m in self._state.keys():
            module = modules[m]
            # print('\t', module)
            checks.append(module._on)
        if all(self._state.values()):
        # if all(checks):
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
            # m = Module(name, Type.FLIP_FLOP, y)
            m = FlipFlop(name, y)
        elif x.startswith('&'):
            name = x[1:]
            # m = Module(name, Type.CONJUCTION, y)
            m = Conjunction(name, y)
        elif x.startswith('broadcaster'):
            name = x
            # m = Module(name, Type.BROADCASTER, y)
            m = Broadcaster(name, y)
        modules[name] = m
    for m in modules.values():
        if isinstance(m, Conjunction):
            continue
        for d in m.destinations:
            dm = modules[d]
            if isinstance(dm, Conjunction):
                dm._state[m.name] = False

    return modules


# d = get_input('20')
d = TEST.strip()
# d = TEST_2.strip()

modules = make_modules(d)
# for m in mod

broadcaster = modules['broadcaster']
receivers = deque([(broadcaster, False, 'button')])

while receivers:
    # print(receivers)
    module, pulse, from_module = receivers.popleft()

    if isinstance(module, str):
        fname = from_module if isinstance(from_module, str) else from_module.name
        p = '-high->' if pulse else '-low->'
        print(fname, p, module)
        continue

    for result in module.receive(pulse, from_module, modules):
        # if not isinstance(m, str):
        receivers.append(result)

    # input()
