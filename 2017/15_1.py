#!python3

'''Day 15, part 1.'''

START_A_TEST = 65
START_B_TEST = 8921

START_A = 516
START_B = 190

FACTOR_A = 16807
FACTOR_B = 48271

MULTIPLE_A = 4
MULTIPLE_B = 8

MODULO = 2147483647


def create_generator(start, factor):
    '''Create a generator.'''
    def generator():
        '''The generator.'''
        previous_value = start
        while True:
            value = (factor * previous_value) % MODULO
            previous_value = value
            yield value
    return generator()


def create_generator2(start, factor, multiple):
    '''Create a generator for part 2.'''
    def generator():
        previous_value = start
        while True:
            value = (factor * previous_value) % MODULO
            if value % multiple:
                previous_value = value
                continue
            value = value % MODULO
            previous_value = value
            yield value
    return generator()


def matching_lowest_16_bits(m, n):
    '''Find the number of match bits in the lowest 16 bits of m and n.

    >>> matching_lowest_16_bits(2, 2)
    '1111111111111111'
    >>> matching_lowest_16_bits(4, 2)
    '1111111111111001'
    >>> matching_lowest_16_bits(245556042, 1431495498)
    '1111111111111111'
    '''
    mask = 0xFFFF
    x = ~(m ^ n)
    x = x & mask
    return x
    # return format(x, '016b')


def count_ones(n):
    '''Count ones in binary representation of n.'''
    total = 0
    while n:
        if n & 1:
            total += 1
        n >>= 1
    return total


def main1():
    '''Main entry point.'''
    gen_a = create_generator(START_A, FACTOR_A)
    gen_b = create_generator(START_B, FACTOR_B)

    total = 0
    for _ in range(40_000_000):
        matching = matching_lowest_16_bits(next(gen_a), next(gen_b))
        # print(matching)
        # if matching.count('1') == 16:
        if count_ones(matching) == 16:
            total += 1
    print(total)


def main2():
    '''Main entry point for part 2.'''
    gen_a = create_generator2(START_A, FACTOR_A, MULTIPLE_A)
    gen_b = create_generator2(START_B, FACTOR_B, MULTIPLE_B)

    for _ in range(5):
        print(next(gen_a), next(gen_b))

    total = 0
    for i in range(5_000_000):
        matching = matching_lowest_16_bits(next(gen_a), next(gen_b))
        if count_ones(matching) == 16:
            total += 1
    print(total)


if __name__ == '__main__':
    main2()
