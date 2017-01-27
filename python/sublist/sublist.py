import re
from enum import IntEnum


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
    elif len(alist) < len(blist) and _has_sublist(alist, blist):
        return SUBLIST
    elif len(alist) > len(blist) and _has_sublist(blist, alist):
        return SUPERLIST
    else:
        return UNEQUAL


def _has_sublist(sub, alist):
    return re.match('.*' + _tostr(sub), _tostr(alist))


def _tostr(seq):
    return '竜'.join(str(d) for d in seq)
