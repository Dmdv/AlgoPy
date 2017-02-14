"""Starts Ascending Compositions
   http://jeromekelleher.net/generating-integer-partitions.html
"""

# import csv
# import os
# import sys

def rule_asc(n):
    """
    Although this algorithm is very simple, it is also very efficient.
    It is Constant Amortised Time, which means that the average computation
    per partition that is output is constant.
    """
    a = [0 for i in range(n + 1)]
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        yield a[:k + 1]

def accel_asc(n):
    """
    Ascending Compositions
    Most efficient algo
    """
    arr = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = arr[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            arr[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            arr[k] = x
            arr[l] = y
            yield arr[:k + 2]
            x += 1
            y -= 1
        arr[k] = x + y
        y = x + y - 1
        yield arr[:k + 1]

# def main():
#     f = csv.writer(open("partitions.csv", 'wb'),
#           delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     generatedPartitions = partitions(100)
#     for i in generatedPartitions:
#         print (i)
#         f.writerow(i)

def main():
    """Starts Ascending Compositions
    http://jeromekelleher.net/generating-integer-partitions.html"""
    for row in accel_asc(10):
        print(row)

if __name__ == '__main__':
    main()
