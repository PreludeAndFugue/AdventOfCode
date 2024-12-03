
from help import get_input

test1 = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''


safe = 0
for line in get_input(2).strip().split('\n'):
# for line in test1.strip().split('\n'):ls
    ns = [int(n) for n in line.split()]
    direction = None
    large = False
    for n1, n2 in zip(ns, ns[1:]):
        dn = n1 - n2
        if dn < 0:
            d = False
        elif dn > 0:
            d = True
        if direction is not None:
            if d != direction:
                direction = None
                break
        else:
            direction = d

        m = abs(dn)
        if m < 1 or m > 3:
            large = True
            break

    if not large and direction is not None:
        safe += 1

print(safe)

