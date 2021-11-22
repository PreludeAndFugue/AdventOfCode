#!python3

'''
Iterative deepening depth-first search.'

https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search
'''

def id_dfs(root, get_children, goal):
    for depth in range(0, 1_000_000):
        found, remaining = dls(root, depth, get_children, goal)
        if found is not None:
            return depth, found
        elif not remaining:
            return None


def dls(node, depth, get_children, goal):
    if depth == 0:
        if node == goal:
            return node, True
        else:
            return None, True
    elif depth > 0:
        any_remaining = False
        for child in get_children(node):
            found, remaining = dls(child, depth - 1, get_children, goal)
            if found is not None:
                return found, True
            if remaining:
                any_remaining = True
        return None, any_remaining
