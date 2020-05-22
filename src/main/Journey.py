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

""" Class that contains the information of a journey, and implements the reservations and payment of the journey"""
class Journey:
    def __init__(self, n_passengers, origin):
        #number of attemps to make a reservation/payment
        self.tryings = 3

        self.bank = Bank.Bank()
        self.skyscanner = Skyscanner.Skyscanner()
        self.rentalcars = Rentalcars.Rentalcars()
        self.booking = Booking.Booking()

        #number of passengers of the joourney
        self.n_passengers = n_passengers
        self.destinies = Destinies()
        #Name (string) of the origin of the journey
        self.origin = origin
        #Return flight (to the origin) of the journey
        self.return_flight = None

        self.payment_data = None
        #Information of the user making the reservations
        self.user = None
        #Information of the user that will appear on the bill data
        self.billing_user = None

    """ Returns the total price of the journey, given by its flights, hotels and cars"""
    def get_total_price(self) -> float:
        total_price = 0
        for i in range(self.destinies.get_len()):
            total_price += self.destinies.get_price(i)
        if self.return_flight is not None:
            total_price += self.return_flight.get_price() * self.n_passengers
        return total_price

    """ Returns the origin (string) of the journey"""
    def get_origin(self) -> str:
        return self.origin

    """ Returns the number of passengers involved on the journey"""
    def get_n_passengers(self) -> int:
        return self.n_passengers

    """ Given a destiny (string), if the destiny belongs to the journey, returns the number of days
    corresponding to that destiny on the journey"""
    def get_n_days(self, destiny) -> int:
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) == destiny:
                return self.destinies.get_destiny(i).get_n_days()

    """ Returns the names of the destinies of the journey"""
    def get_destinies_names(self) -> list:
        destinies = []
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) != self.origin:
                destinies.append(self.destinies.get_name(i))
        return destinies

    """ Returns the flights of the journey"""
    def get_flights(self) -> Flights:
        flights = Flights.Flights()
        for i in range(self.destinies.get_len()):
            flights.add_flight(self.destinies.get_flight(i))
        if self.return_flight is not None:
            flights.add_flight(self.return_flight)
        return flights

    """ Add the return flight of the journey"""
    def add_return_flight(self, return_flight):
        self.return_flight = return_flight

    """ Add a destiny to the journey, from the corresponding flight and number of days"""
    def add_destiny(self, flight, n_days) -> None:
        destiny = Destiny(flight, self.n_passengers, n_days)
        if destiny.get_name() not in self.get_destinies_names() and destiny.get_name() != self.origin:
            self.destinies.add_destiny(destiny)

    """ Given the name of a destiny (string), if its on the journey, it's removed from it."""
    def remove_destiny(self, destiny) -> None:
        destinies_aux = Destinies()
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) != destiny:
                destinies_aux.add_destiny(self.destinies.get_destiny(i))
        self.destinies = destinies_aux

    """ Confirm the reserve of the flights of the journey on the SkyScanner's API.  It tries it 3 times."""
    def confirm_reserve_flights(self):
        self.tryings = 3
        response = False
        while self.tryings > 0:
            self.tryings -= 1
            response = self.skyscanner.confirm_reserve(self.user, self.get_flights())
            if response is True:
                return response
        return response

    """ Returns the cars of the journey"""
    def get_cars(self) -> Cars:
        cars = Cars.Cars()
        for i in range(self.destinies.get_len()):
            cars.add_cars(self.destinies.get_cars(i))
        return cars

    """ Add the given car to the given destiny of the journey"""
    def add_car(self, destiny, car):
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) == destiny:
                self.destinies.add_car(i, car)

    """ Given a car code, remove the corresponding car on the given destiny"""
    def remove_car(self, destiny, code):
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) == destiny:
                self.destinies.remove_car(i, code)

    """ Confirm the reserve of the cars of the journey on the RentalCar's API.  It tries it 3 times."""
    def confirm_reserve_cars(self):
        self.tryings = 3
        response = False
        while self.tryings > 0:
            self.tryings -= 1
            response = self.rentalcars.confirm_reserve(self.user, self.get_cars())
            if response is True:
                return response
        return response

    """ Returns the hotels of the journey"""
    def get_hotels(self) -> Hotels:
        hotels = Hotels.Hotels()
        for i in range(self.destinies.get_len()):
            if self.destinies.get_hotel(i) is not None:
                hotels.add_hotel(self.destinies.get_hotel(i))
        return hotels

    """ Add the given hotel to the given destiny of the journey"""
    def add_hotel(self, destiny, hotel):
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) == destiny:
                self.destinies.add_hotel(i, hotel)

    """ Remove the hotel of a given destiny"""
    def remove_hotel(self, destiny):
        for i in range(self.destinies.get_len()):
            if self.destinies.get_name(i) == destiny:
                self.destinies.remove_hotel(i)

    """ Confirm the reserve of the hotels of the journey on the Booking's API.  It tries it 3 times."""
    def confirm_reserve_hotels(self):
        self.tryings = 3
        response = False
        while self.tryings > 0:
            self.tryings -= 1
            response = self.booking.confirm_reserve(self.user, self.get_hotels())
            if response is True:
                return response
        return response

    "Add the information of the user reservating"
    def add_user(self, user):
        self.user = user

    "Add the payment data"
    def add_payment_data(self, payment_data):
        self.payment_data = payment_data
        self.set_payment_import()

    "Set the import of the payment data to the total price of the journey"
    def set_payment_import(self):
        self.payment_data.set_reserve_amount(self.get_total_price())

    "Add the information of the user that will appear on the bill (if it's correct)"
    def add_billing_user(self, billing_user):
        if billing_user.check_billing_user() is True:
            self.billing_user = billing_user
            return True
        else:
            return False

    "Returns the information of the user that will appear on the bill"
    def get_billing_user(self):
        return self.billing_user

    """ Make the payment on the Bank's API. It tries it 3 times."""
    def do_payment(self):
        self.tryings = 3
        response = False
        while self.tryings > 0:
            self.tryings -= 1
            response = self.bank.do_payment(self.billing_user, self.payment_data)
            if response is True:
                return response
        return response

    """ Returns the type of payment"""
    def get_payment_type(self):
        return self.payment_data.get_payment_type()

    """ Returns the number of tryings remaining on the last try to reserve/pay some element of the journey"""
    def get_tryings(self):
        return self.tryings

