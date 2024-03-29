
import pprint

from help import get_input


'''
directory = {
    # sub-directory
    "name": {
        ... sub directories
        "files": total_size
    }
    "files": total_size (don't need to store names)
}

Part 1
------
1190023: too low


Part 2
------
11_285_770: too high

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


def get_current_directory(directory_stack, root):
    directory = root
    for directory_name in directory_stack:
        directory = directory[directory_name]
    return directory


def directory_sizes(directory, path, current_sizes):
    s = directory['files']
    for dir_name, dir_ in directory.items():
        if dir_name == 'files': continue
        s += directory_sizes(dir_, path + '/' + dir_name, current_sizes)
    current_sizes[path] = s
    return s


def make_file_system(s):
    root = {
        'files': 0
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
            get_current_directory(directory_stack, root)[name] = {'files': 0}
        elif line.startswith('$ ls'):
            pass
        elif line[0].isdigit():
            size, _ = line.split(' ')
            size = int(size)
            get_current_directory(directory_stack, root)['files'] += size
    return root


def part1(all_sizes):
    return sum(v for v in all_sizes.values() if v <= 100_000)


def part2(all_sizes):
    total_space = 70_000_000
    unused_space_required = 30_000_000
    used_space = all_sizes['/']
    unused_space = total_space - used_space
    space_required = unused_space_required - unused_space
    return min(n for n in all_sizes.values() if n >= space_required)


def main():
    s = get_input('07').split('\n')
    # s = TEST.strip().split('\n')

    file_system = make_file_system(s)
    all_sizes = {}
    directory_sizes(file_system, '/', all_sizes)

    p1 = part1(all_sizes)
    p2 = part2(all_sizes)

    print('Part 1:', p1)
    print('Part 2:', p2)


if __name__ == '__main__':
    main()
