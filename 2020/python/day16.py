#!python3

from collections import defaultdict
import re

INPUT = 'day16.txt'

TEST_INPUT = '''class: 1-3 or 5-7
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

TEST_INPUT_2 = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
'''

FIELDS = re.compile(r'([\w ]*): (\d+)-(\d+) or (\d+)-(\d+)')
YOUR_TICKET = re.compile(r'your ticket:\n([\d,]*)')
NEARBY_TICKETS = re.compile(r'nearby tickets:\n([\d,\n]*)')


def make_fields(match):
    ns =  list(map(int, match[1:]))
    return match[0], [range(ns[0], ns[1] + 1), range(ns[2], ns[3] + 1)]


def get_input(input):
    fields = FIELDS.findall(input)
    fields = dict(map(make_fields, fields))

    your_ticket = YOUR_TICKET.search(input)
    your_ticket = list(map(int, your_ticket.group(1).split(',')))

    nearby_tickets = NEARBY_TICKETS.search(input)
    nearby_tickets = [list(map(int, line.split(','))) for line in nearby_tickets.group(1).strip().split('\n')]

    assert len(fields) == len(your_ticket)
    for n in nearby_tickets:
        assert len(n) == len(your_ticket)

    return fields, your_ticket, nearby_tickets


def is_value_valid(value, fields):
    for rs in fields.values():
        for r in rs:
            if value in r:
                return True
    return False


def get_invalid_values(ticket, fields):
    invalid_values = []
    for value in ticket:
        if not is_value_valid(value, fields):
            invalid_values.append(value)
    return invalid_values


def is_invalid_ticket(ticket, fields):
    for value in ticket:
        if not is_value_valid(value, fields):
            return True
    return False


def get_valid_field_names(fields, value):
    names = []
    for name, rs in fields.items():
        for r in rs:
            if value in r:
                names.append(name)
    return names


def make_eligible_fields(fields):
    names = list(n for n in fields.keys())
    return {i: set(names) for i, name in enumerate(names)}


def make_unique_fields(eligible_fields):
    unique_fields = {}
    seen = set()
    did_change = True
    while did_change:
        did_change = False
        for k, v in eligible_fields.items():
            if len(v) == 1:
                name = v.pop()
                unique_fields[k] = name
                seen.add(name)
                did_change = True
        for k, v in eligible_fields.items():
            for x in seen:
                if x in v:
                    v.remove(x)
    return unique_fields


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


def _part2(fields, your_ticket, nearby_tickets):
    valid_tickets = [t for t in nearby_tickets if not is_invalid_ticket(t, fields)]
    eligible_fields = make_eligible_fields(fields)

    for ticket in valid_tickets:
        for i, value in enumerate(ticket):
            valid_field_names = get_valid_field_names(fields, value)
            if valid_field_names:
                eligible_fields[i].intersection_update(valid_field_names)

    unique_fields = make_unique_fields(eligible_fields)
    answer = 1
    for k in sorted(unique_fields.keys()):
        name = unique_fields[k]
        if name.startswith('departure'):
            answer *= your_ticket[k]
    return answer


def test2():
    fields, your_ticket, nearby_tickets = get_input(TEST_INPUT_2.strip())
    _part2(fields, your_ticket, nearby_tickets)


def part2():
    fields, your_ticket, nearby_tickets = get_input(open(INPUT, 'r').read())
    return _part2(fields, your_ticket, nearby_tickets)


def main():
    assert test1() == 71

    p = part1()
    print(p)

    test2()

    p = part2()
    print(p)


if __name__ == "__main__":
    main()
