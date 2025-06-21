class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    
    def display(self):
        print('Name is :',self.name)
        print('Rollno is :',self.rollno)
        print('Marks is :',self.marks)
s=Student('kaushal',101,99)
s.display()