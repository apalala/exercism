

_VERSES = [
    'No more bottles of beer on the wall, no more bottles of beer.\n'
    'Go to the store and buy some more, 99 bottles of beer on the wall.\n',
    '1 bottle of beer on the wall, 1 bottle of beer.\n'
    'Take it down and pass it around, no more bottles of beer on the wall.\n',
    '2 bottles of beer on the wall, 2 bottles of beer.\n'
    'Take one down and pass it around, 1 bottle of beer on the wall.\n',
]


_STANDARD_VERSE = (
    '{} bottles of beer on the wall, {} bottles of beer.\n'
    'Take one down and pass it around, '
    '{} bottles of beer on the wall.\n'
)


def verse(n):
    if n < len(_VERSES):
        return _VERSES[n]
    else:
        return _STANDARD_VERSE.format(n, n, n-1)


def song(top=99, bottom=0):
    return ''.join(
        verse(n) + '\n'
        for n in range(top, bottom - 1, -1)
    )

