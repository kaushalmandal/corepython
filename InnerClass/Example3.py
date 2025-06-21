class Person:
    def __init__(self):
        self.name='kaushal'
        self.head=self.Head()
        self.brain=self.Brain()

    def display(self):
        print('Hello',self.name)

    class Head:
        def talk(self):
            print('Talking')
    class Brain:
        def think(self):
            print('Thinking')

p=Person()
p.display()
p.head.talk()
p.brain.think()