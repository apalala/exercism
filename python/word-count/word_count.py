import re
from collections import Counter


def word_count(text):
    filtered_text = text.replace('_', ' ')
    words = re.split('\W+', filtered_text.lower())

    counts = Counter(words)
    if '' in counts:
        del counts['']

    return counts
