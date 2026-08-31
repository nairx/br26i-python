
# square = lambda x:x*x
# print(square(5))

# add = lambda a,b:a+b
# print(add(4,5))

# maxval = lambda a,b:a if a>b else b
# print(maxval(4,5))

# num = [1,2,3]
# result = lambda x:(i for i in x if i>1)
# print(list(result(num)))

# squares = list(map(lambda n:n*n,[1,2,3,4,5]))
# print(squares)

# even_numbers = list(filter(lambda n:n%2==0,[1,2,3,4,5]))
# print(even_numbers)


from functools import reduce
total = reduce(lambda n,m:n+m,[1,2,3,4,5])
print(total)