
from collections import deque

from tqdm import tqdm

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
        # fname = from_module if isinstance(from_module, str) else from_module.name
        # p = '-high->' if pulse else '-low->'
        # print(fname, p, self.name)

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
        # fname = from_module if isinstance(from_module, str) else from_module.name
        # p = '-high->' if pulse else '-low->'
        # print(fname, p, self.name)

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
        # fname = from_module if isinstance(from_module, str) else from_module.name
        # p = '-high->' if pulse else '-low->'
        # print(fname, p, self.name)

        self._state[from_module.name] = pulse
        new_pulse = self._get_pulse(modules)
        for d in self.destinations:
            module = modules.get(d, None)
            m = module if module is not None else d
            yield m, new_pulse, self

    def _get_pulse(self, modules):
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


d = get_input('20')
# d = TEST.strip()
# d = TEST_2.strip()

modules = make_modules(d)

def run(modules):
    broadcaster = modules['broadcaster']
    receivers = deque([(broadcaster, False, 'button')])

    low = 0
    high = 0

    while receivers:
        # print(receivers)
        module, pulse, from_module = receivers.popleft()

        if pulse:
            high += 1
        else:
            low += 1

        if isinstance(module, str):

            # fname = from_module if isinstance(from_module, str) else from_module.name
            # p = '-high->' if pulse else '-low->'
            # print(fname, p, module)

            if module == 'rx' and not pulse:
                print('\t', '...')
                raise ValueError
            continue

        for result in module.receive(pulse, from_module, modules):
            receivers.append(result)

    return high, low


low_total = 0
high_total = 0
df = modules['df']
for _ in range(1000):
    high, low = run(modules)
    high_total += high
    low_total += low

    # print(df._state)
    # if any(df._state.values()):
    #     print(df)

print(low_total*high_total)

# print(df)