import src.main.Flights
from src.test.conftest import *
from src.main.Bank import Bank
import src.main.Flights
from src.main.Journey import Journey
from src.test.conftest import *
from src.main.Journey import Journey


class TestMockV4:

    def test_retry_payment(self, monkeypatch, flights_multiple_passengers, user, payment_data):
        def mock_return(self, user, payment_data):
            return False

        monkeypatch.setattr(Bank, "do_payment", mock_return)
        journey = Journey(flights_multiple_passengers[0], user, payment_data[0])
        journey.do_payment()
        assert journey.get_tryings() < 2   # default nombre intents 3 si ha de fer reintent llavors 3-2 = 1


    def test_retry_payment_success(self, monkeypatch, flights_multiple_passengers, user, payment_data):
        def mock_return(self, user, payment_data):
            return True

        monkeypatch.setattr(Bank, "do_payment", mock_return)
        journey = Journey(flights_multiple_passengers[0], user, payment_data[0])
        assert journey.retry_payment() is True


    def test_retry_payment_max_reties(self, monkeypatch, flights_multiple_passengers, user, payment_data):
        def mock_return(self, user, payment_data):
            return False

        monkeypatch.setattr(Bank, "do_payment", mock_return)
        journey = Journey(flights_multiple_passengers[0], user, payment_data[0])
        assert journey.do_payment() is False


    def test_retry_flights_reserve(self, monkeypatch, flights_multiple_passengers, user, payment_data):
        def mock_return(self, user, aux):
            return False

        monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_return)
        journey = Journey(flights_multiple_passengers[0], user, payment_data[0])
        journey.confirm_reserve_flights()
        assert journey.get_tryings() < 2  # default nombre intents 3 si ha de fer reintent llavors 3-2 = 1

    def test_retry_flights_reserve_success(self, monkeypatch, flights_multiple_passengers, user, payment_data):
        def mock_return(self, user, payment_data):
            return True

        monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_return)
        journey = Journey(flights_multiple_passengers[0], user, payment_data[0])
        assert journey.retry_payment() is True


    def test_retry_flights_reserve_max_reties(self, monkeypatch, flights_multiple_passengers, user, payment_data):
        def mock_return(self, user, payment_data):
            return False

        monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_return)
        journey = Journey(flights_multiple_passengers[0], user, payment_data[0])
        assert journey.confirm_reserve_flights() is False



