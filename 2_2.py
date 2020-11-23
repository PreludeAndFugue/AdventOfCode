#!python3

'''Day 2, part 2.'''

import data_2


def ribbon(box):
    '''Length of ribbon for box.'''
    a, b, _ = box
    return 2*(a + b)


def bow(box):
    '''Length for bow.'''
    a, b, c = box
    return a*b*c


def main():
    '''Main entry point.'''
    data = data_2.data
    total = sum(ribbon(box) + bow(box) for box in data)
    print(total)


if __name__ == '__main__':
    main()
