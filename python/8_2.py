#!python

INPUT = '8.txt'

TEST_INPUT = '''2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'''


class Data(object):
    def __init__(self, data):
        self.data = map(int, data.split(' '))
    
    def header(self):
        return Header(next(self.data), next(self.data))
        
    def meta(self, n):
        return [next(self.data) for _ in range(n)]
        
    def items(self):
        return self.data
        
        
class Header(object):
    def __init__(self, child_count, meta_count):
        self.child_count = child_count
        self.meta_count = meta_count
        
    def has_no_children(self):
        return self.child_count == 0
        
    def has_children(self):
        return self.child_count > 0
        
    def remove_child(self):
        self.child_count -= 1
        
    def __repr__(self):
        return f'Header({self.child_count}, {self.meta_count})'
        
        
class Node(object):
    def __init__(self, child_count, meta_data_count):
        self.child_count = child_count
        self.meta_data_count = meta_data_count
        self.children = []
        self.meta_data = []
    

def parse_input(data):
    return list(map(int, data.split(' ')))
    
    
def part2(data):
    data = Data(data)
    
    


def main():
    with open(INPUT, 'r') as f:
        part2(f.read())


def test():
    part2(TEST_INPUT)
    

if __name__ == '__main__':
#    main()
    
    test()
    
    data = graph_writer(graph)
    print(data)
