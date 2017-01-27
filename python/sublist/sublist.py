from enum import IntEnum
from itertools import islice


class SubListType(IntEnum):
    SUBLIST = 1
    SUPERLIST = 2
    EQUAL = 3
    UNEQUAL = 4


SUBLIST = SubListType.SUBLIST
SUPERLIST = SubListType.SUPERLIST
EQUAL = SubListType.EQUAL
UNEQUAL = SubListType.UNEQUAL


def check_lists(alist, blist):
    if alist == blist:
        return EQUAL
    elif not alist:
        return SUBLIST
    elif not blist:
        return SUPERLIST
    elif len(alist) < len(blist) and _has_sublist(alist, blist):
        return SUBLIST
    elif len(alist) > len(blist) and _has_sublist(blist, alist):
        return SUPERLIST
    else:
        return UNEQUAL


def _has_sublist(sub, alist):
    return any(
        sub[0] == alist[i] and
        all(s == a for a, s in zip(sub, islice(alist, i, i + len(sub))))
        for i in range(1 + len(alist) - len(sub))
    )
