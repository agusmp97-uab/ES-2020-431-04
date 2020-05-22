import src.main.Flights
from src.test.conftest import *
from src.main.Bank import Bank
import src.main.Flights
from src.main.Journey import Journey
from src.test.conftest import *


class TestMockV2:

    def test_payment_method(self, monkeypatch, journey_multiple_passengers, billing_user, payment_data_type):
        def mock_return(self, user, payment_data):
            return payment_data.get_payment_type()
        monkeypatch.setattr(Bank, "do_payment", mock_return)

        journey_multiple_passengers[0].add_payment_data(payment_data_type[0])
        assert journey_multiple_passengers[0].do_payment(billing_user) == payment_data_type[1][0]

    def test_do_payment_fail(self, monkeypatch, journey_multiple_passengers, billing_user, payment_data):
        def mock_return(self, user, payment_data):
            return False
        monkeypatch.setattr(Bank, "do_payment", mock_return)

        journey_multiple_passengers[0].add_payment_data(payment_data)
        assert journey_multiple_passengers[0].do_payment(billing_user) is False

    def test_do_reserve_fail(self, monkeypatch, journey_multiple_passengers, user):
        def mock_return(self, user, aux):
            return False
        monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_return)

        journey_multiple_passengers[0].add_user(user)
        assert journey_multiple_passengers[0].confirm_reserve_flights() is False
