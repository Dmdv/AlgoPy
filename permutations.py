"""
https://en.wikipedia.org/wiki/Permutation#Algorithms_to_generate_permutations
"""


def perm_unordered(param):
    """
    From Rosetta code
    Unordered implementation
    """
    """ Unordered
    i.e 1,2,3
    i = 2
    swap (2,0)
    swap (2,1)
    swap (2,2) - omitted
    i = 1
    swap (1, 0)
    swap (1, 1) - omitted
    swap (1, 2)
    i = 0
    swap (0, 0) - omitted
    swap (0, 1)
    swap (0, 2)
    """

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
                # print("swap0 {0}-{1}".format(i, k))
                yield from sub(i + 1)
                seq[i], seq[k] = seq[k], seq[i]
                # print("swap1 {0}-{1}".format(i, k))

    yield from sub(0)


def perm(param):
    """
    From Rosetta code
    Lexicographic order
    """

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


def permutation0(xs):
    """
    Straightforward implementation
    :param xs:
    :return:
    """
    if len(xs) == 1:
        return [xs]
    ret = []
    for x in xs:
        for y in permutation0(filter(lambda a: a != x, xs)):
            ret.append([x] + y)
    return ret


def permutation1(xs):
    """
    Straightforward implementation
    :param xs:
    :return:
    """
    if len(xs) == 1:
        return [xs]
    else:
        return [([x] + y) for x in xs for y in permutation1(filter(lambda a: a != x, xs))]


def heap(elements, n):
    """
    Recursive heap permutation implementation

    Heap's algorithm: https://en.wikipedia.org/wiki/Heap%27s_algorithm
    https://stackoverflow.com/questions/29042819/heaps-algorithm-permutation-generator
    :param n: length of an array
    :param elements: array
    :return: set
    """

    if n == 1:
        yield elements
    else:
        for i in range(n):

            for hp in heap(elements, n - 1):
                yield hp

            j = 0 if (n % 2) == 1 else i

            swap(elements, j, n - 1)

        heap(elements, n - 1)


def swap(elements, i, j):
    elements[i], elements[j] = elements[j], elements[i]


def generate_permutations(elements, n):
    """
    Recursive heap permutation implementation
    Compare to heap, just another implementation of Heap's algorithm
    :param elements:
    :param n:
    """

    if n == 0:
        yield elements

    else:
        for i in range(n - 1):

            # Generate permutations with the last element fixed.
            yield from generate_permutations(elements, n - 1)

            j = 0 if (i % 2) == 1 else i

            # Swap the last element.
            swap(elements, j, n - 1)

        # Generate the last permutations after the final swap.
        yield from generate_permutations(elements, n - 1)


def permutations(elements):
    yield from generate_permutations(elements, len(elements))


def generate_permutations_non_recursive(elements, n):
    """
    Non recursive implementation of Heap's algorithm
    http://www.bernardosulzbach.com/heaps-algorithm/
    :param elements:
    :param n:
    """
    # As by Robert Sedgewick in Permutation Generation Methods
    c = [0] * n
    yield elements
    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                swap(elements, 0, i)
            else:
                swap(elements, c[i], i)
            yield elements
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

