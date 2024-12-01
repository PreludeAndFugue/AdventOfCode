base_path = '../day{:02d}.txt'

def get_input(d):
    path = base_path.format(d)
    return open(path, 'r').read().strip()
