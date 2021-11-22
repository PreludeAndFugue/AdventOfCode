#!python

'''
Trying a list where the number at index i is the number that comes
next in the ring

Ring: 389125467

List: [0, 2, 5, 8, 6, 4, 7, 3, 8, 9, 1]
(Ignore zero index.)
'''

INPUT = '792845136'
TEST_INPUT = '389125467'


def make_list(input):
    l = [0] * (len(input) + 1)
    ns = list(map(int, list(input)))
    for m, n in zip(ns, ns[1:] + [ns[0]]):
        # print(m, n)
        l[m] = n
    # print(ns[-1], ns[0])
    # l[ns[-1]] = l[ns[0]]
    return l


def make_list2(input):
    l = [i + 1 for i in range(1_000_001)]
    ns = list(map(int, list(input)))
    for m, n in zip(ns, ns[1:]):
        l[m] = n
    l[-1] = ns[0]
    l[ns[-1]] = 10
    return l


def get_destination(current_value, removed_values, size):
    i = (current_value - 2) % size
    while (i + 1) in removed_values:
        i  = (i - 1) % size
    # print('destination:', i + 1)
    return i + 1


def move_list(l, n, size):
    remove_start = l[n]
    remove_middle = l[remove_start]
    remove_end = l[remove_middle]
    remove_all = [remove_start, remove_middle, remove_end]
    # print(remove_all)

    after_remove_end = l[remove_end]
    # print('after end', after_remove_end)
    destination = get_destination(n, remove_all, size)
    # print('destination', destination)

    destination_end = l[destination]
    # print('destination_end', destination_end)
    l[n] = after_remove_end
    l[destination] = remove_start
    l[remove_end] = destination_end


def print_list(l, start):
    values = [start]
    n = start
    while l[n] != start:
        values.append(l[n])
        n = l[n]
    print(l)
    print(values)


def answer1(l):
    values = []
    n = 1
    while l[n] != 1:
        values.append(l[n])
        n = l[n]
    return ''.join(map(str, values))


def test1():
    l = make_list(TEST_INPUT)
    size = 9
    n = 3
    for _ in range(10):
        move_list(l, n, size)
        n = l[n]
    assert answer1(l) == '92658374'


def test2():
    l = make_list(TEST_INPUT)
    size = 9
    n = 3
    for _ in range(100):
        move_list(l, n, size)
        n = l[n]
    assert answer1(l) == '67384529'


def part1():
    l = make_list(INPUT)
    size = 9
    n = 7
    for _ in range(100):
        move_list(l, n, size)
        n = l[n]
    return answer1(l)


def test3():
    l = make_list2(TEST_INPUT)
    size = 1_000_000
    n = 3
    for _ in range(10_000_000):
        move_list(l, n, size)
        n = l[n]

    x = l[1]
    y = l[x]
    assert x * y == 149245887792


def part2():
    l = make_list2(INPUT)
    size = 1_000_000
    n = 7
    for _ in range(10_000_000):
        move_list(l, n, size)
        n = l[n]

    x = l[1]
    y = l[x]
    return x * y

def main():
    test1()
    test2()

    p = part1()
    print(p)

    # test3()

    p = part2()
    print(p)


if __name__ == "__main__":
    main()
