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
    elif _has_sublist(alist, blist):
        return SUBLIST
    elif _has_sublist(blist, alist):
        return SUPERLIST
    else:
        return UNEQUAL


def _has_sublist(sub, alist):
    for i in range(1 + len(alist) - len(sub)):
        for j, s in enumerate(sub):
            if s != alist[i + j]:
                break
        else:
            return True
