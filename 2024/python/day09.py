
from help import get_input

test1 = '''12345'''

test2 = '''2333133121414131402'''

def expand(source):
    result = []
    for i, n in enumerate(source):
        n = int(n)
        if i % 2 == 0:
            result.append(n * f'{i // 2}')
        else:
            result.append(n * '.')
    return ''.join(result)


def compact(disk_map):
    file_position = 0
    file_no = 0
    file_size = disk_map[file_position]

    space_position = 1
    space_size = disk_map[space_position]

    l = len(disk_map)

    last_file_position = l - 1
    last_file_no = l // 2
    last_file_size = disk_map[last_file_position]

    # print(disk_map)
    # print(file_no, file_position, file_size)
    # print(space_position, space_size)
    # print(last_file_position, last_file_no, last_file_size)

    compacting = True

    while compacting:
        if file_no == last_file_no:
            for _ in range(last_file_size):
                yield last_file_no
            break
        if file_no > last_file_no:
            break
        # the current file
        # print('the current file', file_no, file_size)
        for _ in range(file_size):
            yield file_no

        # update the current file
        file_no += 1
        file_position += 2
        file_size = disk_map[file_position]

        # fill space from the last file
        # print('fill space')
        while space_size:
            # print('last file', last_file_no, last_file_size)
            if last_file_size:
                yield last_file_no
                last_file_size -= 1
                space_size -= 1
            else:
                last_file_position -= 2
                last_file_no -= 1
                last_file_size = disk_map[last_file_position]
                if last_file_no <= file_no:
                    compacting = False
                    break

        if compacting:
            # current space filled, find next space
            space_position += 2
            space_size = disk_map[space_position]
            # print('moving to next space', space_position, space_size)

        # input()


# source = test1.strip()
# source = test2.strip()
source = get_input(9)

disk_map = list(map(int, source))
t = 0
for i, n in enumerate(compact(disk_map)):
    t += i * n
print(t)

