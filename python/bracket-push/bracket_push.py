

BRACKET_PAIRS = [
    ('"', '"'),
    ("'", "'"),
    ('(', ')'),
    ('[', ']'),
    ('{', '}')
]
BRACKETS = {open: close for open, close in BRACKET_PAIRS}


def check_brackets(text):
    closing_stack = []
    for c in text:
        if c in BRACKETS:
            closing_stack.append(BRACKETS[c])
        elif not closing_stack or c != closing_stack.pop():
            return False
    return not closing_stack
