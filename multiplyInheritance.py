class Employee:
    def salary(self):
        return 15000

class Parent:

    def children(self):
        return ['Vasya', 'Katya']

class Man(Employee, Parent):

    def eat(self):
        pass

dan = Man()

# print(dan.children())
# print(dan.salary())

