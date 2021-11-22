'''
Some maths helpers.
'''

from math import prod

def modular_inverse(x, m):
    '''
    The inverse of x modulo m is a number y such that x*y mod m = 1.
    For example, if x = 6 and m = 17, then y = 3, because 6*3 mod 17 = 1.

    The value of y mod m can be calculated exactly when x and m are coprime.

    If m is prime, the formula becomes y = x ** (m - 2)

    https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
    https://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Using_Euler's_theorem
    '''
    return (x ** (m - 2)) % m



def chinese_remainder(pairs):
    '''
    The Chinese remainder theorem solves a group of equations of the form

        x = a1 mod m1
        x = a2 mod m2
        .
        .
        .
        x = an mod mn

    where all pairs of m1, m2, ..., mn are coprime.

    https://en.wikipedia.org/wiki/Chinese_remainder_theorem

    pairs: [(a1, m1), (a2, m2), ..., (an, mn)]
    '''
    answer = 0
    mod_product = prod(pair[1] for pair in pairs)
    for a, m in pairs:
        M = mod_product // m
        M_inv = modular_inverse(M, m)
        answer += a * M * M_inv
    return answer % mod_product