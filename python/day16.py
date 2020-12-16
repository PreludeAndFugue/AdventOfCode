#!python3

import re

INPUT = 'day16.txt'

TEST_INPUT = '''
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
'''

FIELDS = re.compile(r'[\w\s]*: (\d+)-(\d+) or (\d+)-(\d+)')
YOUR_TICKET = re.compile(r'your ticket:\n([\d,]*)')
NEARBY_TICKETS = re.compile(r'nearby tickets:\n([\d,\n]*)')


def make_fields(match):
    ns =  list(map(int, match))
    return [
        range(ns[0], ns[1] + 1),
        range(ns[2], ns[3] + 1)
    ]


def get_input(input):
    fields = FIELDS.findall(input)
    fields = list(map(make_fields, fields))

    your_ticket = YOUR_TICKET.search(input)
    your_ticket = list(map(int, your_ticket.group(1).split(',')))

    nearby_tickets = NEARBY_TICKETS.search(input)
    nearby_tickets = [list(map(int, line.split(','))) for line in nearby_tickets.group(1).strip().split('\n')]
    return fields, your_ticket, nearby_tickets


def is_value_valid(value, fields):
    for field in fields:
        for r in field:
            if value in r:
                return True
    return False


def get_invalid_values(ticket, fields):
    invalid_values = []
    for value in ticket:
        if not is_value_valid(value, fields):
            invalid_values.append(value)
    return invalid_values


def _part1(fields, nearby_tickets):
    invalid = []
    for ticket in nearby_tickets:
        inv = get_invalid_values(ticket, fields)
        invalid.extend(inv)
    return sum(invalid)


def test1():
    fields, _, nearby_tickets = get_input(TEST_INPUT.strip())
    return _part1(fields, nearby_tickets)


def part1():
    fields, _, nearby_tickets = get_input(open(INPUT, 'r').read())
    return _part1(fields, nearby_tickets)


def main():
    assert test1() == 71

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
