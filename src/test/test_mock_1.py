from src.test.conftest import *
#from pytest import mock

#import Gestor as GS  # hem de tenir accés als classesdiverse.py. Falta com un __init__ per l'estructura o quelcom així.(Vaig faltar a la classe de FI sobre includes i sempre he arroseguat aquesta part :(

class Test_mock_1(unittest.TestCase):

    @mock.patch('src.Bank')  # creem un camaleo que  es farà passa per la classe indicada ('   ')
    def test_pagoViaje(self, mock_Bank ): # posem l'assignació del camaleó jus a sobre de la def del test
        self.assertTrue(mock_Bank.do_payment)
        mock_Bank.do_payment.return_value = False  # ara li diem al camaleó que retorni sempre false quan li demanin dopayment
        self.assertFalse(mock_Bank.do_payment)

    @mock.patch('src.Bank')
    def test_avisoErrorPago(self,mock_Bank):
        mock_Bank.do_payment.return_value = False
        viatge = Flights() # la classe viatge o reserva que tinguem ...
        self.assertFalse(gestor.realitzaPagament(viatge,mock_Bank))  # aquí li diem al nostre objecte gestor que envii ordre de pagament al banc per limport del viatge. Si el bank retorna False, el gestor comunicarà que no s'ha pogut cobrar amb un  false





