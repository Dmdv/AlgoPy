import csv
import os
import sys

numberOfDigits = 2

# From: http://stackoverflow.com/a/3682332
def int_wrapper(reader):
    for v in reader:
        yield map(int, v)

# From : http://stackoverflow.com/a/6285203
class unique_element:
    def __init__(self, value, occurrences):
        self.value = value
        self.occurrences = occurrences
def perm_unique(elements):
    eset = set(elements)
    listunique = [unique_element(i, elements.count(i)) for i in eset]
    u = len(elements)
    return perm_unique_helper(listunique, [0] * u, u-1)

def perm_unique_helper(listunique, result_list, d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d] = i.value
                i.occurrences -= 1
                for g in  perm_unique_helper(listunique, result_list, d-1):
                    yield g
                i.occurrences += 1

def main():
    if os.path.isfile("partitions.csv"):
        Ofile = open('partitions.csv', 'r')
        Reader = csv.reader(Ofile, delimiter=',', quotechar='"')
        Reader = int_wrapper(Reader)

        if os.path.isfile("%s.csv" % numberOfDigits):
            formatted = "%s.csv already exists. Do you wish to overwrite? (y/n) : "
            if input(formatted % numberOfDigits).lower() == "y":
                f = csv.writer(
                    open("%s.csv" % numberOfDigits, 'wb'),
                    delimiter=',',
                    quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
            else:
                sys.exit(0)
        else:
            f = csv.writer(
                open("%s.csv" % numberOfDigits, 'wb'),
                delimiter=',',
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL)

        for row in Reader:
            if len(row) == numberOfDigits:
                print("Match")
                for iteration in perm_unique(row):
                    print(list(iteration))
                    f.writerow(list(iteration))
            else:
                print("No Match")
    else:
        print("partitions.csv not found.")

if __name__ == '__main__':
    main()
    