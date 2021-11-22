#!python3

from enum import Enum


SOURCE = 'day09.txt'

TEST1 = 'ADVENT'
TEST2 = 'A(1x5)BC'
TEST3 = '(3x3)XYZ'
TEST4 = 'A(2x2)BCD(2x2)EFG'
TEST5 = '(6x1)(1x3)A'
TEST6 = 'X(8x2)(3x3)ABCY'

class State(Enum):
    READ = 1
    MARKER_FIRST_NUMBER = 2
    MARKER_SECOND_NUMBER = 3
    MARKER_CONTENT = 4


def decompress(string):
    if '(' not in string:
        return len(string)
    total_length = 0
    state = State.READ
    first_number = 0
    second_number = 0
    marker_content = []
    for c in string:
        if state == State.READ:
            if c == '(':
                state = State.MARKER_FIRST_NUMBER
            else:
                total_length += 1
        elif state == State.MARKER_FIRST_NUMBER:
            if c == 'x':
                state = State.MARKER_SECOND_NUMBER
            else:
                i = int(c)
                first_number = 10 * first_number + i
        elif state == State.MARKER_SECOND_NUMBER:
            if c == ')':
                state = State.MARKER_CONTENT
            else:
                i = int(c)
                second_number = 10 * second_number + i
        elif state == State.MARKER_CONTENT:
            if first_number == 1:
                marker_content.append(c)
                # total_length += second_number * len(marker_content)
                total_length += second_number * decompress(marker_content)
                marker_content = []
                state = State.READ
                first_number = 0
                second_number = 0
            else:
                first_number -= 1
                marker_content.append(c)
        else:
            raise EnvironmentError
    return total_length


def main1():
    s = open(SOURCE, 'r').read().strip()
    t = decompress(s)
    print(t)


def test1():
    t1 = decompress(TEST1)
    assert t1 == 'ADVENT'
    t2 = decompress(TEST2)
    assert t2 == 'ABBBBBC'
    t3 = decompress(TEST3)
    assert t3 == 'XYZXYZXYZ'
    t4 = decompress(TEST4)
    assert t4 == 'ABCBCDEFEFG'
    t5 = decompress(TEST5)
    assert t5 == '(1x3)A'
    t6 = decompress(TEST6)
    assert t6 == 'X(3x3)ABC(3x3)ABCY'


if __name__ == '__main__':
    # test1()
    main1()
