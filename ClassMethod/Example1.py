class Animals:
    legs=4
    @classmethod
    def walk(cls):
        print('Animal walks by',Animals.legs)
Animals.walk()
