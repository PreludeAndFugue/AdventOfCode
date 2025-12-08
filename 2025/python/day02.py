
from help import get_input

TEST1 = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''

source = get_input(2)
# source = TEST1.strip()

total = 0
m = 0
for _range in  source.split(','):
    # print(_range)
    a, b = _range.split('-')
    a = int(a)
    b = int(b)
    for n in range(a, b + 1):
        s = str(n)
        l = len(s)
        if l % 2 != 0:
            continue
        x, y = s[:l//2], s[l//2:]
        if x == y:
            total += 1
            m += n


print(total)
print(m)