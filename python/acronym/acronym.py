import re


def abbreviate(phrase):
    words = re.findall('[A-Z]+[a-z]*|[a-z]+', phrase)
    return ''.join(w[0].upper() for w in words)