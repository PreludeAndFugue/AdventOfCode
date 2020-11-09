#!python3

'''
Bot = {
    id: 100,
    values: [],
    low: ('bot', 15),
    high: ('output', 1),
    old_values: []
}
'''


from collections import defaultdict
from random import choice
import re

SOURCE = 'day10.txt'

TEST1 = '''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''


PATTERN_VALUE = r'value (\d+) goes to bot (\d+)'
PATTERN_BOT = r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)'

p1 = re.compile(PATTERN_VALUE)
p2 = re.compile(PATTERN_BOT)


def configure_bots(lines):
    bots = {}
    for line in lines:
        m1 = p1.match(line)
        m2 = p2.match(line)
        assert (m1 is not None) or (m2 is not None)
        if m1:
            value, bot_id = m1.groups()
            if bot_id in bots:
                bots[bot_id]['values'].append(value)
            else:
                bot = {
                    'id': bot_id,
                    'values': [value],
                    'low': None,
                    'high': None
                }
                bots[bot_id] = bot

        if m2:
            bot_id, low, low_id, high, high_id = m2.groups()
            if bot_id in bots:
                bots[bot_id]['low'] = (low, low_id)
                bots[bot_id]['high'] = (high, high_id)
            else:
                bot = {
                    'id': bot_id,
                    'values': [],
                    'low': (low, low_id),
                    'high': (high, high_id)
                }
                bots[bot_id] = bot
    return bots


def get_bot(bots):
    '''Gets bot with 2 values.'''
    for bot in bots.values():
        if len(bot['values']) == 2:
            return bot
    return None


def hand_over_type(type, id, value, bots, outputs):
    if type == 'bot':
        b = bots[id]
        b['values'].append(value)
    else:
        outputs[id].append(value)


def hand_over(bot, bots, outputs):
    '''bot gives its values to other bots.'''
    low_type, low_id = bot['low']
    high_type, high_id = bot['high']
    low_value, high_value = sorted(bot['values'])
    hand_over_type(low_type, low_id, low_value, bots, outputs)
    hand_over_type(high_type, high_id, high_value, bots, outputs)
    bot['values'] = []
    bot['old_values'] = [low_value, high_value]


def find_bot(values, bots):
    found = []
    for bot in bots.values():
        if sorted(bot['old_values']) == values:
            found.append(bot)
    return found


def run(bots, outputs):
    while True:
        bot = get_bot(bots)
        if bot is None:
            return
        hand_over(bot, bots, outputs)


def main():
    lines = open(SOURCE, 'r').read().strip().split('\n')
    bots = configure_bots(lines)
    outputs = defaultdict(list)
    run(bots, outputs)
    # for b in bots.values():
    #     print(b)
    found = find_bot(['17', '61'], bots)
    print(found)
    print(outputs)


def test1():
    lines = TEST1.strip().split('\n')
    bots = configure_bots(lines)
    outputs = defaultdict(list)
    run(bots, outputs)
    found = find_bot(['2', '5'], bots)
    print(found)


if __name__ == '__main__':
    test1()
    main()
