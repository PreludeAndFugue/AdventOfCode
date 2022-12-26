

from help import get_input

TEST = '''1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122'''


def number5(n):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(str(n % 5))
        n //= 5
    return ''.join(digits[::-1])


def convert_from(s):
    result = 0
    for i, c in enumerate(reversed(s)):
        # print(i, c)
        n = 5 ** i
        if c.isdigit():
            c = int(c)
            result += c * n
        elif c == '-':
            result -= n
        elif c == '=':
            result -= 2*n
    return result


def convert_to(n):
    result = []
    m5 = int(number5(n))
    while m5 > 0:
        k = m5 % 10
        assert 0 <= k <= 4
        m5 = m5 // 10
        if k == 0 or k == 1 or k == 2:
            result.append(str(k))
        elif k == 3:
            result.append('=')
            m5 += 1
        elif k == 4:
            result.append('-')
            m5 += 1
        else:
            raise ValueError

        a = m5 % 10
        if a == 5:
            m5 += 5
        if a > 5:
            raise ValueError

    return ''.join(reversed(result))


def test():
    s = 0
    for x in TEST.strip().split('\n'):
        n = convert_from(x)
        s += n
        y = convert_to(n)
        assert x == y
    a = convert_to(s)
    b = convert_from(a)
    assert b == s


def main():
    s = get_input('25')
    total = 0
    for line in s.split('\n'):
        n = convert_from(line)
        total += n
        a = convert_to(n)
        assert a == line
    b = convert_to(total)
    c = convert_from(b)
    assert total == c
    print('Part 1:', b)


if __name__ == '__main__':
    test()
    main()
