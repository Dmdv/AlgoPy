from itertools import combinations


def comb(m, lst):
    """
    Custom implementations
    """
    if m == 0:
        return [[]]
    return [[x] + suffix for i, x in enumerate(lst)
            for suffix in comb(m - 1, lst[i + 1:])]


def main():
    list(combinations(range(5), 3))
    # comb usage
    comb(3, range(5))


if __name__ == '__main__':
    main()
