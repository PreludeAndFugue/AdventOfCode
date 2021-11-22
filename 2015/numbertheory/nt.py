#!python3

from math import sqrt

def divisors(n):
    '''Divisors of integer n.'''
    m = int(sqrt(n))
    d = set([1, n])
    for i in range(2, m + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)
