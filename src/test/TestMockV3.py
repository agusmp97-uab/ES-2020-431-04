import src.main.Flights
from src.test.conftest import *
from src.main.Bank import Bank
import src.main.Flights
from src.main.Journey import Journey
from src.test.conftest import *


class TestMockV3:

    def test_do_car_reserve(self, monkeypatch, flights_multiple_passengers, user, payment_data, cars):
        def mock_return(self, user, cars):
            return True
        monkeypatch.setattr(Rentalcars, "confirm_reserve", mock_return)

        journey = Journey(flights_multiple_passengers[0], user, payment_data[0], None, cars[0])
        assert journey.confirm_reserve_cars() is True


    def test_do_reserve_cars_fail(self, monkeypatch, cars, user, payment_data):
        def mock_return(self, user, aux):
            return False

        monkeypatch.setattr(Rentalcars, "confirm_reserve", mock_return)
        journey = Journey(flights_multiple_passengers[0], user, payment_data[0], cars[0], hotels[0])
        assert journey.confirm_reserve_cars() is False