#!python3

INPUT = '''AlphaCentauri to Snowdin = 66
AlphaCentauri to Tambi = 28
AlphaCentauri to Faerun = 60
AlphaCentauri to Norrath = 34
AlphaCentauri to Straylight = 34
AlphaCentauri to Tristram = 3
AlphaCentauri to Arbre = 108
Snowdin to Tambi = 22
Snowdin to Faerun = 12
Snowdin to Norrath = 91
Snowdin to Straylight = 121
Snowdin to Tristram = 111
Snowdin to Arbre = 71
Tambi to Faerun = 39
Tambi to Norrath = 113
Tambi to Straylight = 130
Tambi to Tristram = 35
Tambi to Arbre = 40
Faerun to Norrath = 63
Faerun to Straylight = 21
Faerun to Tristram = 57
Faerun to Arbre = 83
Norrath to Straylight = 9
Norrath to Tristram = 50
Norrath to Arbre = 60
Straylight to Tristram = 27
Straylight to Arbre = 81
Tristram to Arbre = 90'''

import networkx as nx
import matplotlib.pyplot as plt

import re
from itertools import permutations

regex = r'(\w+)\sto\s(\w+) = (\d+)'


def parse_input(input_string):
    lines = input_string.split('\n')
    for line in lines:
        match = re.match(regex, line)
        # print(line)
        # print(match)
        s1, s2, distance = match.groups()
        yield s1, s2, int(distance)


def make_graph(data):
    graph = nx.Graph()
    for s1, s2, distance in data:
        graph.add_edge(s1, s2, weight=distance)
    return graph


def make_data(data):
    locations = set()
    distance_map = dict()
    for l1, l2, distance in data:
        locations.add(l1)
        locations.add(l2)
        distance_map[f'{l1}-{l2}'] = distance
        distance_map[f'{l2}-{l1}'] = distance
    return locations, distance_map


def calc_distance(locations, distance_map):
    distance = 0
    for l1, l2 in zip(locations[:-1], locations[1:]):
        map_key = f'{l1}-{l2}'
        distance += distance_map[map_key]
    return distance


if __name__ == '__main__':
    locations, distance_map = make_data(parse_input(INPUT))
    # for k, v in distance_map.items():
    #     print(k, v)

    min_path = ''
    min_distance = 0
    for perm in permutations(tuple(locations)):
        distance = calc_distance(perm, distance_map)
        if distance > min_distance:
            min_distance = distance
            min_path = perm

    print(min_path)
    print(min_distance)
