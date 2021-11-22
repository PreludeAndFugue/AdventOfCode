#!python3

'''2.2'''

from itertools import product

INPUT = '2.txt'

def get_ids():
    '''Get box ids.'''
    ids = []
    with open(INPUT, 'r') as f:
        for line in f:
            ids.append(line)
    return ids
    
    
def get_diff(a, b):
    '''Find indices of differing chars.'''
    indices = []
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            indices.append(i)
    return indices
    
    
def main():
    '''Main entry point.'''
    ids = get_ids()
    for a, b in product(ids, repeat=2):
        diff = get_diff(a, b)
        if len(diff) == 1:
            print(a)
            print(b)
            print(diff)
    
    
if __name__ == '__main__':
    main()
