#!python3

'''Day 4, part 1.'''

import data_4


def sort_word(word):
    '''Sort letters in word.

    >>> sort_word('a')
    'a'

    >>> sort_word('abc')
    'abc'

    >>> sort_word('bca')
    'abc'

    '''
    letters = list(word)
    letters.sort()
    return ''.join(letters)


def is_valid_phrase(phrase):
    '''Check if pass phrase is valid.

    >>> is_valid_phrase('a')
    True

    >> is_valid_phrase('ab ba')
    False
    '''
    words = [sort_word(word.strip()) for word in phrase.split()]
    word_count = len(words)
    return len(set(words)) == word_count


def main():
    phrases = data_4.phrases
    valid_count = sum(1 if is_valid_phrase(ph) else 0 for ph in phrases)
    print(valid_count)


if __name__ == '__main__':
    main()


    # sort_word('bca')
