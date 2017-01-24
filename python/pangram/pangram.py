from string import ascii_lowercase

_LETTERS = set(ascii_lowercase)


def is_pangram(sentence):
    return  _LETTERS == set(sentence.lower()) & _LETTERS
