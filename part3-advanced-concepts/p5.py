#Decorators
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)  # result = calculate()
        end = time.time()
        print(f"Took {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def calculate():
    total=0
    for i in range(1_000_000):
        total += i
    return total

result1 = calculate()
print(result1)

@timer
def add(a,b):
    return a+b

result2 = add(3,5)
print(result2)


@timer
def greet():
    print("Hello")

greet()
