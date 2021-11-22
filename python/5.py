#!python3

from string import ascii_lowercase, ascii_uppercase

INPUT = '5.txt'

def get_input():
    with open(INPUT, 'r') as f:
        return f.read().strip('\n')
        
        
        
def strip_pairs(p):
    initial_length = len(p)
    for lower, upper in zip(ascii_lowercase, ascii_uppercase):
        p = p.replace(f'{lower}{upper}', '')
        p = p.replace(f'{upper}{lower}', '')
    final_length = len(p)
    return p, final_length != initial_length
    
    
def react(p):
    while True:
        p, change = strip_pairs(p)
        if not change:
            break
    return p
    
    
def remove_pair(p, a, b):
    return p.replace(a, '').replace(b, '')
        

def main():
    p = get_input()
    p = react(p)
    print(len(p))
    
    
def main2():
    p = get_input()
    lengths = []
    for lower, upper in zip(ascii_lowercase, ascii_uppercase):
        q = remove_pair(p, lower, upper)
        q = react(q)
        lengths.append(len(q))
    print(min(lengths))
    
    
    
def test():
    p = 'dabAcCaCBAcCcaDA'
    p = react(p)
    print(p)
    print(len(p))
    
    
if __name__ == '__main__':
    test()
    main()
    main2()
