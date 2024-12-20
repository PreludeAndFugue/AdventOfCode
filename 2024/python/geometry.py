
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

NEXT_DIRECTIONS = {
    UP: [LEFT, RIGHT],
    RIGHT: [UP, DOWN],
    DOWN: [RIGHT, LEFT],
    LEFT: [DOWN, UP]
}


def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)
