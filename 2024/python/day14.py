import re

from PIL import Image, ImageDraw, ImageFont

from help import get_input

test1 = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''

p = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
r = re.compile(p)

def parse(source):
    for line in source.split('\n'):
        m = r.match(line)
        x = int(m.group(1))
        y = int(m.group(2))
        vx = int(m.group(3))
        vy = int(m.group(4))
        # print(x, y, vx, vy)
        yield (x, y), (vx, vy)


def move(p, v, t):
    x, y = p
    dx, dy = v
    for _ in range(t):
        x += dx
        y += dy
        x = x % X
        y = y % Y
    return (x, y), v


def single_move_all(robots):
    return [move(p, v, 1) for p, v in robots]


def quadrant_count(robots):
    XX = X // 2
    YY = Y // 2
    # print(X, Y, XX, YY)
    count = {1: 0, 2: 0, 3: 0, 4: 0}
    seen = set()
    for p, _ in robots:
        if p in seen:
            continue
        seen.add(p)
        x, y = p
        if x == XX or y == YY:
            continue
        if y < YY:
            if x < XX:
                count[1] += 1
            else:
                count[2] += 1
        else:
            if x < XX:
                count[3] += 1
            else:
                count[4] += 1

    result = 1
    # print(count)
    if count[1] == count[2] and count[3] == count[4]:
        return True
    return False
    # for v in count.values():
    #     result *= v
    # return result

font = ImageFont.truetype("Andale Mono.ttf", size=8)


def print_robots(robots, i):
    robots = set(robots)
    rows = []
    for y in range(Y):
        row = []
        for x in range(X):
            p = x, y
            if p in robots:
                row.append('█')
            else:
                row.append(' ')
        rows.append(''.join(row))
    x = '\n'.join(rows)
    # with open(f'day14_{i}.txt', 'w') as f:
    #     f.write(x)

    image = Image.new('RGB', (550, 1280))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), x, font=font, fill=(255, 255, 255))
    image.save(f'14/day14_{i}.png')


# X, Y = 11, 7
# source = test1.strip()

X, Y = 101, 103
source = get_input(14)

robots = list(parse(source))

# for p, v in robots:
    # pp, v = move(p, v, 100)


Z = 10_500

D1_START = 14
D1_DIFF = 101

D2_START = 94
D2_DIFF = 103

symmetries = set()
for i in range(Z):
    robots = single_move_all(robots)
    r = [p for p, v in robots]
    # n = quadrant_count(robots)
    if i + 1 == D1_START:
        print_robots(r, i + 1)
        D1_START += D1_DIFF
        # input()
    if i + 1 == D2_START:
        print_robots(r, i + 1)
        D2_START += D2_DIFF
        # input()

