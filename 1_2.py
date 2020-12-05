#!python

'''1.2'''

from itertools import cycle


INPUT = '1_1.txt'


def get_changes():
    '''Get frequency changes from file.'''
    changes = []
    with open(INPUT, 'r') as f:
        for line in f:
            changes.append(int(line))
    return changes
    
    
def main():
    '''Main entry point.'''
    changes = get_changes()
    current_value = 0
    values = set([current_value])
    for n in cycle(changes):
        new_value = current_value + n
#        print(values)
#        print(n, new_value)
        if new_value in values:
            print(new_value)
            break
        values.add(new_value)
        current_value = new_value
    
    
if __name__ == '__main__':
    main()
