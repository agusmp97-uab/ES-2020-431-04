from src.test.conftest import *
#from pytest import mock

class TestMockV1:

   def test_do_payment(self, monkeypatch, capsys, payment_data, user, flights_multiple_passengers):
       def mockreturn(self, user, payment_data):
           return False

       monkeypatch.setattr(Bank, "do_payment", mockreturn)

       journey = Journey(flights_multiple_passengers[0], user, payment_data)
       assert journey.do_payment() == False


       #assert de prints
       #captured = capsys.readouterr()
       #assert captured.out == "hello\n"



