#!python3

from collections import Counter


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

SOURCE = 'day04.txt'

TEST = '''aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
'''

class Room(object):
    def __init__(self, string):
        parts = string.split('-')
        name = parts[:-1]
        last = parts[-1]
        checksum, last = last.split('[')
        self.name = name
        self.sector_id = int(checksum)
        self.checksum = last.strip(']')


    @property
    def is_valid(self):
        counter = Counter(sorted(''.join(self.name)))
        common = ''.join([item[0] for item in counter.most_common(5)])
        return ''.join(common) == self.checksum


    def decrypt(self):
        shift = self.sector_id % 26
        shifted = ALPHABET[shift:] + ALPHABET[:shift]
        trans = str.maketrans(ALPHABET, shifted)
        return [x.translate(trans) for x in self.name]


    def __repr__(self):
        return f'Room({self.name}, {self.sector_id}, {self.checksum}'


def main1():
    count = 0
    with open(SOURCE, 'r') as f:
        for line in f:
            room = Room(line.strip())
            if room.is_valid:
                count += room.sector_id
    print(count)


def main2():
    with open(SOURCE, 'r') as f:
        for line in f:
            room = Room(line.strip())
            if room.is_valid:
                d = room.decrypt()
                if 'northpole' in d:
                    print(room.sector_id)


def test1():
    results = [True, True, True, False]
    for string, result in zip(TEST.strip().split(), results):
        room = Room(string)
        assert room.is_valid == result


def test2():
    string = 'qzmt-zixmtkozy-ivhz-343[abcde]'
    room = Room(string)
    assert room.decrypt() == ['very', 'encrypted', 'name']


if __name__ == '__main__':
    test1()
    test2()
    main1()
    main2()
