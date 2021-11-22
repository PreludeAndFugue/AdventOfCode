#!python3

'''Day 3.'''

INPUT = 'day03.txt'

MOVES = {
    '^': (0, 1),
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, -1)
}


def part1(moves):
    houses = set()
    position = (0, 0)

    houses.add(position)

    for move in moves:
        direction = MOVES[move]
        position = position[0] + direction[0], position[1] + direction[1]
        houses.add(position)

    return len(houses)


def part2(moves):
    position_1 = (0, 0)
    position_2 = (0, 0)

    houses = set()
    houses.add(position_1)

    for move in moves[::2]:
        direction = MOVES[move]
        position_1 = position_1[0] + direction[0], position_1[1] + direction[1]
        houses.add(position_1)

    for move in moves[1::2]:
        direction = MOVES[move]
        position_2 = position_2[0] + direction[0], position_2[1] + direction[1]
        houses.add(position_2)

    return len(houses)


def main():
    moves = open('day03.txt', 'r').read().strip()

    p1 = part1(moves)
    print(p1)

    p2 = part2(moves)
    print(p2)


if __name__ == "__main__":
    main()
