from my_module.engine import Engine


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine = Engine()
        self.distance = 0

    def move_distance(self, distance):
        if self.is_engine_working():
            print(f"the car is moving ${distance} meters")
            self.distance += distance
        return self.distance

    def is_engine_working(self):
        return self.engine.start_engine()
