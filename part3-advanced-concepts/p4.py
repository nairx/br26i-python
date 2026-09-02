def f1(f):
    def wrapper():
        print("Function begins")
        f()
        print("Function ends")
    return wrapper

@f1
def f2():
    print("I am f2")

@f1
def f3():
    print("I am f3")

f2()
f3()