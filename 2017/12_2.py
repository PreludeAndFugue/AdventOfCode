#!python3

'''Day 12, part 2.'''

from data_12 import graph, test_graph


def node_component(node, components):
    '''Is a node in one of the components.'''
    for component in components:
        if node in component:
            return component
    return None


def find_connected_component(graph, start):
    '''Find a connected component of graph.'''
    connected = set()
    seen_nodes = set()
    next_nodes = set([start])
    while next_nodes:
        next_node = next_nodes.pop()
        if next_node in seen_nodes:
            continue
        seen_nodes.add(next_node)
        connected.add(next_node)
        neighbours = graph[next_node]
        for neighbour in neighbours:
            if neighbour not in seen_nodes:
                next_nodes.add(neighbour)
    return connected


def find_components(graph, start):
    '''Find all components of the graph.'''
    all_nodes = set(node for node in graph.keys())
    components = []
    while all_nodes:
        next_node = all_nodes.pop()
        component = find_connected_component(graph, next_node)
        components.append(component)
        all_nodes = all_nodes - component
    return components


def main():
    '''Main entry point.'''
    component = find_connected_component(graph, 0)
    print(component)
    print(len(component))

    components = find_components(graph, 0)
    print(components)
    print(len(components))


if __name__ == '__main__':
    main()
