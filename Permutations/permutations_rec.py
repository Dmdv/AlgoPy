""" Unordered """


def perm_unordered(param):

    if isinstance(input, int):
        seq = list(range(param))
    else:
        seq = param

    n = len(seq)

    def sub(i):
        if i == n - 1:
            yield tuple(seq)
        else:
            for k in range(i, n):
                seq[i], seq[k] = seq[k], seq[i]
                yield from sub(i + 1)
                seq[i], seq[k] = seq[k], seq[i]

    yield from sub(0)


""" Lexicographic order """


def perm(param):

    if isinstance(param, int):
        seq = list(range(param))
    else:
        seq = param

    n = len(seq)

    def sub(i):
        if i == n - 1:
            yield tuple(seq)
        else:
            for k in range(i, n):
                seq[i], seq[k] = seq[k], seq[i]
                yield from sub(i + 1)
            x = seq[i]
            for k in range(i + 1, n):
                seq[k - 1] = seq[k]
            seq[n - 1] = x

    yield from sub(0)
