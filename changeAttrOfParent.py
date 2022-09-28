# #переопределяем свойства и методы родителя
# class Cat:
#     has_tail = True
#     woolliness = 20
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Имя {} хвост {} пушистость {}'.format(self.name, self.has_tail,
#                                                       self.woolliness)
#
# class Bobcat(Cat):
#
#     has_tail = False
#
# class Sphinx(Cat):
#
#     woolliness = 1
#
# sonya = Bobcat('sonya')
# loqy = Sphinx('loqy')
#
# print(sonya)
# print(loqy)

class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} модель {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('робот ездит по кругу')

class CanFly:
    def __init__(self):
        self.altitude = 0 # метров
        self.velocity = 0 #км/ч

class Drone(Robot, CanFly):

    def __init__(self, model):
        super(Drone, self).__init__(model=model)
        CanFly.__init__(self)
    def __str__(self):
        return '{} модель {}'.format(self.__class__.__name__, self.model) +'' \
        'высота{} скорость {}'.format(self.altitude, self.velocity)
    def operate(self):
        print('ведет разведку с воздуха')

my_rob = Drone(model='r2d2')
my_rob.operate()
print(my_rob)