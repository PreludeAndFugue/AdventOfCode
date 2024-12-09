
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

    compacting = True

    while compacting:
        if file_no == last_file_no:
            for _ in range(last_file_size):
                yield last_file_no
            break
        if file_no > last_file_no:
            break

        # the current file
        for _ in range(file_size):
            yield file_no

        # update the current file
        file_no += 1
        file_position += 2
        file_size = disk_map[file_position]

        # fill space from the last file
        while space_size:
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


def compact2(disk_map):
    new_disk_map = []
    for i, n in enumerate(disk_map):
        if i % 2 == 0:
            new_disk_map.append((i // 2, n))
        else:
            new_disk_map.append((-1, n))

    files_to_check = reversed(new_disk_map[2::2])
    for file_no, file_size in files_to_check:
        update = False
        for i, item in enumerate(new_disk_map):
            if item[0] == file_no:
                break
            if item[0] == -1:
                space = item[1]
                if space >= file_size:
                    new_space = space - file_size
                    update = True
                    break

        if update:
            new_disk_map.insert(i, (file_no, file_size))
            new_disk_map.pop(i + 1)
            if new_space:
                new_disk_map.insert(i + 1, (-1, new_space))

    seen = set()
    for file_no, file_size in new_disk_map:
        if file_no != -1 and file_no not in seen:
            seen.add(file_no)
            for _ in range(file_size):
                yield file_no
        else:
            for _ in range(file_size):
                yield -1


def part1():
    # source = test1.strip()
    # source = test2.strip()
    source = get_input(9)

    disk_map = list(map(int, source))
    t = 0
    for i, n in enumerate(compact(disk_map)):
        t += i * n
    print(t)


def part2():
    # source = test2.strip()
    source = get_input(9)

    disk_map = list(map(int, source))
    compact2(disk_map)

    t = 0
    for i, n in enumerate(compact2(disk_map)):
        if n != -1:
            t += i * n
    print(t)


# part1()
part2()
