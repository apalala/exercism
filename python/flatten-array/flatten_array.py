from collections.abc import Sequence


def flatten(array):
    if array is None:
        return []
    elif isinstance(array, str) or not isinstance(array, Sequence):
        return [array]
    else:
        return [e for x in array for e in flatten(x)]
