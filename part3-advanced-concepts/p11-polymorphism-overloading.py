#Method overloading
class Example:
    def greet(self,name,age=0):
        if age==0:
            print(f"{name}")
        else:
            print(f"{name},{age}")
    
example = Example()
example.greet("John",21)
example.greet("John")