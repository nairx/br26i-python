class Employee:
    def __init__(self,name):
        self.__name = name
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

e = Employee("John")
print(e.getName())
e.setName("Shawn")
print(e.getName())