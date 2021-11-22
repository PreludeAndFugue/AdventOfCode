#!python3

'''
f'{rules[2]}'

'''

import re


TEST_INPUT_2 = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
'''

INPUT = 'day19.txt'

def make_rule(text):
    if text.startswith('"'):
        return text[1]
    new_rule = []
    parts = text.split(' ')
    for part in parts:
        if part.isdigit():
            new_rule.append(f'{{{part}}}')
        else:
            new_rule.append(part)
    if '|' in text:
        new_rule = ['('] + new_rule + [')']
    return ' '.join(new_rule)


def make_rules(text):
    rules = {}
    for line in text.strip().split('\n'):
        n, rule = line.strip().split(': ')
        n = int(n)
        rules[n] = make_rule(rule)
    return rules


def make_rules_list(rules):
    return list(rules.values())


def test1():
    rules = make_rules(TEST_INPUT_2)
    for n, rule in rules.items():
        print(n, rule)

    rules_list = make_rules_list(rules)
    x = rules[0].format(*rules_list)
    while '{' in x:
        x = x.format(*rules_list)
    x = x.replace(' ', '')
    print(x)


def test2():
    text = open(INPUT, 'r').read()
    rules, strings = text.strip().split('\n\n')
    rules = make_rules(rules)
    keys = sorted(rules.keys())
    sorted_rules = [rules[n] for n in keys]
    x = rules[0].format(*sorted_rules)
    while '{' in x:
        x = x.format(*sorted_rules)
    x = x.replace(' ', '')
    regex = re.compile(x)
    count = 0
    for s in strings.strip().split('\n'):
        if regex.match(s):
            count += 1
    print(count)


def main():
    test2()


if __name__ == "__main__":
    main()