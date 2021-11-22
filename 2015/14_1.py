#!python3

'''Day 14, part 1.'''

from collections import defaultdict
import re

INPUT = '''Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds.'''

regex = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'


def parse_input(input_string):
    results = []
    for row in input_string.strip().split('\n'):
        name, a, b, c = re.match(regex, row).groups()
        results.append((name, int(a), int(b), int(c)))
    return results


def main1(total_time, data):
    results = []
    for name, speed, duration, rest in data:
        unit = duration + rest
        unit_count, remainder = divmod(total_time, unit)
        distance = speed*duration*unit_count
        # print(name, unit, unit_count, distance, remainder)
        extra_time = duration if remainder > duration else remainder
        distance += speed*extra_time
        results.append((name, distance))

    max_value = max(results, key=lambda x: x[1])
    print(max_value)


def main2(total_time, data):
    results = defaultdict(list)
    for name, speed, duration, rest in data:
        unit = duration + rest
        unit_count, remainder = divmod(total_time, unit)
        distance = speed*duration*unit_count
        # print(name, unit, unit_count, distance, remainder)
        extra_time = duration if remainder > duration else remainder
        distance += speed*extra_time
        results[distance].append(name)

    max_value = max(results.keys())
    print(results[max_value])
    return results[max_value]


if __name__ == '__main__':
    data = parse_input(INPUT)
    # print(data)

    N = 2503

    results = defaultdict(int)
    for i in range(2503):
        winners = main2(i + 1, data)
        for winner in winners:
            results[winner] += 1

    print(results)
    
