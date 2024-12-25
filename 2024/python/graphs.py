
def bron_kerbosch(R, P, X, map_):
    '''
    Recursive function to find all maximal cliques.
    R: current clique
    P: potential vertices to add to the clique
    X: vertices already processed
    '''
    if not P and not X:
        yield R
        return

    for v in list(P):
        neighbors = set(map_[v])
        yield from bron_kerbosch(
            R.union({v}),
            P.intersection(neighbors),
            X.intersection(neighbors),
            map_
        )
        P.remove(v)
        X.add(v)


def find_cliques(map_):
    '''Find all maximal cliques in the graph.'''
    P = set(map_.keys())
    R = set()
    X = set()
    return list(bron_kerbosch(R, P, X, map_))
