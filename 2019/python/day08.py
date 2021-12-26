#!python3

from collections import Counter
from itertools import zip_longest

from helpers import BASE

WIDTH = 25
HEIGHT = 6
LAYER_LENGTH = WIDTH * HEIGHT

TRANSPARENT = '2'
BLACK = '0'
WHITE = '1'


def grouper(iterable, n, fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def part1(string):
    min_zero_count = 10_000_000
    min_layer = None
    min_counter = None
    for layer in grouper(string, LAYER_LENGTH):
        counter = Counter(layer)
        zero_count = counter['0']
        if zero_count < min_zero_count:
            min_zero_count = zero_count
            min_counter = counter
            min_layer = layer
    return min_counter['1'] * min_counter['2']


def part2(string):
    final_layer = [TRANSPARENT for _ in range(LAYER_LENGTH)]
    for layer in grouper(string, LAYER_LENGTH):
        for i, pixel in enumerate(layer):
            current_pixel = final_layer[i]
            if current_pixel == TRANSPARENT:
                p = pixel
                final_layer[i] = p
    image = '\n'.join(''.join(' ' if r == BLACK else '#' for r in row) for row in grouper(final_layer, WIDTH))
    print(image)


def main():
    string = open(BASE + 'day08.txt', 'r').read().strip()

    p1 = part1(string)
    print(f'Part 1: {p1}')

    part2(string)


if __name__ == '__main__':
    main()
