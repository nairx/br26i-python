# test=["Sem1","Sem2","Sem3"]
# result = [True,False,True]
# print(all(result))
# print(any(result))

#######################

# def f(x):
#     return x*2

# sqr = map(f,[2,3,4,5])

# print(list(sqr))


# def f(x):
#     return x%2==0

# filteredResult = filter(f,[2,3,4,5])

# print(list(filteredResult))


# from functools import reduce
# def f(x,y):
#     return x+y
# total = reduce(f,[2,3,4,5])
# print(total)


# names = ["Alice","John","Amy"]
# scores = [45,67,54]

# for name,score in zip(names,scores):
#     print(name,score)


names = ["Alice","John","Amy"]
for index,name in enumerate(names,start=1):
    print(index,name)
