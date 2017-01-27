

VALUE_CLASSES = {
    1: ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'),
    2: ('D', 'G'),
    3: ('B', 'C', 'M', 'P'),
    4: ('F', 'H', 'V', 'W', 'Y'),
    5: ('K',),
    8: ('J', 'X'),
    10: ('Q', 'Z'),
}

LETTER_VALUE = {
    letter: value
    for value, letters in VALUE_CLASSES.items()
    for letter in letters
}


def score(word):
    if not word.isalpha():
        return 0
    return sum(LETTER_VALUE[letter] for letter in word.upper())