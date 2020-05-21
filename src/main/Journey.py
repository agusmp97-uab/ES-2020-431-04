from . import Hotel
from . import Flight
from . import Car
from src.main.Destiny import *
from . import Skyscanner
from . import Booking
from . import Rentalcars
from . import Bank


class Journey:
    def __init__(self, user, payment_data, n_passengers, origin, return_flight, tryings=3):
        self.user = user
        self.payment_data = payment_data
        self.tryings = tryings

        self.bank = Bank.Bank()
        self.skyscanner = Skyscanner.Skyscanner()
        self.rentalcars = Rentalcars.Rentalcars()
        self.booking = Booking.Booking()

        self.n_passengers = n_passengers
        self.destinies = []
        self.origin = origin
        self.return_flight = return_flight

    def get_total_price(self) -> float:
        total_price = 0
        for destiny in self.destinies:
            total_price += destiny.get_price()
        return total_price

    def get_origin(self):
        return self.origin

    def get_destinies(self) -> list:
        destinies = []
        for destiny in self.destinies:
            destinies.append(destiny.get_name())
        return destinies

    def get_flights(self) -> list:
        flights = []
        for destiny in self.destinies:
            flights.append(destiny.get_flight())
        flights.append(self.return_flight)
        return flights

    def set_return_flight(self, return_flight):
        self.return_flight = return_flight

    def add_destiny(self, flight, n_days) -> None:
        if flight.destiny not in self.get_destinies():
            new_destiny = Destiny(flight, self.n_passengers, n_days)
            self.destinies.append(new_destiny)

    def remove_destiny(self, destiny) -> None:
        destinies_aux = []
        for d in self.destinies:
            if d.get_name() != destiny:
                destinies_aux.append(d)
        self.destinies = destinies_aux

    def confirm_reserve_flights(self):
        tryings = self.tryings
        while tryings > 1:
            tryings -= 1
            if self.skyscanner.confirm_reserve(self.user, self.get_flights()) is True:
                return True
        return False

    def get_cars(self) -> list:
        cars = []
        for destiny in self.destinies:
            cars = cars + destiny.get_cars()
        return cars

    def add_car(self, destiny, car):
        for i, d in enumerate(self.destinies):
            if d.get_name() == destiny:
                self.destinies[i].add_car(car)

    def remove_car(self, destiny, code):
        for i, d in enumerate(self.destinies):
            if d.get_name() == destiny:
                self.destinies[i].remove_car(code)

    def confirm_reserve_cars(self):
        tryings = self.tryings
        while tryings > 0:
            tryings -= 1
            if self.rentalcars.confirm_reserve(self.user, self.get_cars()) is True:
                return True
        return False

    def get_hotels(self) -> list:
        hotels = Hotels()
        for destiny in self.destinies:
            if destiny.get_hotel() is not None:
                hotels.add(destiny.get_hotel())
        return hotels

    def set_hotel(self, destiny, hotel):
        for i, d in enumerate(self.destinies):
            if d.get_name() == destiny:
                self.destinies[i].set_hotel(hotel)

    def remove_hotel(self, destiny):
        for i, d in enumerate(self.destinies):
            if d.get_name() == destiny:
                self.destinies[i].remove_hotel()

    def confirm_reserve_hotels(self):
        tryings = self.tryings
        while tryings > 0:
            tryings -= 1
            if self.skyscanner.confirm_reserve(self.user, Hotels(self.get_hotels())) is True:
                return True
        return False

    def set_payment_import(self):
        self.payment_data.set_reserve_amount(self.get_total_price())

    def do_payment(self):
        tryings = self.tryings
        while tryings > 0:
            tryings -= 1
            if self.bank.do_payment(self.user, self.payment_data) is True:
                return True
        return False

    def get_payment_type(self):
        return self.payment_data.get_payment_type()