class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks 
    def __str__(self):
        return f"{self.name}-{self.marks}"

s = Student("John",90)
print(s)

