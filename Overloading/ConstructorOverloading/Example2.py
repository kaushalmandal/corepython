class Test:
    def __init__(self,*a):
        print('constructor with variable number of arguments')
t=Test()
t1=Test(10)
t2=Test(10,20)
t3=Test(10,20,30)