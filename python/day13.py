#!python3

INPUT = 'day13.txt'

TEST_INPUT = '''939
7,13,x,x,59,x,31,19
'''

def get_input(input):
    timestamp, buses = input.strip().split('\n')
    timestamp = int(timestamp)
    buses = [int(b) for b in buses.split(',') if b != 'x']
    return timestamp, buses


def wait(bus, timestamp):
    return bus - (timestamp % bus)


def _part1(timestamp, buses):
    waits = {wait(bus, timestamp): bus for bus in buses}
    min_wait = min(waits.keys())
    return waits[min_wait] * min_wait


def test1():
    timestamp, buses = get_input(TEST_INPUT)
    return _part1(timestamp, buses)


def part1():
    timestamp, buses = get_input(open(INPUT, 'r').read())
    return _part1(timestamp, buses)


def main():
    assert test1() == 295

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
