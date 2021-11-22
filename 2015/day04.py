#!python3

'''Day 4'''

from hashlib import md5


def find(zeros):
    key = 'iwrupvqb'
    i = 1
    while True:
        test = f'{key}{i}'
        hasher = md5()
        hasher.update(test.encode())
        result = hasher.hexdigest()
        if result.startswith(zeros):
            return i
        i += 1


def main():
    p1 = find('00000')
    print(p1)

    p2 = find('000000')
    print(p2)


if __name__ == "__main__":
    main()
