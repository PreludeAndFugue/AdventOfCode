#!python3

'''4.1'''

INPUT = '4.txt'


def get_input():
    records = []
    with open(INPUT, 'r') as f:
        for line in f:
            records.append(line)
    return sorted(records)
    
    
def main():
    for record in get_input():
        print(record)
    
    
if __name__ == '__main__':
    main()
