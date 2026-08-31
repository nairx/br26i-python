# x=10
# def f1():
#     x=20
#     print(x)
# f1()
# print(x)


x=10
def f1():
    global x
    x=20
    print(x)
f1()
print(x)