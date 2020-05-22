from src.test.conftest import *


class TestMockV1:

    def test_do_payment(self, monkeypatch, payment_data, user, journey):
        def mock_return(self, user, payment_data):
            return True
        monkeypatch.setattr(Bank, "do_payment", mock_return)
        assert journey.do_payment() is True

    def test_do_reserve(self, monkeypatch, payment_data, user, journey):
        def mock_return(self, user, flights):
            return True
        monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_return)
        assert journey.confirm_reserve_flights() is True


