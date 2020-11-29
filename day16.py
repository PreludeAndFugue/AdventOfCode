#!python3

INPUT = '10001110011110000'
LENGTH = 272

TEST_INPUT = '10000'
TEST_LENGTH = 20

LENGTH_2 = 35_651_584

def lengthen(data, n):
    while len(data) < n:
        data = modified_dg(data)
    return data[:n]


def modified_dg(data):
    other = ''.join('0' if x == '1' else '1' for x in data)[::-1]
    return f'{data}0{other}'


def checksum_step(data):
    result = []
    for i in range(0, len(data), 2):
        x = data[i:i + 2]
        if x == x[::-1]:
            result.append('1')
        else:
            result.append('0')
    return ''.join(result)


def checksum(data):
    while len(data) % 2 == 0:
        data = checksum_step(data)
    return data


def main():
    data = lengthen(INPUT, LENGTH_2)
    x = checksum(data)
    print(x)


if __name__ == '__main__':
    main()
