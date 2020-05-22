
""" Class encapsulating a list of cars"""
class Cars:
    def __init__(self):
        self.cars = []

    """ Add the given cars to the cars atribute"""
    def add_cars(self, cars):
        for i in range(cars.get_len()):
            self.cars.append(cars.get_car(i))

    """ Add the given car to the cars atribute"""
    def add_car(self, car):
        self.cars.append(car)

    """ Get the car on the i index of the cars atribute"""
    def get_car(self, i):
        return self.cars[i]

    """ Get the price of the car on the i index (price per day * n_days)"""
    def get_price(self, i):
        return self.cars[i].get_price()

    """ Get the code of the car on the i index"""
    def get_code(self, i):
        return self.cars[i].get_code()

    """ Get the number of cars"""
    def get_len(self):
        return len(self.cars)
