from . import Hotels
from . import Flights
from . import Cars
from . import Skyscanner
from . import Booking
from . import Rentalcars
from . import Bank

class Journey:
    def __init__(self, flights, user, payment_data, hotels=Hotels(), cars=Cars()):
        self.bank = Bank()
        self.skyscanner = Skyscanner()
        self.rentalcars = Rentalcars()
        self.booking = Booking()
        self.flights = flights
        self.user = user
        self.payment_data = payment_data
        self.hotels = hotels
        self.cars = cars

    def set_flights(self, flights):
        self.flights = Flights

    def set_hotels(self, hotels):
        self.hotels = hotels

    def set_cars(self, cars):
        self.cars = cars

    def set_payment_data(self, payment_data):
        self.payment_data = payment_data

    def set_user(self, user):
        self.user = user

    def confirm_reserve_flights(self):
        self.skyscanner.confirm_reserve(self.user, self.flights)

    def do_payment(self):
        self.payment_data.calculate_reserve_amount(self.flights, self.hotels, self.cars)
        self.bank.do_payment(self.user, self.payment_data)

