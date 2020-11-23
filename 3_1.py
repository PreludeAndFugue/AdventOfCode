#!python3

'''Day 3, part 1.'''

import data_3

houses = set()
position = (0, 0)

houses.add(position)

for move in data_3.INPUT:
    direction = data_3.MOVES[move]
    position = position[0] + direction[0], position[1] + direction[1]
    houses.add(position)

print(len(houses))
