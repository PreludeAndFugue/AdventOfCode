#!python3

from helpers import BASE


TEST01 = '''D2FE28'''
TEST02 = '''38006F45291200'''
TEST03 = '''EE00D40C823060'''
TEST04 = '''8A004A801A8002F478'''
TEST05 = '''620080001611562C8802118E34'''
TEST06 = '''C0015000016115A2E0802F182340'''
TEST07 = '''A0016C880162017C3686B18A3D4780'''

TEST08 = '''C200B40A82'''
TEST09 = '''04005AC33890'''
TEST10 = '''880086C3E88112'''
TEST11 = '''CE00C43D881120'''
TEST12 = '''D8005AC2A8F0'''
TEST13 = '''F600BC2D8F'''
TEST14 = '''9C005AC2F8F0'''
TEST15 = '''9C0141080250320F1802104A08'''


TRANSLATION_TABLE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}
TRANSLATION = str.maketrans(TRANSLATION_TABLE)


def parse(string):
    return iter(string.strip().translate(TRANSLATION))


def get_version(bits):
    try:
        parts = []
        for _ in range(3):
            parts.append(next(bits))
        return int(''.join(parts), 2)
    except StopIteration:
        return None


def get_type(bits):
    return int(''.join(next(bits) for _ in range(3)), 2)


def get_value(bits):
    more_parts = True
    ns = []
    while more_parts:
        prefix = next(bits)
        more_parts = True if prefix == '1' else False
        n = ''.join(next(bits) for _ in range(4))
        ns.append(n)
    return int(''.join(ns), 2)


def get_packet(bits):
    v = get_version(bits)
    if v is None:
        return None
    t = get_type(bits)
    if t == 4:
        n = get_value(bits)
        return (v, t, n)
    else:
        i = next(bits)
        if i == '0':
            l = int(''.join(next(bits) for _ in range(15)), 2)
            sub_bits = iter(next(bits) for _ in range(l))
            sub_packets = []
            while True:
                sub_packet = get_packet(sub_bits)
                if sub_packet is None:
                    return (v, t, sub_packets)
                sub_packets.append(sub_packet)
        elif i == '1':
            i_n = int(''.join(next(bits) for _ in range(11)), 2)
            sub_packets = []
            for _ in range(i_n):
                sub_packet = get_packet(bits)
                sub_packets.append(sub_packet)
            return (v, t, sub_packets)
        else:
            raise ValueError


def version_sum(package):
    v, t, sub = package
    if t == 4:
        return v
    else:
        return v + sum(version_sum(p) for p in sub)


def product(items):
    t = 1
    for i in items:
        t *= i
    return t


def calculate(packet):
    v, t, sub = packet
    if t == 0:
        return sum(calculate(p) for p in sub)
    elif t == 1:
        return product([calculate(p) for p in sub])
    elif t == 2:
        return min(calculate(p) for p in sub)
    elif t == 3:
        return max(calculate(p) for p in sub)
    elif t == 4:
        return sub
    elif t == 5:
        assert len(sub) == 2
        c1 = calculate(sub[0])
        c2 = calculate(sub[1])
        return 1 if c1 > c2 else 0
    elif t == 6:
        assert len(sub) == 2
        c1 = calculate(sub[0])
        c2 = calculate(sub[1])
        return 1 if c1 < c2 else 0
    elif t == 7:
        assert len(sub) == 2
        c1 = calculate(sub[0])
        c2 = calculate(sub[1])
        return 1 if c1 == c2 else 0
    else:
        raise ValueError


def part1(bits):
    p = get_packet(bits)
    return version_sum(p)


def part2(bits):
    p = get_packet(bits)
    return calculate(p)


def main():
    string = open(BASE + 'day16.txt', 'r').read()

    t4 = parse(TEST04)
    assert part1(t4) == 16

    t5 = parse(TEST05)
    assert part1(t5) == 12

    t6 = parse(TEST06)
    assert part1(t6) == 23

    t7 = parse(TEST07)
    assert part1(t7) == 31

    bits = parse(string)
    p1 = part1(bits)
    print(f'Part 1: {p1}')

    t8 = parse(TEST08)
    assert part2(t8) == 3

    t9 = parse(TEST09)
    assert part2(t9) == 54

    t10 = parse(TEST10)
    assert part2(t10) == 7

    t11 = parse(TEST11)
    assert part2(t11) == 9

    t12 = parse(TEST12)
    assert part2(t12) == 1

    t13 = parse(TEST13)
    assert part2(t13) == 0

    t14 = parse(TEST14)
    assert part2(t14) == 0

    t15 = parse(TEST15)
    assert part2(t15) == 1

    bits = parse(string)
    p2 = part2(bits)
    print(f'Part 2 {p2}')


if __name__ == '__main__':
    main()
