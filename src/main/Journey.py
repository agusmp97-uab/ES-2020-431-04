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
    def __init__(self, n_passengers, origin):
        self.tryings = 3

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
        self.billing_user = None

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
        self.tryings = 3
        response = False
        while self.tryings > 0:
            self.tryings -= 1
            response = self.skyscanner.confirm_reserve(self.user, self.get_flights())
            if response is True:
                return response
        return response

    def get_cars(self) -> Cars:
        cars = Cars.Cars()
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
        self.tryings = 3
        response = False
        while self.tryings > 0:
            self.tryings -= 1
            response = self.rentalcars.confirm_reserve(self.user, self.get_cars())
            if response is True:
                return response
        return response

    def get_hotels(self) -> Hotels:
        hotels = Hotels.Hotels()
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
        self.tryings = 3
        response = False
        while self.tryings > 0:
            self.tryings -= 1
            response = self.booking.confirm_reserve(self.user, self.get_hotels())
            if response is True:
                return response
        return response

    def add_user(self, user):
        self.user = user

    def add_payment_data(self, payment_data):
        self.payment_data = payment_data
        self.set_payment_import()

    def set_payment_import(self):
        self.payment_data.set_reserve_amount(self.get_total_price())

    def add_billing_user(self, billing_user):
        if billing_user.check_billing_user() is True:
            self.billing_user = billing_user
            return True
        else:
            return False

    def get_billing_user(self):
        return self.billing_user

    def do_payment(self):
        self.tryings = 3
        response = False
        while self.tryings > 0:
            self.tryings -= 1
            response = self.bank.do_payment(self.billing_user, self.payment_data)
            if response is True:
                return response
        return response

    def get_payment_type(self):
        return self.payment_data.get_payment_type()

    def get_tryings(self):
        return self.tryings

