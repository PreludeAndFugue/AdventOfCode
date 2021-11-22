#!python3

TEST01 = '''
ULL
RRDDD
LURDL
UUUUD
'''


SOURCE = 'day02.txt'

LEFT = -1, 0
RIGHT = 1, 0
UP = 0, -1
DOWN = 0, 1

KEYPAD1 = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

KEYPAD2 = [
    ['', '', '1', '', ''],
    ['', '2', '3', '4', ''],
    ['5', '6', '7', '8', '9'],
    ['', 'A', 'B', 'C', ''],
    ['', '', 'D', '', '']
]

DIRECTIONS = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, -1),
    'D': (0, 1)
}


class Keypad(object):
    def __init__(self, keypad):
        self._coord_helper = Keypad._make_coord_helper(keypad)
        self._digit_helper = Keypad._make_digit_helper(keypad)


    def next_digit(self, digit, direction):
        location = self._digit_helper[digit]
        dx, dy = DIRECTIONS[direction]
        x, y = location[0] + dx, location[1] + dy
        new_location = x, y
        new_digit = self._coord_helper.get(new_location, '')
        return digit if new_digit == '' else new_digit


    @staticmethod
    def _make_digit_helper(keypad):
        coords = {}
        for i, row in enumerate(keypad):
            for j, col in enumerate(row):
                coords[col] = j, i
        return coords


    @staticmethod
    def _make_coord_helper(keypad):
        coords = {}
        for i, row in enumerate(keypad):
            for j, col in enumerate(row):
                coords[(j, i)] = col
        return coords



def make_instructions(string):
    return string.strip().split()


def make_keypad_coords(keypad):
    coords = {}
    for i, row in enumerate(keypad):
        for j, col in enumerate(row):
            coords[col] = i, j
    return coords


def run1(source, keypad):
    instructions = make_instructions(source)
    keypad = Keypad(keypad)
    digit = '5'
    result = []
    for instruction in instructions:
        for direction in instruction:
            digit = keypad.next_digit(digit, direction)
        result.append(digit)

    print(''.join(result))


def main1():
    run1(open(SOURCE, 'r').read(), KEYPAD1)


def main2():
    run1(open(SOURCE, 'r').read(), KEYPAD2)


def test1():
    run1(TEST01, KEYPAD1)


def test2():
    run1(TEST01, KEYPAD2)


if __name__ == '__main__':
    test1()
    main1()
    test2()
    main2()
