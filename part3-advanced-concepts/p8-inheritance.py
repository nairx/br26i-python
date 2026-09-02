#Inheritance
class User():
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(self.name)

class Staff(User):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary=salary
    def showSalary(self):
        print(self.salary)

class Vendor(User):
    def __init__(self,id,name,wage):
        super().__init__(id,name)
        self.wage = wage
    def showWage(self):
        print(self.wage)

s = Staff(1001,"Mike",5000)
s.display()
s.showSalary()

v=Vendor(1002,"Max",1000)
v.display()
v.showWage()