
from itertools import cycle

from help import get_input


def parse(d):
    '''Get frequency changes from file.'''
    changes = []
    for line in d.split('\n'):
        changes.append(int(line))
    return changes


def main():
    d = get_input('01').strip()
    changes = parse(d)

    p1 = sum(changes)
    print(p1)

    current_value = 0
    values = set([current_value])
    for n in cycle(changes):
        new_value = current_value + n
        if new_value in values:
            break
        values.add(new_value)
        current_value = new_value

    print(new_value)


if __name__ == '__main__':
    main()