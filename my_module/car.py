from my_module.engine import Engine


class Car:
    def __init__(self):
        self.mileage = 0
        self.engine = Engine()

    def start(self):
        self.engine.start_engine()

    def move(self, distance):
        if self.engine.is_enabled():
            print(f"the car is moving ${distance} meters")
            self.mileage += distance
            return True
        else:
            return False
