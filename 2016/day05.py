#!python3

from hashlib import md5


TEST1 = 'abc'
INPUT = 'uqwqemis'


def get_char(door_id, n):
    x = f'{door_id}{n}'
    y = md5(x.encode('ascii')).hexdigest()
    if y.startswith('00000'):
        return y[5]
    else:
        return None

def get_position_and_char(door_id, n):
    x = f'{door_id}{n}'
    y = md5(x.encode('ascii')).hexdigest()
    if y.startswith('00000'):
        position = y[5]
        char = y[6]
        if position not in '01234567':
            return None, None
        else:
            return int(position), char
    else:
        return None, None


def main1():
    result = []
    for i in range(1_000_000_000):
        c = get_char(INPUT, i)
        if c is not None:
            result.append(c)
            if len(result) == 8:
                break
    print(''.join(result))


def main2():
    result = {}
    for i in range(1_000_000_000):
        p, c = get_position_and_char(INPUT, i)
        if p is not None and p not in result:
            result[p] = c
            # print(result)
            if len(result) == 8:
                break
    print(''.join([result[i] for i in range(8)]))



def test1():
    result = []
    for i in range(1_000_000_000):
        c = get_char(TEST1, i)
        if c is not None:
            result.append(c)
            if len(result) == 8:
                break
    assert ''.join(result) == '18f47a30'


def test2():
    result = {}
    for i in range(1_000_000_000):
        p, c = get_position_and_char(TEST1, i)
        if p is not None and p not in result:
            result[p] = c
            # print(result)
            if len(result) == 8:
                break
    print(''.join([result[i] for i in range(8)]))



if __name__ == '__main__':
    # test1()
    # test2()
    # main1()
    main2()
