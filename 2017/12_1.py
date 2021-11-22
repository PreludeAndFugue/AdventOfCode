#!python3

'''Day 12, part 1.'''

from data_12 import graph, test_graph


def find_connected_component(graph, start):
    '''Find the connected component of the graph starting from start.'''
    connected_component = set([start])
    seen_items = set([start])
    next_items = set(graph[start])
    while next_items:
        item = next_items.pop()
        if item in seen_items:
            continue
        seen_items.add(item)
        connected_component.add(item)
        neighbours = graph[item]
        for neighbour in neighbours:
            if neighbour not in seen_items:
                next_items.add(neighbour)
    return connected_component


def main():
    '''Main entry point.'''
    print(graph)

    connected_component = find_connected_component(graph, 0)
    print(connected_component)
    print(len(connected_component))

if __name__ == '__main__':
    main()
