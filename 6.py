#!python3

from collections import Counter

INPUT = '6.txt'
TEST_INPUT = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''.split('\n')


def get_raw_input():
    with open(INPUT, 'r') as f:
        return f.read().strip().split('\n')


def get_points(raw_input):
    points = []
    for line in raw_input:
        point = tuple(map(int, line.strip('\n').split(', ')))
        points.append(point)
    return points
    
    
def get_boundary(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)
    return (min_x, min_y), (max_x, max_y)
    
    
def make_grid(lower, upper):
    grid = []
    for x in range(lower[0], upper[0] + 1):
        for y in range(lower[1], upper[1] + 1):
            p = (x, y)
            grid.append(p)
    return grid
    
    
def distance(p1, p2):
    '''Manhattan distance.'''
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    
def find_nearest(p, points):
    min_distance = 1_000_000
    nearest_points = []
    for q in points:
        d = distance(p, q)
        if d < min_distance:
            nearest_points = [q]
            min_distance = d
        elif d == min_distance:
            nearest_points.append(q)
    return nearest_points
    
    
def find_nearest_on_grid(grid, points):
    results = {}
    for p in grid:
        results[p] = find_nearest(p, points)
    return results
    
    
def remove_duplicates(nearest):
    '''Remove points on grid which have more than one nearest point.'''
    result = {}
    for (key, value) in nearest.items():
        if len(value) == 1:
            result[key] = value
    return result
    
    
def find_boundary_points(nearest, a, b):
    x_min, y_min = a
    x_max, y_max = b
    points = set()
    for p, q in nearest.items():
        if p[0] == x_min or p[0] == x_max or p[1] == y_min or p[1] == y_max:
            points.update(q)
    return points
    
    
def remove_boundary_points(nearest, boundary_points):
    result = {}
    for p, q in nearest.items():
        if not boundary_points.intersection(q):
            result[p] = q[0]
    return result
    
    
def total_distance(p, points):
    total = 0
    for point in points:
        total += distance(p, point)
    return total
    
    
def find_close_points(grid, points, max_distance):
    result = []
    for p in grid:
        if total_distance(p, points) < max_distance:
            result.append(p)
    return result
        
    
    
def main():
    raw_input = get_raw_input()
    points = get_points(raw_input)
    a, b = get_boundary(points)
    grid = make_grid(a, b)
    nearest = find_nearest_on_grid(grid, points)
    nearest = remove_duplicates(nearest)
    boundary_points = find_boundary_points(nearest, a, b)
    nearest = remove_boundary_points(nearest, boundary_points)
    count = Counter(nearest.values())
    print(count.most_common(1))
    
    
def main2():
    raw_input = get_raw_input()
    points = get_points(raw_input)
    a, b = get_boundary(points)
    grid = make_grid(a, b)
    close_points = find_close_points(grid, points, 10_000)
    print(len(close_points))
    
    
def test():
    points = get_points(TEST_INPUT)
    a, b = get_boundary(points)
    grid = make_grid(a, b)
    nearest = find_nearest_on_grid(grid, points)
    nearest = remove_duplicates(nearest)
    boundary_points = find_boundary_points(nearest, a, b)
    nearest = remove_boundary_points(nearest, boundary_points)
    count = Counter(nearest.values())
    print(count.most_common(1))
    
    
def test2():
    points = get_points(TEST_INPUT)
    a, b = get_boundary(points)
    grid = make_grid(a, b)
    close_points = find_close_points(grid, points, 32)
    print(len(close_points))
    
    
if __name__ == '__main__':
#    test()
#    main()
    
    test2()
    main2()
