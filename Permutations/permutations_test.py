from Permutations.permutations import *


def test():
    for subset in generate_permutations_non_recursive([1, 2, 3], 3):
        print(subset)


test()
