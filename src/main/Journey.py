from . import Hotel
from . import Flight
from . import Car
from src.main.Destinies import *
from src.main.Hotels import *
from src.main.Flights import *
from src.main.Cars import *
from src.main.User import *
from src.main.PaymentData import *
from . import Skyscanner
from . import Booking
from . import Rentalcars
from . import Bank


class Journey:
    def __init__(self, n_passengers, origin, tryings=3):
        self.tryings = tryings

        self.bank = Bank.Bank()
        self.skyscanner = Skyscanner.Skyscanner()
        self.rentalcars = Rentalcars.Rentalcars()
        self.booking = Booking.Booking()

        self.n_passengers = n_passengers
        self.destinies = Destinies()
        self.origin = origin

        self.return_flight = None
        self.user = None
        self.payment_data = None

    def get_total_price(self) -> float:
        total_price = 0
        for i in range(self.destinies.get_len()):
            total_price += self.destinies.get_price(i)
        if self.return_flight is not None:
            total_price += self.return_flight.get_price() * self.n_passengers
        return total_price

    def get_origin(self):
        return self.origin

    def get_n_passengers(self):
        return self.n_passengers

    def get_n_days(self, destiny):
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) == destiny:
                return self.destinies.get_destiny(i).get_n_days()

    def get_destinies_names(self) -> list:
        destinies = []
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) != self.origin:
                destinies.append(self.destinies.get_name(i))
        return destinies

    def get_flights(self) -> Flights:
        flights = Flights.Flights()
        for i in range(self.destinies.get_len()):
            flights.add_flight(self.destinies.get_flight(i))
        if self.return_flight is not None:
            flights.add_flight(self.return_flight)
        return flights

    def add_return_flight(self, return_flight):
        self.return_flight = return_flight

    def add_destiny(self, flight, n_days) -> None:
        destiny = Destiny(flight, self.n_passengers, n_days)
        if destiny.get_name() not in self.get_destinies_names() and destiny.get_name() != self.origin:
            self.destinies.add_destiny(destiny)

    def remove_destiny(self, destiny) -> None:
        destinies_aux = Destinies()
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) != destiny:
                destinies_aux.add_destiny(self.destinies.get_destiny(i))
        self.destinies = destinies_aux

    def confirm_reserve_flights(self):
        tryings = self.tryings
        while tryings > 1:
            tryings -= 1
            if self.skyscanner.confirm_reserve(self.user, self.get_flights()) is True:
                return True
        return False

    def get_cars(self) -> Cars:
        cars = Cars()
        for i in range(self.destinies.get_len()):
            cars.add_cars(self.destinies.get_cars(i))
        return cars

    def add_car(self, destiny, car):
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) == destiny:
                self.destinies.add_car(i, car)

    def remove_car(self, destiny, code):
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) == destiny:
                self.destinies.remove_car(i, code)

    def confirm_reserve_cars(self):
        tryings = self.tryings
        while tryings > 0:
            tryings -= 1
            if self.rentalcars.confirm_reserve(self.user, self.get_cars()) is True:
                return True
        return False

    # def confirm_reserve_cars(self):
    #     self.tryings -= 1
    #     if self.rentalcars.confirm_reserve(self.user, self.get_cars) is True:
    #         return True
    #     else:
    #         return self.retry_reserve_cars()
    #
    # def retry_reserve_cars(self):
    #     while self.tryings > 1:
    #         self.tryings -= 1
    #         if self.rentalcars.confirm_reserve(self.user, self.get_cars) is True:
    #             return True
    #     return self.rentalcars.confirm_reserve(self.user, self.get_cars)  # superat maxim intents

    def get_hotels(self) -> Hotels:
        hotels = Hotels()
        for i in range(self.destinies.get_len()):
            if self.destinies.get_hotel(i) is not None:
                hotels.add_hotel(self.destinies.get_hotel(i))
        return hotels

    def add_hotel(self, destiny, hotel):
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) == destiny:
                self.destinies.add_hotel(i, hotel)

    def remove_hotel(self, destiny):
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) == destiny:
                self.destinies.remove_hotel(i)

    def confirm_reserve_hotels(self):
        tryings = self.tryings
        while tryings > 0:
            tryings -= 1
            if self.booking.confirm_reserve(self.user, self.get_hotels()) is True:
                return True
        return False

    def add_user(self, user):
        self.user = user

    def add_payment_data(self, payment_data):
        self.payment_data = payment_data

    def set_payment_import(self):
        self.payment_data.set_reserve_amount(self.get_total_price())

    def do_payment(self):
        tryings = self.tryings
        while tryings > 0:
            tryings -= 1
            if self.bank.do_payment(self.user, self.payment_data) is True:
                return True
        return False


    # def do_payment(self):
    #     self.payment_data.calculate_reserve_amount(self.get_flights, self.get_hotels, self.get_cars)
    #     self.tryings -= 1
    #     bank_response = self.bank.do_payment(self.user, self.payment_data)
    #     if bank_response is True:
    #         return bank_response  # ho he hagut de posar així pel testMockV2 paymentMethod que cal que retorni method_payment
    #     else:
    #         return self.retry_payment()
    #
    # def retry_payment(self):
    #     while self.tryings > 1:
    #         self.tryings -= 1
    #         if self.bank.do_payment(self.user, self.payment_data) is True:
    #             return self.bank.do_payment(self.user, self.payment_data)
    #     return self.bank.do_payment(self.user, self.payment_data)  # superat maxim intents

    def get_payment_type(self):
        return self.payment_data.get_payment_type()