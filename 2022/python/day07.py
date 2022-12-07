
import pprint

from help import get_input


'''
directory = {
    # sub-directory
    "name": {
        ... sub directories
        "files": [...]
    }
    "files": [(size, name), ...]
}


1190023: too low

'''

TEST = '''
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''

def insert_file(file_details, directory_stack, root):
    directory = root
    for directory_name in directory_stack:
        directory = directory[directory_name]
    directory['files'].append(file_details)


def insert_directory(name, directory_stack, root):
    directory = root
    for directory_name in directory_stack:
        directory = directory[directory_name]
    directory[name] = {'files': []}


def directory_sizes(directory, directory_name, path, current_sizes):
    s = sum(size for size, _ in directory['files'])
    for dir_name, dir_ in directory.items():
        if dir_name == 'files': continue
        s += directory_sizes(dir_, dir_name, path + '/' + dir_name, current_sizes)

    current_sizes[path + directory_name] = s
    return s


def part1(s):
    root = {
        'files': []
    }
    directory_stack = []
    for line in s:
        if line.startswith('$ cd'):
            directory = line.split(' ')[2]
            if directory == '..':
                directory_stack.pop()
            elif directory == '/':
                directory_stack = []
            else:
                directory_stack.append(directory)
        elif line.startswith('dir'):
            name = line.split(' ')[1]
            insert_directory(name, directory_stack, root)
        elif line.startswith('$ ls'):
            # do nothing
            continue
        elif line[0].isdigit():
            size, name = line.split(' ')
            size = int(size)
            insert_file((size, name), directory_stack, root)

    all_sizes = {}
    directory_sizes(root, '/', '', all_sizes)

    total = 0
    for v in all_sizes.values():
        if v <= 100_000:
            total += v
    return total


def main():
    s = get_input('07').split('\n')
    # s = TEST.strip().split('\n')

    p1 = part1(s)

    print('Part 1:', p1)


if __name__ == '__main__':
    main()
