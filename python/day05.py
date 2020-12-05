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


def part1():
    seats = get_seats(open(INPUT, 'r').read())
    max_seat_id = max(get_seat_id(s) for s in seats)
    return max_seat_id


def main():
    test1()

    p = part1()
    print(p)


if __name__ == "__main__":
    main()
