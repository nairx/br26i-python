#normal function
# def numbers():
#     return [1,2,3]

# x=numbers()
# print(x)


#generator
# def numbers():
#     yield 1
#     yield 2
#     yield 3

# x=numbers()
# print(x)

# for n in numbers():
#     print(n)


#generator
# def numbers():
#     for i in range(10):
#         yield i

# x=numbers()
# print(x)

# for n in numbers():
#     print(n)



import sys 

#regular 
def numbers():
    return [i for i in range(10000000)]

#generator 
def numbers_gen():
    for i in range(10000000):
         yield i

mylist = numbers()
mygen = numbers_gen()

print(sys.getsizeof(mylist), " bytes")
print(sys.getsizeof(mygen), " bytes")

