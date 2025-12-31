
from queue import Queue

test = '''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''


source = test.strip()
source = open('day11.txt', 'r').read().strip()

map_ = {}
for line in source.split('\n'):
    l1, l2 = line.split(': ')
    l2 = l2.split(' ')
    map_[l1] = l2
# print(map_)


with open('graph11.txt', 'w') as f:
    for k, v in map_.items():
        for w in v:
            # print(k, '->', w)
            f.write(f'{k} -> {w}\n')


def part1():
    q = Queue()
    q.put('you')
    count = 0
    while not q.empty():
        v = q.get()
        if v == 'out':
            count += 1
            continue
        for w in map_[v]:
            q.put(w)

    print(count)


part1()
