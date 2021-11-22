#!python3

'''Day 24, part 1.'''

from data_24 import test_components, components, Component, Node, Container


def next_components(value, components):
    next_c = []
    for c in components:
        if value in c:
            next_c.append(c)
    return tuple(next_c)


def remove_component(component, components):
    return tuple(c for c in components if c != component)


def rotate_component(value, component):
    if component[0] == value:
        return component
    else:
        return component[1], component[0]


def max_path(path, components, all_paths):
    current_component = path[-1]
    next_value = current_component[1]
    next_coms = next_components(next_value, components)

    if not next_coms:
        all_paths.append(path)

    # print(current_component)
    # print(next_coms)

    for next_component in next_coms:
        new_components = remove_component(next_component, components)

        if not new_components:
            all_paths.append(path)
            continue

        rotated_component = rotate_component(next_value, next_component)
        new_path = path + (rotated_component, )
        max_path(new_path, new_components, all_paths)


def path_length(path):
    return sum(sum(x) for x in path)


def strongest_path(paths):
    return max(path_length(path) for path in paths)


if __name__ == '__main__':
    start = (0, 0)
    print(start)

    path = (start, )
    all_paths = []
    max_path(path, components, all_paths)

    value = strongest_path(all_paths)
    print(value)


    max_path_length = len(max(all_paths, key=lambda path: len(path)))
    print('max path length', max_path_length)

    max_length_paths = [path for path in all_paths if len(path) == max_path_length]

    max_length_values = [path_length(path) for path in max_length_paths]

    print(max_length_values)
    print(max(max_length_values))
