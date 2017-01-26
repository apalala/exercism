

def abbreviate(phrase):
    return ''.join(w[0].upper() for w in _words(phrase))


def _words(phrase):
    words = []
    i = 0
    while i < len(phrase):
        if not phrase[i].isalpha():
            i += 1
        else:
            j = i
            while j < len(phrase) and phrase[j].isupper():
                j += 1
            while j < len(phrase) and phrase[j].islower():
                j += 1
            words.append(phrase[i:j])
            i = j

    return words
