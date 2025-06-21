class Outer:
    def __init__(self):
        print('outer class object creation')
    class Inner:
        def __init__(self):
            print('Inner class object creation')
        def m1(self):
            print('Inner class Instance method')
o=Outer()
i=o.Inner()
i.m1()