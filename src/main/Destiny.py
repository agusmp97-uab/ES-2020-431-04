from . import Hotel
from . import Flight
from . import Car
from src.main.Cars import *

""" Class containing the information of one destiny in a journey"""
class Destiny:
    def __init__(self, flight, n_passengers, n_days):
        #outbound flight
        self.flight = flight
        self.name = flight.get_destiny() # string, can be initialized from the flight info
        self.n_passengers = n_passengers
        self.n_days = n_days
        # hotel on the destiny (not always selected)
        self.hotel = None
        #list of cars on the destiny
        self.cars = Cars()

    """ Returns the name (string) of the destiny"""
    def get_name(self):
        return self.name

    """ Add a hotel to the destiny"""
    def add_hotel(self, hotel):
        self.hotel = hotel
        self.hotel.set_n_days(self.n_days)
        self.hotel.set_n_guests(self.n_passengers)

    """ Add a car to the destiny"""
    def add_car(self, car):
        car.set_days_reserved(self.n_days)
        self.cars.add_car(car)

    """ Get the total price of the destiny (hotel + flight + cars)"""
    def get_price(self):
        price_cars = 0
        for i in range(self.cars.get_len()):
            price_cars += self.cars.get_price(i)

        price_hotel = 0
        if self.hotel is not None:
            price_hotel = self.hotel.get_price()

        return price_cars + price_hotel + self.flight.get_price()*self.n_passengers

    def get_flight(self):
        return self.flight

    def get_cars(self):
        return self.cars

    def get_n_days(self):
        return self.n_days

    def get_hotel(self):
        return self.hotel

    """ Remove the hotel on the testiny"""
    def remove_hotel(self):
        self.hotel = None

    """ Remove the car with the given code on the destiny"""
    def remove_car(self, code):
        cars_aux = Cars()
        for i in range(self.cars.get_len()):
            if self.cars.get_code(i) != code:
                cars_aux.add_car(self.cars.get_car(i))
        self.cars = cars_aux
