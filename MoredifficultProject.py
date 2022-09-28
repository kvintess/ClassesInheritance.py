#модель доставки грузов

class Road:

    def init(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance

class Warehouse:

    def __init__(self, name, content=0):
        pass

    def __str__(self):
        pass

    def set_road_out(self, road):
        pass

    def truck_arrived(self, truck):
        pass

    def get_next_truck(self):
        pass

    def truck_ready(self, truck):
        pass

    def act(self):
        pass

class Vehicle:
    fuel_rate = 0

    def __init__(self, model):
        pass

    def __str__(self):
        pass

    def tank_up(self):
        pass

class Truck(Vehicle):

    def __init__(self, model, body_space=1000):
        pass

    def __str__(self):
        pass

    def ride(self):
        pass

    def go_to(self, road):
        pass

    def act(self):
        pass

class AutoLoader(Vehicle):

    def __init__(self, model,bucket_capacity=100, warehouse=None, role='loader'):
        pass

    def __str__(self):
        pass

    def act(self):
        pass

    def load(self):
        pass

    def unload(self):
        pass

TOTAL_CARGO = 100000

moscow = Warehouse(name='Москва',content=TOTAL_CARGO)
piter = Warehouse(name='Питер',content=0)

moscow_piter = Road(start=moscow, end=piter, distanse=715)
piter_moscow = Road(start=piter, end=moscow, distanse=780)

moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

loader_1 = AutoLoader(model='Bobcat', bucket_capacity=1000, warehouse=moscow
                      role='loader')
loader_2 = AutoLoader(model='lonking', bucket_capacity=500, warehouse=piter
                      role='unloader')

truck_1 = Truck(model='Камаз', body_space=5000)
truck_2 = Truck(model='Газ', body_space=2000)

moscow.truck_arrived(truck_1)
moscow.truck_arrived(truck_2)

hour = 0