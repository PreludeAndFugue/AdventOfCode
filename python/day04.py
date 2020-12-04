#!python3

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

KEYS_PART1 = [
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
]


def get_credentials(input):
    for item in (input.split('\n\n')):
        yield item


def is_valid_part1(credential):
    for key in KEYS_PART1:
        if key not in credential:
            return False
    return True


def part1(input):
    count = 0
    for credential in get_credentials(input):
        if is_valid_part1(credential):
            count += 1
    return count


def main():
    assert part1(TEST_INPUT) == 2
    
    p = part1(open(INPUT, 'r').read())
    print(p)


if __name__ == "__main__":
    main()
