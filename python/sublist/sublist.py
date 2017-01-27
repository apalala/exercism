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
    elif _has_sublist(blist, alist):
        return SUBLIST
    elif _has_sublist(alist, blist):
        return SUPERLIST
    else:
        return UNEQUAL


def _has_sublist(alist, sub):
    # See:
    #   http://stackoverflow.com/a/12576755/545637
    if not sub:
        return True
    elif len(sub) > len(alist):
        return False
    else:
        for i in range(1 + len(alist) - len(sub)):
            if sub[0] != alist[i]:
                continue
            if sub == alist[i:i + len(sub)]:
                return True
        return False
