
class Cars:
    def __init__(self):
        self.cars = []

    def add_cars(self, cars):
        for i in range(cars.get_len()):
            self.cars.append(cars.get_car(i))

    def add_car(self, car):
        self.cars.append(car)

    def get_car(self, i):
        return self.cars[i]

    def get_price(self, i):
        return self.cars[i].get_price()

    def get_code(self, i):
        return self.cars[i].get_code()

    def get_len(self):
        return len(self.cars)
