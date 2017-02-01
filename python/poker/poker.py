from enum import IntEnum
from collections import Counter

RANKS = '0123456789TJQKA'
VALUE = {rank: i for i, rank in enumerate(RANKS)}


class Hand(IntEnum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULLHOUSE = 6
    POKER = 7
    STRAIGHT_FLUSH = 8
    FIVE_OF_A_KIND = 9


def poker(hands):
    values = [_hand_value(hand) for hand in hands]
    best = max(values)

    return [
        hand for hand, value in zip(hands, values)
        if value == best
    ]


def _hand_value(hand):
    ranks, suits = list(zip(*hand))

    values = sorted([VALUE[r] for r in ranks], reverse=True)
    counts = sorted([(n, value) for value, n in Counter(values).items()], reverse=True)
    repeats = [n for n, _ in counts]

    flush = len(set(suits)) == 1
    straight = len(counts) == 5 and (
        values[0] - values[-1] == 4 or
        values[1] - values[-1] == 3 and values[0] == len(VALUE)
    )

    if repeats == [5]:
        return (Hand.FIVE_OF_A_KIND, values)
    elif straight and flush:
        return (Hand.STRAIGHT_FLUSH, values)
    elif repeats == [4, 1]:
        return (Hand.POKER, counts)
    elif repeats == [3, 2]:
        return (Hand.FULLHOUSE, counts)
    elif flush:
        return (Hand.FLUSH, values)
    elif straight:
        return (Hand.STRAIGHT, values)
    elif repeats == [3, 1, 1]:
        return (Hand.THREE_OF_A_KIND, counts)
    elif repeats == [2, 2, 1]:
        return (Hand.TWO_PAIR, counts)
    elif repeats == [2, 1, 1, 1]:
        return (Hand.PAIR, counts)
    elif repeats == [1] * 5:
        return (Hand.HIGH_CARD, values)
    else:
        raise ValueError('Unknown hand?', hand)
