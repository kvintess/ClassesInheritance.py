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

class WarRobot(Robot):

    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self):
        super().operate()
        print('робот охраняет объект')

my_rob = WarRobot(model='r2d2',gun='pist')
my_rob.operate()
# class CleaningRobot(Robot):
#
#     def operate(self):
#         print('робот пылесосит')
#
