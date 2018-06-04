# narayana_test.py

from Permutations.narayana import narayana


def less(value_0, value_1):
    return value_0 < value_1


"""Возвращает True, если value_0 больше value_1, иначе — False"""


def greater(value_0, value_1):
    return value_0 > value_1


# Основная программа
count = int(input())

sequence = list(range(1, count + 1))  # Заполнение последовательности значениями 1, 2, 3…
print("Неубывающая последовательность и её перестановки:")

while True:
    print(sequence)
    if not narayana.next_permutation(sequence, less):  # x < y — критерий сравнения для неубывающей последовательности
        break

print("Невозрастающая последовательность и её перестановки:")
while True:
    print(sequence)
    if not narayana.next_permutation(sequence,
                                     greater):  # x > y — критерий сравнения для невозрастающей последовательности
        break
