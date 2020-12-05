#!python
'''
2 3
    0 3 
        m: 10 11 12
    1 1
        0 1
            m: 99
        m: 2
    m: 1 1 2
'''

INPUT = '8.txt'

TEST_INPUT = '''2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'''

READ_HEADER = 0
READ_META_ITEMS = 1
PARSE_HEADER = 2

STATE_DESCRIPTION = {
    READ_HEADER: 'read header',
    READ_META_ITEMS: 'read meta items',
    PARSE_HEADER: 'parse header'
}


class Data(object):
    def __init__(self, data):
        self.data = map(int, data.split(' '))
    
    def header(self):
        return Header(next(self.data), next(self.data))
        
    def meta(self, n):
        return [next(self.data) for _ in range(n)]
        
        
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


def parse_input(data):
    return list(map(int, data.split(' ')))
    
    
def machine(data):
    '''States
        0: read header
        1: read meta items
        2: parse header
    '''
    headers = []
    state = READ_HEADER
    meta_items = []
    
    while True:
        if state == READ_HEADER:
            header = data.header()
            headers.append(header)
            state = PARSE_HEADER
        
        elif state == PARSE_HEADER:
            if not headers: 
                break
            header = headers.pop()
            if header.has_no_children():
                state = READ_META_ITEMS
            else:
                state = READ_HEADER
            headers.append(header)
            
        elif state == READ_META_ITEMS:
            header = headers.pop()
            meta_items.extend(data.meta(header.meta_count))
            if header.has_children():
                header.remove_child()
                headers.append(header)
            else:
                if headers:
                    header = headers.pop()
                    header.remove_child()
                    headers.append(header)
                
            state = PARSE_HEADER

    return meta_items
        
    
def part1(data):
    data = Data(data)
    meta_items = machine(data)
    print(sum(meta_items))
    
    
def main():
    with open(INPUT, 'r') as f:
        part1(f.read())
    
    
def test():
    part1(TEST_INPUT)
    
    
if __name__ == '__main__':
    main()
    
    test()
