class A:
    def __init__(self,a):
        self.a=a
    def __add__(self, other):
        return self.a+other.a
a=A(10)
a1=A(20)
print(a+a1)
b=A('kaushal')
b1=A('kumar')
print(b+b1)