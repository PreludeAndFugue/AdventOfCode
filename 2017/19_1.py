#!python3

'''Day 19, part 1.'''

from collections import namedtuple

from data_19 import grid, test_grid

Position = namedtuple('Position', ['row', 'col'])
Direction = namedtuple('Direction', ['row', 'col'])


class GridTraverser(object):
    '''Traverse a path.'''

    HORIZONTAL_DIRECTIONS = (Direction(0, 1), Direction(0, -1))
    VERTICAL_DIRECTIONS = (Direction(1, 0), Direction(-1, 0))

    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.running = True
        self.collected_letters = []
        self.steps = 0


    def traverse(self):
        '''Traverse the path.'''
        position = self._find_start()
        direction = Direction(1, 0)
        item = '|'
        while True:
            print(item, position, direction)
            self.steps += 1
            position = self._next_position(position, direction)
            item = self._next_item(position)
            if item == ' ':
                break
            if item.isalpha():
                self.collected_letters.append(item)
            direction = self._next_direction(item, position, direction)



    def _find_start(self):
        '''Find the start position on the grid.'''
        for i, item in enumerate(self.grid[0]):
            if item == '|':
                return Position(0, i)


    def _next_position(self, position, direction):
        '''Get next position.'''
        return Position(position.row + direction.row, position.col + direction.col)


    def _next_item(self, position):
        '''get next item.'''
        return self.grid[position.row][position.col]


    def _next_direction(self, item, position, current_direction):
        '''Get the next direction.'''
        if item in ('-', '|') or item.isalpha():
            return current_direction
        if item == '+':
            return self._find_direction_change(position, current_direction)


    def _find_direction_change(self, position, current_direction):
        '''Find a change in direction.'''
        if current_direction in self.HORIZONTAL_DIRECTIONS:
            test_directions = self.VERTICAL_DIRECTIONS
        else:
            test_directions = self.HORIZONTAL_DIRECTIONS
        for test_direction in test_directions:
            new_row = position.row + test_direction.row
            new_col = position.col + test_direction.col
            test_position = Position(new_row, new_col)
            test_item = self._test_item(test_position)
            if test_item is not None:
                return test_direction


    def _test_item(self, position):
        '''Try to get an item at position.'''
        if position.row < 0 or position.row >= self.rows:
            return None
        if position.col < 0 or position.col >= self.cols:
            return None
        item = self._next_item(position)
        if item == ' ':
            return None
        return item


if __name__ == '__main__':
    for row in test_grid:
        print(row)

    gt = GridTraverser(grid)
    gt.traverse()
    print(''.join(gt.collected_letters))
    print(gt.steps)
