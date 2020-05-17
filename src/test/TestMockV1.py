from src.test.conftest import *


class TestMockV1:

    def test_do_payment(self, monkeypatch, payment_data, user, flights_multiple_passengers):
        def mock_return(self, user, payment_data):
            return True
        monkeypatch.setattr(Bank, "do_payment", mock_return)

        journey = Journey(flights_multiple_passengers[0], user, payment_data[0])
        assert journey.do_payment() is True

       #captured = capsys.readouterr()
       #assert captured.out == "correcte\n"

    def test_do_reserve(self, monkeypatch, payment_data, user, flights_multiple_passengers):
        def mock_return(self, user, flights):
            return True
        monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_return)

        journey = Journey(flights_multiple_passengers[0], user, payment_data[0])
        assert journey.confirm_reserve_flights() is True


