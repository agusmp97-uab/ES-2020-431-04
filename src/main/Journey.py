from . import Hotels
from . import Flights
from . import Cars
from . import Skyscanner
from . import Booking
from . import Rentalcars
from . import Bank

class Journey:
    def __init__(self, flights, user, payment_data, hotels=Hotels.Hotels(), cars=Cars.Cars()):
        self.bank = Bank.Bank()
        self.skyscanner = Skyscanner.Skyscanner()
        self.rentalcars = Rentalcars.Rentalcars()
        self.booking = Booking.Booking()
        self.flights = flights
        self.user = user
        self.payment_data = payment_data
        self.hotels = hotels
        #self.hotels.set_n_passengers(self.flights.get_n_passengers())
        self.cars = cars

    def set_flights(self, flights):
        self.flights = flights

    def set_hotels(self, hotels):
        self.hotels = hotels

    def set_cars(self, cars):
        self.cars = cars

    def set_payment_data(self, payment_data):
        self.payment_data = payment_data

    def get_payment_type(self):
        return self.payment_data.get_payment_type()

    def get_cars(self):
        return self.cars

    def get_reserve_amount(self):
        self.payment_data.calculate_reserve_amount(self.flights, self.hotels, self.cars)

    def set_user(self, user):
        self.user = user

    def confirm_reserve_flights(self):
        return self.skyscanner.confirm_reserve(self.user, self.flights)

    def do_payment(self):
        self.payment_data.calculate_reserve_amount(self.flights, self.hotels, self.cars)
        return self.bank.do_payment(self.user, self.payment_data)

    def confirm_reserve_cars(self):
        return self.rentalcars.confirm_reserve(self.user, self.cars)

    def confirm_reserve_hotels(self):
        return self.skyscanner.confirm_reserve(self.user, self.hotels)