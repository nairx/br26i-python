# numbers = [5,3,2]
# print(sum(numbers))

# def sayHello():
#     print("Hello World")

# sayHello()


# def add(a,b):
#     return a+b

# result = add(4,5)  #Positional Argument
# print(result)



# def add(a,b):
#     return a+b

# result = add(b=4,a=5)  #Keyword Argument
# print(result)


# def add(a=0,b=0):  #default argument
#     return a+b

# result = add(b=4)  
# print(result)



# def add(*args): 
#     print(args)
# add(4,5)


# def add(**kwargs): 
#     print(kwargs)
# add(a=4,b=5,c=7)


# def add(*args,**kwargs): 
#     print(sum(args)+sum(kwargs.values()))
# add(4,5,6,d=9,e=7)


def f1(*args,**kwargs): 
    print(args)
    print(kwargs)
f1("Hello","World",c="Hi",d="Namaste")