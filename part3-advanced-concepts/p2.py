import sys

mylist = [i for i in range(1000)]
myiterator = iter([i for i in range(1000)])
print(sys.getsizeof(mylist), " bytes")
print(sys.getsizeof(myiterator), " bytes")