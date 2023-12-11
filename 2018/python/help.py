base_path = '../day{}.txt'

def get_input(d):
    path = base_path.format(d)
    return open(path, 'r').read().strip()
