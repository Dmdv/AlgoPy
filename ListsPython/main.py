def remove_sublist(sublist, mainlist):
    cursor = 0

    for b in mainlist:

        if cursor == len(sublist):
            cursor = 0
        if b == sublist[cursor]:
            cursor += 1
        else:
            cursor = 0
            yield b

    for i in range(0, cursor):
        yield sublist[i]


def filter_odd_sets(iterable):
    odd = []
    for b in iterable:
        if b % 2 == 0:
            odd.append(b)
        elif odd:
            yield odd
            odd = []

    if odd:
        yield odd


def distinct(iterable):
    # or just set(iterable)
    d = dict([i, i] for i in iterable)
    return d.keys()


# from itertools import izip
# i = iter(a)
# b = dict(izip(i, i))
# b = dict(zip(a[::2], a[1::2]))


def duplicates(iterable):

    dist = distinct(iterable)

    if len(iterable) == len(dist):
        return

    for d in dist:
        if iterable.count(d) > 1:
            yield d


if __name__ == '__main__':

    for x in remove_sublist([1, 1, 1], [1, 1, 1, 1, 1]):
        print (x)

    for x in filter_odd_sets([1, 2, 4, 3, 4, 2, 6, 3, 8, 6, 4]):
        print(x)

    print(distinct([1, 1, 2, 2, 3, 3, 3, 4]))

    print([x for x in duplicates([1, 2, 4])])

    print([ x for x in duplicates([1, 1, 2, 2, 3, 3, 3, 4])])
