#!python3

'''Day 3, part 2.'''

import data_3

position_1 = (0, 0)
position_2 = (0, 0)

houses = set()
houses.add(position_1)

for move in data_3.INPUT[::2]:
    direction = data_3.MOVES[move]
    position_1 = position_1[0] + direction[0], position_1[1] + direction[1]
    houses.add(position_1)

for move in data_3.INPUT[1::2]:
    direction = data_3.MOVES[move]
    position_2 = position_2[0] + direction[0], position_2[1] + direction[1]
    houses.add(position_2)


print(len(houses))
