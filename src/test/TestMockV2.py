from src.main.Bank import Bank
import src.main.Flights

import unittest
from unittest import mock
from src.main.Flight import Flight
from src.main.Flights import Flights
from src.main.PaymentData import PaymentData
from src.main.User import User


class TestMockV2(unittest.TestCase):

    payment = PaymentData("VISA","Juanma Pamundi", 123,123)
    payment.set_reserve_amount(1989)
    client = User("Juanma Pamundi", 46991566, "postal_address", "phone_number", "email")
    @mock.patch('src.main.Bank')  # creem un camaleo que es farà passar per la classe indicada ('   ')
    @mock.patch(client)
    @mock.patch(payment)
    def test_more_than_one_of_all_paymentmode_ok(self, mock_bank, client, payment): # posem l'assignació del camaleó jus a sobre de la def del test

        mock_bank.do_payment.return_value = payment.payment_type
        self.assertTrue(mock_bank.do_payment(client, payment), payment)



    def test_more_than_one_of_all_paymentmode_false(self, mock_bank, client, payment): # posem l'assignació del camaleó jus a sobre de la def del test
        mock_bank.do_payment.return_value = False  # Payment error
        self.assertTrue(mock_bank.do_payment(client, payment), payment)



    # @mock.patch('src.Bank')
    # def test_avisoErrorPago(self,mock_Bank):
    #     mock_Bank.do_payment.return_value = False
    #     viatge = Flights() # la classe viatge o reserva que tinguem ...
    #     self.assertFalse(gestor.realitzaPagament(viatge,mock_Bank))  # aquí li diem al nostre objecte gestor que envii ordre de pagament al banc per limport del viatge. Si el bank retorna False, el gestor comunicarà que no s'ha pogut cobrar amb un  false
