from . import Hotel
from . import Flight
from . import Car
from src.main.Destiny import *
from src.main.Hotels import *
from src.main.Flights import *
from src.main.Cars import *
from . import Skyscanner
from . import Booking
from . import Rentalcars
from . import Bank


class Journey:
    def __init__(self, n_passengers, origin, flights, user, payment_data, tryings=3):
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
        self.return_flight = flights[-1]

        for f in flights[:-1]:
            self.destinies.append(Destiny(f.get_destiny(),n_passengers))



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
        flights = Flights()
        for destiny in self.destinies:
            flights.add_flight(destiny.get_flight())
        flights.add_flight(self.return_flight)
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
        cars = Cars()
        for destiny in self.destinies:
            if destiny.get_cars() is not []:
                cars.add_car(destiny.get_cars())
        return cars

    def add_car(self, destiny, car):
        for i, d in enumerate(self.destinies):
            if d.get_name() == destiny:
                self.destinies[i].add_car(car)

    def remove_car(self, destiny, code):
        for i, d in enumerate(self.destinies):
            if d.get_name() == destiny:
                self.destinies[i].remove_car(code)

    # def confirm_reserve_cars(self):
    #     tryings = self.tryings
    #     while tryings > 0:
    #         tryings -= 1
    #         if self.rentalcars.confirm_reserve(self.user, self.get_cars()) is True:
    #             return True
    #     return False

    def confirm_reserve_cars(self):
        self.tryings -= 1
        if self.rentalcars.confirm_reserve(self.user, self.get_cars) is True:
            return True
        else:
            return self.retry_reserve_cars()

    def retry_reserve_cars(self):
        while self.tryings > 1:
            self.tryings -= 1
            if self.rentalcars.confirm_reserve(self.user, self.get_cars) is True:
                return True
        return self.rentalcars.confirm_reserve(self.user, self.get_cars)  # superat maxim intents

    def get_hotels(self) -> Hotels:
        hotels = Hotels()
        for destiny in self.destinies:
            if destiny.get_hotel() is not None:
                hotels.add_hotel(destiny.get_hotel())
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
        self.tryings -= 1
        if self.booking.confirm_reserve(self.user, self.get_hotels) is True:
            return True
        else:
            return self.retry_reserve_hotels()

    def retry_reserve_hotels(self):
        while self.tryings > 1:
            self.tryings -= 1
            if self.booking.confirm_reserve(self.user, self.get_hotels) is True:
                return True
        return self.booking.confirm_reserve(self.user, self.get_hotels)  # superat maxim intents

    def set_payment_import(self):
        self.payment_data.set_reserve_amount(self.get_total_price())

    def do_payment(self):
        self.payment_data.calculate_reserve_amount(self.get_flights, self.get_hotels, self.get_cars)
        self.tryings -= 1
        bank_response = self.bank.do_payment(self.user, self.payment_data)
        if bank_response is True:
            return bank_response  # ho he hagut de posar així pel testMockV2 paymentMethod que cal que retorni method_payment
        else:
            return self.retry_payment()

    def retry_payment(self):
        while self.tryings > 1:
            self.tryings -= 1
            if self.bank.do_payment(self.user, self.payment_data) is True:
                return self.bank.do_payment(self.user, self.payment_data)
        return self.bank.do_payment(self.user, self.payment_data)  # superat maxim intents

    def get_payment_type(self):
        return self.payment_data.get_payment_type()