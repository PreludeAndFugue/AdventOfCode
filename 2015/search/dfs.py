#!python3

'''
Depth-first search.

https://en.wikipedia.org/wiki/Depth-first_search
'''

def dfs_iterative(start, get_children, goal):
    seen = set()
    stack = []
    item = start, 0
    stack.append(item)
    while stack:
        node, depth = stack.pop()
        print(depth)

        if node == goal:
            return node, depth
        if len(node) < len(goal):
            seen.add(node)
            continue

        if node not in seen:
            seen.add(node)
            for child in get_children(node):
                if child not in seen:
                    item = child, depth + 1
                    stack.append(item)
