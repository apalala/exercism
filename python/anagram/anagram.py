

def _is_anagram(word, candidate):
    word, candidate = word.lower(), candidate.lower()

    return (
        word != candidate and
        sorted(word) == sorted(candidate)
    )


def detect_anagrams(word, candidates):
    return [c for c in candidates if _is_anagram(word, c)]
