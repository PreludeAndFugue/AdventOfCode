#!python3

'''Day 20, part 1.'''

from data_20 import particles, manhattan


if __name__ == '__main__':
    print(len(particles))
    min_a = min(particles, key=lambda item: manhattan(item.a))
    print(min_a)
    min_v = min(min_a, key=lambda item: manhattan(item.v))
    print(min_v)

    # for item in data:
    #     print(manhattan(item['a']))
