class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,eno,sal):
        super().__init__(name,age)
        self.eno=eno
        self.sal=sal

    def display(self):
        print('Employee name :',self.name)
        print('Employee age :',self.age)
        print('Employee number :',self.eno)
        print('Employee salary is :',self.sal)

e=Employee('kaushal',35,101,75000)
e.display()