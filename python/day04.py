#!python3

from itertools import chain
import re

INPUT = 'day04.txt'
TEST_INPUT = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''


TEST_INPUT_2_INVALID = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

TEST_INPUT_2_VALID = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''

KEYS_PART1 = [
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
]


PROG_HGT = re.compile(r'(\d+)(\w+)')
PROG_HCL = re.compile('#([0-9a-f]+)')


def flatten(list_of_lists):
    "Flatten one level of nesting"
    return chain.from_iterable(list_of_lists)


def get_credentials(input):
    credentials = []
    for item in (input.split('\n\n')):
        pairs = flatten(x.split(' ') for x in item.split('\n'))
        credential = dict(pair.split(':') for pair in pairs)
        credentials.append(credential)
    return credentials


def is_valid_part1(credential):
    for key in KEYS_PART1:
        if key not in credential:
            return False
    return True


def part1(credentials):
    count = 0
    for credential in credentials:
        if is_valid_part1(credential):
            count += 1
    return count


def is_valid_year(year, lower, upper):
    try:
        n = int(year)
        return lower <= n <= upper
    except:
        return False


def is_valid_byr(byr):
    return is_valid_year(byr, 1920, 2002)


def is_valid_iyr(iyr):
    return is_valid_year(iyr, 2010, 2020)


def is_valid_eyr(eyr):
    return is_valid_year(eyr, 2020, 2030)


def is_valid_hgt(hgt):
    m = PROG_HGT.match(hgt)
    if m is None:
        return False
    n = m[1]
    u = m[2]
    try:
        n = int(n)
    except:
        return False
    if u == 'cm':
        return 150 <= n <= 193
    elif u == 'in':
        return 59 <= n <= 76
    else:
        return False


def is_valid_hcl(hcl):
    m = PROG_HCL.match(hcl)
    if m is None:
        return False
    c = m[1]
    return len(c) == 6


def is_valid_ecl(ecl):
    valid = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    return ecl in valid


def is_valid_pid(pid):
    return len(pid) == 9 and pid.isdecimal()


VALID = {
    'byr': is_valid_byr,
    'iyr': is_valid_iyr,
    'eyr': is_valid_eyr,
    'hgt': is_valid_hgt,
    'hcl': is_valid_hcl,
    'ecl': is_valid_ecl,
    'pid': is_valid_pid
}


def is_valid_part2(credential):
    for k in KEYS_PART1:
        if k not in credential:
            return False
        fn = VALID[k]
        c = credential[k]
        if not fn(c):
            return False
    return True


def test2():
    assert is_valid_byr('2002') == True
    assert is_valid_byr('2003') == False

    assert is_valid_hgt('60in') == True
    assert is_valid_hgt('190cm') == True
    assert is_valid_hgt('190in') == False
    assert is_valid_hgt('190') == False

    assert is_valid_hcl('#123abc') == True
    assert is_valid_hcl('#123abz') == False
    assert is_valid_hcl('123abc') == False

    assert is_valid_ecl('brn') == True
    assert is_valid_ecl('wat') == False

    assert is_valid_pid('000000001') == True
    assert is_valid_pid('0123456789') == False

    for valid in get_credentials(TEST_INPUT_2_VALID):
        assert is_valid_part2(valid) == True

    for invalid in get_credentials(TEST_INPUT_2_INVALID):
        assert is_valid_part2(invalid) == False


def part2(credentials):
    return sum(is_valid_part2(c) for c in credentials)


def main():
    assert part1(get_credentials(TEST_INPUT)) == 2

    credentials = get_credentials(open(INPUT, 'r').read().strip())

    p = part1(credentials)
    print(p)

    test2()

    p = part2(credentials)
    print(p)



if __name__ == "__main__":
    main()
