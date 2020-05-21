from . import Hotel
from . import Flight
from . import Car


class Destiny:
    def __init__(self, flight, n_passengers, n_days=0, hotel=None, cars=[]):
        self.flight = flight                #  n_days ho indicarà l'hotel? o o afegim al vol?
        self.name = flight.get_destiny()
        self.n_passengers = n_passengers
        self.n_days = n_days
        self.hotel = hotel
        self.cars = cars

    def get_name(self):
        return self.name

    def set_hotel(self, hotel):
        self.hotel = hotel

    def add_car(self, car):
        self.cars.append(car)

    def get_price(self):
        price_cars = 0
        for car in self.cars:
            price_cars += car.get_price()

        price_hotel = 0
        if self.hotel is not None:
            price_hotel = self.hotel.get_price()

        return price_cars + price_hotel + self.flight.get_price()

    def get_flight(self):
        return self.flight

    def get_cars(self):
        return self.cars

    def get_hotel(self):
        return self.hotel

    def remove_hotel(self):
        self.hotel = None

    def remove_car(self, code):
        cars_aux = []
        for car in self.cars:
            if car.get_code() != code:
                cars_aux.append(car)
        self.cars = cars_aux
