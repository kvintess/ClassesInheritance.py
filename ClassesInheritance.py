class Pet:
    leggs = 4
    has_tail = True

    def __init__(self,name):
        self.name = name

    def inspect(self):
        print(self.__class__.__name__)
        print('всего ног', self.leggs)
        print('хвост присутствует', ' да ' if self.has_tail else ' нет')
        print(self.__dict__)

class Cat(Pet):
    '''кошка это дом животное'''

    def sound(self):
        print('мяу')

class Bobtail(Cat):
    has_tail = False

class Dog(Pet):
    def sound(self):
        print('гав')

my_pet = Bobtail('kiss')
my_pet.inspect()

