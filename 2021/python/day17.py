#!python3

from math import sqrt

TEST_TARGET = range(20, 30 + 1), range(-10, -5 + 1)
TARGET = range(144, 178 + 1), range(-100, -76 + 1)


def f(x, y, dx, dy):
    x += dx
    y += dy
    if dx > 0:
        dx -= 1
    elif dx < 0:
        dx -= 1
    return x, y, dx, dy - 1


def calculate_steps(dx, dy, target_x, target_y):
    '''
    Calculate the maximum number of steps needed to check if the initial velocity
    (dx, dy) will end up in the target.
    '''
    max_x = max(target_x)
    steps_x = 1
    x = 0
    while x <= max_x:
        if dx == 0:
            break
        x += dx
        dx -= 1
        steps_x += 1
    min_y = min(target_y)
    steps_y = 1
    y = 0
    while y >= min_y:
        y += dy
        dy -= 1
        steps_y += 1
    return max(steps_x, steps_y)


def check(dx, dy, target_x, target_y):
    x, y = 0, 0
    steps = calculate_steps(dx, dy, target_x, target_y)
    for _ in range(steps):
        x, y, dx, dy = f(x, y, dx, dy)
        if x in target_x and y in target_y:
            return True
    return False


def part1(target):
    _ , ty = target
    y_max = abs(min(ty))
    return sum(range(y_max))


def part2(target):
    tx, ty = target
    # Solve 1/2n(n+1) >= min(tx) for n will find the smallest x velocity that will
    # reach the target before friction stops the x motion.
    x_min = int(sqrt(2 * min(tx) + 0.25) + 0.5)
    x_max = max(tx)
    y_min = min(ty)
    y_max = abs(min(ty))
    vs = []
    for dy in range(y_min, y_max + 1):
        for dx in range(x_min, x_max + 1):
            result = check(dx, dy, tx, ty)
            if result:
                vs.append((dx, dy))
    return len(vs)


def main():
    t1 = part1(TEST_TARGET)
    assert t1 == 45

    p1 = part1(TARGET)
    print(f'Part 1: {p1}')

    t2 = part2(TEST_TARGET)
    assert t2 == 112

    p2 = part2(TARGET)
    print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
