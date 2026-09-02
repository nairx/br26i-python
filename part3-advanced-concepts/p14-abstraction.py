#abstraction
from abc import ABC,abstractmethod
class User(ABC):
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(self.name)
    @abstractmethod
    def Salary(self):
        pass

class Staff(User):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary=salary
    def Salary(self):
        print(self.salary)
    @abstractmethod
    def incentive():
        pass

class Vendor(User):
    def __init__(self,id,name,wage):
        super().__init__(id,name)
        self.wage = wage
    def Salary(self):
        print(self.wage)
    

class Agent(Staff):
    def __init__(self,id,name,salary,commission):
            super().__init__(id,name,salary)
            self.commission=commission
    def incentive(self):
            print(self.commission)


# s = Staff(1001,"Mike",5000)
# s.display()
# s.Salary()

# v=Vendor(1002,"Max",1000)
# v.display()
# v.Salary()

a=Agent(1003,"Ryan",1000,100)
a.incentive()
