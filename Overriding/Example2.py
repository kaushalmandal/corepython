class P:
    def property(self):
        print('Land+gold+cash')
    def marry(self):
        print('appalamma')
class C(P):
    def marry(self):
        super().marry()
        print('katrina kaif')

c=C()
c.property()
c.marry()