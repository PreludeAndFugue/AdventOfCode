
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
for step in d.split(','):
    h = hash(step)
    p1 += h
print(p1)
