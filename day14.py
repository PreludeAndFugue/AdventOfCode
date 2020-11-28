#!python3

from hashlib import md5

# Cache of index and md5
CACHE = {}
SALT = 'ngcjuoqr'
TEST_SALT = 'abc'

salt = SALT

def get_hexdigest(n):
    if n in CACHE:
        return CACHE[n]
    x = f'{salt}{n}'.encode('utf8')
    y = md5(x).hexdigest()
    CACHE[n] = y
    return y


def get_stretch_hexdigest(n):
    if n in CACHE:
        return CACHE[n]
    x = f'{salt}{n}'.encode('utf8')
    y = md5(x)
    for j in range(2016):
        y = md5(y.hexdigest().encode('utf8'))
    CACHE[n] = y.hexdigest()
    return y.hexdigest()


def contains_triple(x):
    l = len(x)
    for i in range(l - 2):
        t = x[i:i + 3]
        if len(set(t)) == 1:
            return t[0]
    return None


def check_quint(i, ch):
    test = ch * 5
    for j in range(i + 1, i + 1001):
        # z = get_hexdigest(j)
        z = get_stretch_hexdigest(j)
        if test in z:
            return True
    return False


def part1():
    keys = []
    for i in range(1_000_000):
        # x = get_hexdigest(i)
        x = get_stretch_hexdigest(i)
        z = contains_triple(x)
        if z is not None:
            if check_quint(i, z):
                print(i, x)
                keys.append(x)
                if len(keys) == 64:
                    return i


def main():
    x = part1()
    print(x)


if __name__ == '__main__':
    main()
