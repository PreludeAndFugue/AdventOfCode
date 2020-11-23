#!python3

'''Day 6, part 2.'''

import data_6

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for command in data_6.data:
    (x1, y1), (x2, y2) = command[1], command[2]
    instruction = command[0]
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if instruction == 'on':
                grid[x][y] = grid[x][y] + 1
            elif instruction == 'off':
                grid[x][y] = 0 if grid[x][y] == 0 else grid[x][y] - 1
            else:
                grid[x][y] = grid[x][y] + 2

result = sum(sum(row) for row in grid)
print(result)
