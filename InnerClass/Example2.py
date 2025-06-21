class Person:
    def __init__(self,name):
        self.name=name
        self.db=self.DOB(10,9,88)

    def display(self):
        print('Name is :',self.name)

    class DOB:
        def __init__(self,dd,mm,yy):
            self.dd=dd
            self.mm=mm
            self.yy=yy

        def dateOfBirth(self):
            print('Date is :',self.dd)
            print('Month is :',self.mm)
            print('Year is :',self.yy)

p=Person('kaushal')
p.display()
x=p.db
x.dateOfBirth()

