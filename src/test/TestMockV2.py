import src.main.Flights
from src.test.conftest import *
from src.main.Bank import Bank
import src.main.Flights
from src.main.Journey import Journey
from src.test.conftest import *


class TestMockV2:

    def test_payment_method(self, monkeypatch, flights_multiple_passengers, user, payment_data_type):
        def mock_return(self, user, payment_data):
            return payment_data.get_payment_type()

        monkeypatch.setattr(Bank, "do_payment", mock_return)
        journey = Journey(flights_multiple_passengers[0], user, payment_data_type[0])
        assert journey.do_payment() == payment_data_type[1][0]

    # def test_do_payment_fail(self, monkeypatch, flights_multiple_passengers, user, payment_data):
    #     def mock_return(self, user, payment_data):
    #         return False
    #
    #     monkeypatch.setattr(Bank, "do_payment", mock_return)
    #     journey = Journey(flights_multiple_passengers[0], user, payment_data[0])
    #     assert journey.do_payment() is False
    #
    # def test_do_reserve_fail(self, monkeypatch, flights_multiple_passengers, user, payment_data):
    #     def mock_return(self, user, aux):
    #         return False
    #
    #     monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_return)
    #     journey = Journey(flights_multiple_passengers[0], user, payment_data[0])
    #     assert journey.confirm_reserve_flights() is False
