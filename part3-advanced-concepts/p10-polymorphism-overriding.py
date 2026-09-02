#Method Overriding
class Example:
    def greet(self,name,age):
        print("This is greet method from Example")
        return f"Hello {name},{age}"

class Child(Example):
    def greet1(self,name,age):
        print("This is greet method from Child")
        return f"Hello {name},{age}"

# example = Example()
# print(example.greet("John",21))

child = Child()
print(child.greet("Amy",23))