BASE = '/Users/gary/Documents/computing/_AdventOfCode/2021/'

def get_ints(filename):
    with open(BASE + filename, 'r') as f:
        for line in f:
            yield int(line)
