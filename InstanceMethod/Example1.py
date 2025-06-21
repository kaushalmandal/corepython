class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print('Name is :',self.name)
        print('Marks are :',self.marks)

    def grade(self):
        if self.marks>=60:
            print('First grade')
        elif self.marks>=50:
            print('second grade')
        elif self.marks>=33:
            print('Third grade')
        else:
            print('FAIL better luck next time')

n=int(input('Enter number of students'))
for i in range(n):
    name=input('Enter name of students')
    marks=int(input('Enter students marks'))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()