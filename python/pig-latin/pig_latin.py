


def translate(phrase):
    return ' '.join(_translate_word(word) for word in phrase.split())


def _translate_word(word):
    word = word.lower()
    first = word[0]
    if first in ('x', 'y') and not _is_vowel(word[1:2]):
        pass
    elif not _is_vowel(first):
        i = 1
        while not _is_vowel(word[i]):
            i += 1
        if word[i - 1] == 'q' and word[i] == 'u':
            i += 1
        word = word[i:] + word[:i]
    return word + 'ay'


def _is_vowel(c):
    return c in set('aeiou')

