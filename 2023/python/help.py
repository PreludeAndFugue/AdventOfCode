base_path = '../day{}.txt'

def get_input(d):
    path = base_path.format(d)
    return open(path, 'r').read().strip()


def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)
