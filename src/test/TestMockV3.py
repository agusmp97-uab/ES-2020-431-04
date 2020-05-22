import src.main.Flights
from src.test.conftest import *
from src.main.Bank import Bank
import src.main.Flights
from src.main.Journey import Journey
from src.test.conftest import *


class TestMockV3:

    """ When the reserve of the cars is confirmed, the program reports it"""
    def test_do_car_reserve(self, monkeypatch, journey_with_cars, user):
        def mock_return(self, user, cars):
            return True
        monkeypatch.setattr(Rentalcars, "confirm_reserve", mock_return)

        journey_with_cars.add_user(user)
        assert journey_with_cars.confirm_reserve_cars() is True

    """ When there is an error on the reserve of the cars, the program reports it"""
    def test_do_reserve_cars_fail(self, monkeypatch, journey_with_cars, user):
        def mock_return(self, user, cars):
            return False
        monkeypatch.setattr(Rentalcars, "confirm_reserve", mock_return)

        journey_with_cars.add_user(user)
        assert journey_with_cars.confirm_reserve_cars() is False

    """ When the reserve of the hotels is confirmed, the program reports it"""
    def test_do_hotel_reserve(self, monkeypatch, journey_with_cars_and_hotels, user):
        def mock_return(self, user, hotels):
            return True
        monkeypatch.setattr(Booking, "confirm_reserve", mock_return)

        journey_with_cars_and_hotels.add_user(user)
        assert journey_with_cars_and_hotels.confirm_reserve_hotels() is True

    """ When there is an error on the reserve of the hotels, the program reports it"""
    def test_do_hotel_reserve_fail(self, monkeypatch, journey_with_cars_and_hotels, user):
        def mock_return(self, user, hotels):
            return False
        monkeypatch.setattr(Booking, "confirm_reserve", mock_return)

        journey_with_cars_and_hotels.add_user(user)
        assert journey_with_cars_and_hotels.confirm_reserve_hotels() is False

