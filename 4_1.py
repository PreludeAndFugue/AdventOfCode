#!python3

'''Day 4, part 1.'''

from hashlib import md5

key = 'iwrupvqb'
i = 1

while True:
    test = f'{key}{i}'
    hasher = md5()
    hasher.update(test.encode())
    result = hasher.hexdigest()
    if result.startswith('000000'):
        print(i)
        break
    i += 1
