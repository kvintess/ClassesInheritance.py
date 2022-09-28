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

    def truck_ready(self):
        pass

    def act(self):
        pass

class Vehicle:
    fuel_rate = 0

    def __init__(self, model):
        pass

    def __str__(self):
        pass

    def ride(self):
        pass

    def go_to(self, road):
        pass

    def act(self):
        pass
