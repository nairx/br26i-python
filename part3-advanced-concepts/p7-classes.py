# class Employee:
#     def sayHello(self):
#         print("Hello")
# e = Employee()
# e.sayHello()

#Constructor with parameter
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def displayInfo(self):
#         print("Displaying Information of Person")
#         print(self.name,self.age)

# p = Person("John",21)
# p.displayInfo()


#Constructor with default value
class Person:
    def __init__(self,name,age=23):
        self.name = name
        self.age = age
    def displayInfo(self):
        print("Displaying Information of Person")
        print(self.name,self.age)

p1= Person("John",21)
p2 = Person("Amy")
p1.displayInfo()
p2.displayInfo()