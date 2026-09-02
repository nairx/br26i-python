import sys 
mylist = ["John","Amy","Mike","Brian","Chastity"]
myiterator = iter(mylist)
print(sys.getsizeof(mylist), " bytes")
print(sys.getsizeof(myiterator), " bytes")

print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
