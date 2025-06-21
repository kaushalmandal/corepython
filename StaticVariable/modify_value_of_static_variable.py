class Test:
    a=777
    def __init__(self):
        Test.a=888
    @classmethod
    def m1(cls):
        cls.a=999

    def m2(self):
        Test.a=666

    @staticmethod
    def m3():
        Test.a=555
print(Test.a)
t=Test()
print(t.a)
t.m1()
print(t.a)
t.m2()
print(t.a)
t.m3()
print(t.a)