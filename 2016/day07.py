#!python3


SOURCE = 'day07.txt'

TEST1 = '''abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn'''

TEST2 = '''aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb'''


def split_ip(ip):
    outside = []
    inside = []
    is_outside = True
    current_inside = []
    current_outside = []
    for c in ip:
        if c == '[':
            is_outside = False
            outside.append(''.join(current_outside))
            current_outside = []
        elif c == ']':
            is_outside = True
            inside.append(''.join(current_inside))
            current_inside = []
        else:
            if is_outside:
                current_outside.append(c)
            else:
                current_inside.append(c)
    if current_inside:
        inside.append(''.join(current_inside))
    if current_outside:
        outside.append(''.join(current_outside))
    return outside, inside


def supports_tls(outsides):
    for outside in outsides:
        for i in range(len(outside) - 3):
            x = outside[i:i + 4]
            if x == x[::-1] and x[0] != x[1]:
                return True
    return False


def get_abas(parts):
    abas = set()
    for part in parts:
        for i in range(len(part) - 2):
            x = part[i:i + 3]
            if x == x[::-1] and x[0] != x[1]:
                abas.add(x)
    return abas


def supports_ssl(outsides, insides):
    abas = get_abas(outsides)
    babs = get_abas(insides)
    babs = set([x[1:] + x[1] for x in babs])
    return len(abas.intersection(babs)) != 0


def main1():
    count = 0
    ips = open(SOURCE, 'r').read().strip().split()
    for ip in ips:
        outsides, insides = split_ip(ip)
        if supports_tls(outsides):
            if not supports_tls(insides):
                count += 1
    print(count)


def main2():
    count = 0
    ips = open(SOURCE, 'r').read().strip().split()
    for ip in ips:
        outsides, insides = split_ip(ip)
        if supports_ssl(outsides, insides):
            count += 1
    print(count)


def test1():
    for line in TEST1.split():
        print(line)
        outsides, _ = split_ip(line)
        print(supports_tls(outsides))


def test2():
    for line in TEST2.split():
        print(line)
        outsides, insides = split_ip(line)
        print(supports_ssl(outsides, insides))


if __name__ == '__main__':
    # test1()
    # test2()
    main1()
    main2()
