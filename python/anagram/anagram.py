

def _is_anagram(word, candidate):
    word, candidate = word.lower(), candidate.lower()

    if word == candidate:
        return False

    return list(sorted(word)) == list(sorted(candidate))


def detect_anagrams(word, candidates):
    return [c for c in candidates if _is_anagram(word, c)]
