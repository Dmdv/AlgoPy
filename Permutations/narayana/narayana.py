# narayana.py
"""Поиск очередной перестановки"""


def next_permutation(sequence, compare):
    count = len(sequence)
    i = count

    # Этап № 1
    while True:
        if i < 2:
            return False  # Перебор закончен
        i -= 1;
        if compare(sequence[i - 1], sequence[i]):
            break

    # Этап № 2
    j = count
    while j > i and not compare(sequence[i - 1], sequence[j - 1]):
        j -= 1
    sequence[i - 1], sequence[j - 1] = sequence[j - 1], sequence[i - 1]
    
    # Этап № 3
    j = count
    while i < j - 1:
        j -= 1
        sequence[i], sequence[j] = sequence[j], sequence[i]
        i += 1
    return True
