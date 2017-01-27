

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


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
    return not sub or any(
        sub[0] == alist[i] and
        sub == alist[i:i + len(sub)]
        for i in range(1 + len(alist) - len(sub))
    )
