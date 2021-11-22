#!python3

'''Data for day 21.'''

from math import sqrt

INPUT = '''../.. => ###/#../.#.
#./.. => ##./.#./...
##/.. => ..#/.#./#.#
.#/#. => ..#/.#./..#
##/#. => .../.##/##.
##/## => ###/#../#..
.../.../... => .#../.#../#..#/##..
#../.../... => ####/####/.###/####
.#./.../... => ####/..../#.#./.#.#
##./.../... => ..##/###./...#/##.#
#.#/.../... => .#../#..#/.#../#.#.
###/.../... => #.##/..##/##.#/..##
.#./#../... => .##./#..#/..../....
##./#../... => ##../.#../...#/####
..#/#../... => ##../###./...#/.#.#
#.#/#../... => ####/#.../..../##..
.##/#../... => #..#/..##/#..#/....
###/#../... => #.##/####/..#./#.#.
.../.#./... => #.##/.#.#/#.../...#
#../.#./... => .###/##.#/..../###.
.#./.#./... => ..#./.#../..../##..
##./.#./... => ##../...#/..../....
#.#/.#./... => ####/.#../..#./.###
###/.#./... => ..#./.###/##../.##.
.#./##./... => ###./#.#./.###/.##.
##./##./... => ...#/.#../.#../####
..#/##./... => ..#./#.../##../###.
#.#/##./... => #.../..../.#.#/.###
.##/##./... => #.#./.#../####/.###
###/##./... => .#.#/#.#./##../#...
.../#.#/... => #.##/##.#/..../#.#.
#../#.#/... => ##../#.##/###./###.
.#./#.#/... => ##../.#../#.##/###.
##./#.#/... => ##../##../..#./..#.
#.#/#.#/... => #.../.##./.###/###.
###/#.#/... => ##.#/##../.##./#...
.../###/... => ...#/####/..../#..#
#../###/... => ##.#/##.#/.##./#.#.
.#./###/... => .#../#.../.#.#/##.#
##./###/... => ##.#/#.#./#.../.#..
#.#/###/... => ..../#.../####/.#..
###/###/... => .#../#..#/.#../.#..
..#/.../#.. => .#.#/#.../..##/...#
#.#/.../#.. => ####/####/###./...#
.##/.../#.. => ####/.###/##.#/##..
###/.../#.. => ..##/..../...#/#.#.
.##/#../#.. => ###./..#./##.#/##.#
###/#../#.. => ##.#/...#/.##./.###
..#/.#./#.. => #.#./#.#./...#/#.#.
#.#/.#./#.. => ###./.#.#/#.#./.#..
.##/.#./#.. => #.#./.##./.###/#.#.
###/.#./#.. => #.../#.../#.#./.###
.##/##./#.. => .#.#/.##./..#./##..
###/##./#.. => .###/.##./#.##/..##
#../..#/#.. => #.#./#..#/###./.##.
.#./..#/#.. => ###./.###/...#/..##
##./..#/#.. => ###./##../####/.#.#
#.#/..#/#.. => ..#./.#../.##./.#..
.##/..#/#.. => ##.#/###./.##./#...
###/..#/#.. => ...#/..##/##.#/##.#
#../#.#/#.. => #.../.##./.#.#/.###
.#./#.#/#.. => #.##/...#/####/###.
##./#.#/#.. => .#../#.../.###/....
..#/#.#/#.. => ####/###./.#.#/#...
#.#/#.#/#.. => ###./..##/...#/#.##
.##/#.#/#.. => ##.#/..#./..##/.#.#
###/#.#/#.. => #.#./..../##../.###
#../.##/#.. => #..#/###./.#.#/##.#
.#./.##/#.. => #.../.###/.##./.###
##./.##/#.. => .#../###./.#../##.#
#.#/.##/#.. => .#../#.#./.#../#.##
.##/.##/#.. => ##../###./.#.#/.###
###/.##/#.. => ..##/...#/#.../.#..
#../###/#.. => #.##/#..#/####/###.
.#./###/#.. => .###/.#.#/#.#./..#.
##./###/#.. => ####/#.#./..##/#.##
..#/###/#.. => .###/##.#/.##./#.#.
#.#/###/#.. => #.##/###./.###/....
.##/###/#.. => #.##/..../.#../####
###/###/#.. => ##.#/###./.#../...#
.#./#.#/.#. => ..#./##.#/.#../###.
##./#.#/.#. => ..##/###./..#./.#.#
#.#/#.#/.#. => .#../..##/.#.#/.#.#
###/#.#/.#. => ##../#..#/.#../..#.
.#./###/.#. => #.../#..#/.#.#/....
##./###/.#. => ..../..##/..#./####
#.#/###/.#. => ..##/##.#/.###/...#
###/###/.#. => ##.#/#.##/..#./#.#.
#.#/..#/##. => #.../####/#.##/.###
###/..#/##. => ###./...#/.#.#/#..#
.##/#.#/##. => ..../.#.#/##.#/..##
###/#.#/##. => ###./.#../.#.#/###.
#.#/.##/##. => ###./.#../.#../.#.#
###/.##/##. => .##./..../..../#.##
.##/###/##. => ####/##../.###/##.#
###/###/##. => #..#/#.##/#.##/.#..
#.#/.../#.# => ####/#.#./#..#/.##.
###/.../#.# => .#../.#.#/.#../.#.#
###/#../#.# => ..#./..#./.###/#...
#.#/.#./#.# => #.#./..../.##./####
###/.#./#.# => #.../..##/.##./..#.
###/##./#.# => .#.#/##../#.#./..#.
#.#/#.#/#.# => #.##/#.##/#.##/..##
###/#.#/#.# => .###/#.#./.##./..##
#.#/###/#.# => ...#/#.#./..#./#..#
###/###/#.# => #.../#..#/#..#/.##.
###/#.#/### => .#.#/..##/##.#/#...
###/###/### => .###/#.#./#.../#...'''

TEST_INPUT = '''../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#'''


class Pattern(object):
    '''A pattern and replacement.'''

    def __init__(self, pattern, replacement):
        self.pattern = pattern
        self.replacement = replacement
        self.all_patterns = self._construct_all_patterns()


    def __str__(self):
        return f'{self.pattern} => {self.replacement}'


    def is_match(self, pattern):
        return pattern in self.all_patterns


    def _construct_all_patterns(self):
        if len(self.pattern) == 5:
            return self._construct_all_patterns2()
        return self._construct_all_patterns3()


    def _construct_all_patterns2(self):
        '''Construct all 2x2 patterns.'''
        all_patterns = set([self.pattern])
        rotations = self._rotations2(self.pattern)
        all_patterns.update(rotations)
        flip_v = self._flip_vertically2(self.pattern)
        all_patterns.add(flip_v)
        flip_v_rotations = self._rotations2(flip_v)
        all_patterns.update(flip_v_rotations)
        flip_h = self._flip_horizontally2(self.pattern)
        all_patterns.add(flip_h)
        flip_h_rotations = self._rotations2(flip_h)
        all_patterns.update(flip_h_rotations)
        return all_patterns


    def _rotations2(self, pattern):
        patterns = []
        pattern = self._rotate_clockwise2(pattern)
        patterns.append(pattern)
        pattern = self._rotate_clockwise2(pattern)
        patterns.append(pattern)
        pattern = self._rotate_clockwise2(pattern)
        patterns.append(pattern)
        return patterns


    def _rotate_clockwise2(self, pattern):
        r0, r1, _, r2, r3 = list(pattern)
        return ''.join([r2, r0, '/', r3, r1])


    def _flip_horizontally2(self, pattern):
        r0, r1, _, r2, r3 = list(pattern)
        return ''.join([r1, r0, '/', r3, r2])


    def _flip_vertically2(self, pattern):
        r0, r1, _, r2, r3 = list(pattern)
        return ''.join([r2, r3, '/', r0, r1])


    def _construct_all_patterns3(self):
        '''Construct all 3x3 rotated and flipped patters.'''
        all_patterns = set([self.pattern])
        rotations = self._rotations3(self.pattern)
        all_patterns.update(rotations)
        flip_v = self._flip_vertically3(self.pattern)
        all_patterns.add(flip_v)
        flip_v_rotations = self._rotations3(flip_v)
        all_patterns.update(flip_v_rotations)
        flip_h = self._flip_horizontally3(self.pattern)
        all_patterns.add(flip_h)
        flip_h_rotations = self._rotations3(flip_h)
        all_patterns.update(flip_h_rotations)
        return all_patterns


    def _rotations3(self, pattern):
        '''Construct 3 rotations of pattern.'''
        patterns = []
        pattern = self._rotate_clockwise3(pattern)
        patterns.append(pattern)
        pattern = self._rotate_clockwise3(pattern)
        patterns.append(pattern)
        pattern = self._rotate_clockwise3(pattern)
        patterns.append(pattern)
        return patterns


    def _rotate_clockwise3(self, pattern):
        '''A single rotation clockwise.'''
        r0, r1, r2, _, r3, r4, r5, _, r6, r7, r8 = list(pattern)
        return ''.join([r6, r3, r0, '/', r7, r4, r1, '/', r8, r5, r2])


    def _flip_vertically3(self, pattern):
        '''A vertical flip.'''
        r0, r1, r2, _, r3, r4, r5, _, r6, r7, r8 = list(pattern)
        return ''.join([r6, r7, r8, '/', r3, r4, r5, '/', r0, r1, r2])


    def _flip_horizontally3(self, pattern):
        '''A horizontal flip.'''
        r0, r1, r2, _, r3, r4, r5, _, r6, r7, r8 = list(pattern)
        return ''.join([r2, r1, r0, '/', r5, r4, r3, '/', r8, r7, r6])


def parse_input(input):
    '''Parse input.'''
    return [Pattern(*row.split(' => ')) for row in input.strip().split('\n')]


def find_match(pattern, patterns):
    for test_pattern in patterns:
        if test_pattern.is_match(pattern):
            return test_pattern


def pattern_parts(pattern):
    grid = [list(row) for row in pattern.split('/')]
    # print(grid)
    size = len(grid)
    d = 2 if size % 2 == 0 else 3
    step = int(size / d)
    parts = []
    # print('size', size, 'd', d, 'step', step)
    for row in range(step):
        for col in range(step):
            part = []
            for i in range(d):
                minor_row = d*row + i
                start = d*col
                # print(minor_row, [start, start + d])
                minor_part = grid[minor_row][start:start + d]
                part.append(''.join(minor_part))
            parts.append('/'.join(part))
    return parts


def join_patterns(patterns):
    size = len(patterns)
    d = int(sqrt(size))
    rows = []
    for i in range(d):
        parts = patterns[i*d:i*d + d]
        parts = [part.split('/') for part in parts]
        parts = [''.join(parts) for parts in zip(*parts)]
        parts = '/'.join(parts)
        rows.append(parts)
    return '/'.join(rows)



patterns = parse_input(INPUT)
test_patterns = parse_input(TEST_INPUT)

start = '.#./..#/###'
test_start = '.#./..#/###'
