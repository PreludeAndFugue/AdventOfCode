#!python3

'''
FBFBBFFRLR: row 44, column 5, seat ID 357.
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
'''


INPUT = 'day05.txt'

TEST_INPUT = '''FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL'''

TEST_OUTPUT = [
    357, 567, 119, 820
]


TRANSLATION = str.maketrans('FBRL', '0110')

def get_seats(input):
    for row in input.strip().split('\n'):
        yield row[:7], row[7:]


def translate_binary(binary):
    b = binary.translate(TRANSLATION)
    return int(b, 2)


def get_seat_id(seat):
    row, col = map(translate_binary, seat)
    return 8 * row + col


def test1():
    seats = get_seats(TEST_INPUT)
    for (seat, seat_id) in zip(seats, TEST_OUTPUT):
        assert get_seat_id(seat) == seat_id


def part2(seat_ids):
    min_id = min(seat_ids)
    max_id = max(seat_ids)
    seat_set = set(seat_ids)
    all_seat_set = set(range(min_id, max_id))
    empty_set_set = all_seat_set - seat_set
    return empty_set_set.pop()


def main():
    seats = get_seats(open(INPUT, 'r').read())
    seat_ids = [get_seat_id(s) for s in seats]

    test1()

    print(max(seat_ids))

    p = part2(seat_ids)
    print(p)


if __name__ == "__main__":
    main()
