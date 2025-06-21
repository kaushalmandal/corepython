class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def display(self):
        print('Name is :',self.name)
        print('Rollno is :',self.rollno)
        print('Marks are :',self.marks)

s=Student('kaushal',101,90)
s.display()
s1=Student('kajal',102,98)
s1.display()
