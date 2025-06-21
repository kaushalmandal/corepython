class Test:
    def __init__(self,a):
        self.a=a
    def __add__(self, other):
        return self.a+other.a

t1=Test(10)
t2=Test(20)
print(t1+t2)

t3=Test('kaushal')
t4=Test('Mandal')
print(t3+t4)