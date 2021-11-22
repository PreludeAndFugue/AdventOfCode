#!python3

'''Data for day 9.'''

from enum import Enum

INPUT = 'data_9.txt'

data = open(INPUT, 'r').read()

def process_normal(ch):
    '''Process a character in normal state.'''
    if ch == '!':
        return State.IGNORE, None
    if ch == '<':
        return State.GARGABE, None
    return State.NORMAL, ch


def process_garbage(ch):
    '''Process a character in garbage state.'''
    if ch == '!':
        return State.IGNORE_IN_GARBAGE, None
    if ch == '>':
        return State.NORMAL, None
    return State.GARGABE, None


def process_ignore(ch):
    '''Process a character in ignore state.'''
    return State.NORMAL, None


def process_ignore_in_garbage(ch):
    '''Process a character in ignore state which is in garbage state.'''
    return State.GARGABE, None


class State(Enum):
    '''Track state of stream of characters.'''
    NORMAL = 0
    GARGABE = 1
    IGNORE = 2
    IGNORE_IN_GARBAGE = 3

    def process(self, ch):
        '''Process a character.'''
        if self == State.NORMAL:
            return process_normal(ch)
        if self == State.GARGABE:
            return process_garbage(ch)
        if self == State.IGNORE:
            return process_ignore(ch)
        if self == State.IGNORE_IN_GARBAGE:
            return process_ignore_in_garbage(ch)
