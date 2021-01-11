#!python3

'''Day 6'''

INPUT = 'day06.txt'

def parse_input(input):
    rows = (row.strip().split(' ') for row in input.split('\n'))
    commands = []
    for row in rows:
        if len(row) == 4:
            from_ = tuple(map(int, row[1].split(',')))
            to = tuple(map(int, row[3].split(',')))
            commands.append((row[0], from_, to))
        else:
            from_ = tuple(map(int, row[2].split(',')))
            to = tuple(map(int, row[4].split(',')))
            commands.append((row[1], from_, to))
    return commands


def part1(data):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for command in data:
        (x1, y1), (x2, y2) = command[1], command[2]
        instruction = command[0]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if instruction == 'on':
                    grid[x][y] = 1
                elif instruction == 'off':
                    grid[x][y] = 0
                else:
                    grid[x][y] = 1 - grid[x][y]
    return sum(sum(row) for row in grid)


def part2(data):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for command in data:
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

    return sum(sum(row) for row in grid)


def main():
    data = parse_input(open(INPUT, 'r').read().strip())

    p = part1(data)
    print(p)

    p = part2(data)
    print(p)


if __name__ == "__main__":
    main()
