class Test:
    def __init__(self):
        self.a=10

    def m1(self):
        self.b=20
t=Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
t.c=30
print(t.__dict__)