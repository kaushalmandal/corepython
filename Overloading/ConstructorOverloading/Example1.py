class Test:
    def __init__(self):
        print('No-arg constructor')
    def __init__(self,a):
        print('one-arg constructor')
    def __init__(self,a,b):
        print('two-arg constructor')
# t=Test()
# t=Test(10)
t=Test(10,20)