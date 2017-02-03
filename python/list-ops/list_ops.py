# Please, do not use the built-in python functions like map, reduce, len, etc.
# that solve the same problems and try to solve it yourself instead.


def map_clone(function, xs):
    return tuple(function(x) for x in xs)


def length(xs):
    return sum(1 for _ in xs)


def filter_clone(function, xs):
    return tuple(x for x in xs if function(x))


def reverse(xs):
    if not xs:
        return []

    result = []
    for x in xs:
        result = [x] + result
    return type(xs)(result)


def append(xs, y):
    return xs + type(xs)([y])


def foldl(function, xs, acc):
    result = acc
    for x in xs:
        result = function(result,x)
    return result


def foldr(function, xs, acc):
    result = acc
    for x in reverse(xs):
        result = function(x, result)
    return result


def flat(xs):
    if xs is None:
        return []
    elif not isinstance(xs, (list, tuple)):
        return [xs]
    else:
        return [e for x in xs for e in flat(x)]


def concat(xs, ys):
    if xs is None:
        return ys
    elif ys is None:
        return xs
    else:
        return xs + ys
