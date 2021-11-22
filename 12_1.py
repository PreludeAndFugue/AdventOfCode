#!python

'''Day 12, part 1.'''

import json

INPUT = 'data_12.txt'


def numbers_from_data(data):
    if isinstance(data, list):
        for item in data:
            yield from numbers_from_data(item)
    if isinstance(data, dict):
        values = data.values()
        # part 2
        if 'red' not in values:
            for k, v in data.items():
                yield from numbers_from_data(k)
                yield from numbers_from_data(v)
    if isinstance(data, str):
        pass
    if isinstance(data, int):
        yield data


if __name__ == '__main__':
    data = json.load(open(INPUT, 'r'))
    # print(data)

    s = sum(n for n in numbers_from_data(data))
    print(s)
