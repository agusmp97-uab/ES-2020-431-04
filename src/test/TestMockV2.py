import src.main.Flights
from src.test.conftest import *
from src.main.Bank import Bank
import src.main.Flights
from src.main.Journey import Journey
from src.test.conftest import *

# creem els diferents test mock com def test_ ..............  sempre han de començar amb el key-word 'test_'


class TestMockV2:

    def test_more_than_one_of_all_paymentmode_ok(self, monkeypatch,  capsys, flights_multiple_passengers, user, payment_data): # posem l'assignació del camaleó jus a sobre de la def del test
        def mockreturn(self, user, payment_data):
            return True

        monkeypatch.setattr(Bank,"do_payment", mockreturn)
        journey = Journey(flights_multiple_passengers[0],user, payment_data)
        assert journey.payment_data.payment_type == payment_data.payment_type

    def test_more_than_one_of_all_payment_fail(self, monkeypatch,  capsys, flights_multiple_passengers, user, payment_data): # posem l'assignació del camaleó jus a sobre de la def del test
        def mockreturn(self, user, payment_data):
            return False

        monkeypatch.setattr(Bank,"do_payment", mockreturn)
        journey = Journey(flights_multiple_passengers[0],user, payment_data)
        assert journey.do_payment() == False

    def test_more_than_one_of_all_flights_no_more(self, monkeypatch,  capsys, flights_multiple_passengers, user, payment_data): # posem l'assignació del camaleó jus a sobre de la def del test
        aux, aux2 = flights_multiple_passengers
        def mockreturn(self, user, aux):
            return False

        monkeypatch.setattr(Skyscanner,"confirm_reserve", mockreturn)
        journey = Journey(flights_multiple_passengers[0],user, payment_data)
        assert journey.confirm_reserve_flights() == False
