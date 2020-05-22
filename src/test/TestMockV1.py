from src.test.conftest import *


class TestMockV1:

    def test_do_payment(self, monkeypatch, payment_data, billing_user, journey_multiple_passengers):
        def mock_return(self, user, payment_data):
            return True
        monkeypatch.setattr(Bank, "do_payment", mock_return)

        journey_multiple_passengers[0].add_payment_data(payment_data)
        assert journey_multiple_passengers[0].do_payment(billing_user) is True

    def test_do_reserve(self, monkeypatch, user, journey_multiple_passengers):
        def mock_return(self, user, flights):
            return True
        monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_return)

        journey_multiple_passengers[0].add_user(user)
        assert journey_multiple_passengers[0].confirm_reserve_flights() is True


