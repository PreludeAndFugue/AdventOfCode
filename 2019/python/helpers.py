BASE = '/Users/gary/Documents/computing/_AdventOfCode/2019/'

def manhattan_distance_2(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return abs(x1 - x2) + abs(y1 - y2)
