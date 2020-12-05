#!python3

'''1.1'''

INPUT = '1_1.txt'


total = 0

with open(INPUT, 'r') as f:
    for line in f:
        total += int(line)
        
print(total)