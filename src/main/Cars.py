

class Cars:

    def __init__(self):
        self.cars = []
        self.total_price = 0

    def get_cars(self) -> list:
        return self.cars

    def get_price(self) -> float:
        return self.total_price

    def add_car(self, car) -> None:
        self.cars.append(car)
        self.total_price += car.get_price()

    def add_cars(self, cars):
        for car in cars:
            self.cars.append(car)
            self.total_price += car.get_price()
        #return self

    def remove_car(self, car) -> None:
        cars_aux = []
        for car in self.cars:
            if car.get_id() == car.get_id():
                self.total_price -= car.get_price()
            else:
                cars_aux.append(car)
        self.cars = cars_aux