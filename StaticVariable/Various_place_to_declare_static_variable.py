class Test:
    a=10
    def __init__(self):
        Test.b=20

    def m1(self):
        Test.c=30
    @classmethod
    def m2(cls):
        cls.d=40
        Test.d=400
    @staticmethod
    def m3():
        Test.e=500
print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)