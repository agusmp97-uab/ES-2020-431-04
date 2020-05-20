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
        self.tryings = 3  # el nombre de reintents s'inicialitaza quan comença el primer do_payment/confirm_reserve. Podriem fer que es passes al constructor i fos configurable

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

    def get_tryings(self):
        return self.tryings

    def get_cars(self):
        return self.cars

    def get_reserve_amount(self):
        return self.payment_data.calculate_reserve_amount(self.flights, self.hotels, self.cars)

    def set_user(self, user):
        self.user = user

    def confirm_reserve_flights(self):
        self.tryings -= 1
        if self.skyscanner.confirm_reserve(self.user, self.flights) is True:
            return True
        else:
            return self.retry_reserve_flights()

    def retry_reserve_flights(self):
        while self.tryings > 1:
            self.tryings -= 1
            if self.skyscanner.confirm_reserve(self.user, self.flights) is True:
                return True
        return self.skyscanner.confirm_reserve(self.user, self.flights)  # superat maxim intents

    def confirm_reserve_cars(self):
        return self.rentalcars.confirm_reserve(self.user, self.cars)

    def confirm_reserve_hotels(self):
        return self.skyscanner.confirm_reserve(self.user, self.hotels)

    def do_payment(self):
        self.payment_data.calculate_reserve_amount(self.flights, self.hotels, self.cars)
        self.tryings -= 1
        bank_response =self.bank.do_payment(self.user, self.payment_data)
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