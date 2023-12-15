
from collections import defaultdict, OrderedDict

from help import get_input

TEST = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''


d = get_input('15').strip()
# d = TEST.strip()

def hash(value):
    current_value = 0
    for ch in value:
        current_value += ord(ch)
        current_value *= 17
        current_value %= 256
    return current_value


p1 = 0
boxes = defaultdict(OrderedDict)
for step in d.split(','):
    h = hash(step)
    p1 += h

    if '=' in step:
        l, f = step.split('=')
        f = int(f)
        h = hash(l)
        boxes[h][l] = f
    else:
        l = step.split('-')[0]
        h = hash(l)
        box = boxes[h]
        if l in box:
            del box[l]

p2 = 0
for i in range(256):
    box = boxes[i]
    slot = 0
    for l, f in box.items():
        slot += 1
        p2 += (i + 1)*slot*f


print(p1)

print(p2)
