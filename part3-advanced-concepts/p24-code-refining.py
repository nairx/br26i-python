# n=10
# x=0
# for i in range(1,n+1):
#     x=x+i
# print(x)

# n=10
# total = sum(range(1,n+1))
# print(total)

######################

# name = "John"
# print("Hello ",name)
# name = "Amy"
# print("Hello ",name)
# name = "Mike"
# print("Hello ",name)

# def greet(name):
#     print("Hello ",name)

# greet("Amy")
# greet("John")
# greet("Mike")

########################
numbers = [1,2,3,4,5,6]
result=[]
for n in numbers:
    if n%2==0:
        result.append(n*n)
print(result)

numbers = [1,2,3,4,5,6]
result = [n*n for n in numbers if n%2==0]
print(result)
