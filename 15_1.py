#!python3

'''Day 15, part 1.'''

import re

INPUT = '''Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8'''

regex = r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)'


def parse_input(input_string):
    results = []
    for row in input_string.strip().split('\n'):
        name, c, d, f, t, cal = re.match(regex, row).groups()
        results.append((name, int(c), int(d), int(f), int(t), int(cal)))
    return results


def brute_force(n, depth):
    # print('brute force', n, depth)
    # input()
    if depth == 1:
        yield (n, )
    else:
        for i in range(n + 1):
            for part in brute_force(n - i, depth - 1):
                yield (i, ) + part


def calculate_property_sum(parts, index, data):
    total = sum(part*item[index] for part, item in zip(parts, data))
    if total < 0:
        return 0
    return total


if __name__ == '__main__':
    data = parse_input(INPUT)
    # print(data)
    max_total = 0
    max_combo = None
    for parts in brute_force(100, 4):
        #  print(parts)
         capacity = calculate_property_sum(parts, 1, data)
         durability = calculate_property_sum(parts, 2, data)
         flavor = calculate_property_sum(parts, 3, data)
         texture = calculate_property_sum(parts, 4, data)
         calories = calculate_property_sum(parts, 5, data)

         # part 2
         if calories != 500:
             continue

         total = capacity * durability * flavor * texture
         if total > max_total:
             max_total = total
             max_combo = parts
    print(max_total, max_combo)
