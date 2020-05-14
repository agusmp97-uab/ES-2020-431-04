import unittest
from unittest import mock
import main.Flights as FLS
import main.Flight as FL

num_passatgers = 4
destincacions = ["BCN","PARIS","BERLIN","ESTOCOLM","MOSCOU"]


class Test_v1(unittest.TestCase):

    viaje_sin_destinos = FLS.Flights(num_passatgers)
    viaje_anadir_destinos = FLS.Flights(num_passatgers)

    def test_num_viajeros(self,viaje_sin_destinos,num_passatgers):
        assert viaje_sin_destinos.n_passatge == 4  # Need n_passatgers per guardar el nombre de viatjers

    def test_sinDestinos_emptyDestlist(self,viaje_sin_destinos):
        assert len(viaje_sin_destinos.Fligths) == 0  # Need atribut flights per guardar les destinacions

    def test_sinVuelos(self,viaje_sin_destinos):
        assert len(viaje_sin_destinos.Fligths) == 0  # Need atribut flights per guardar les destinacions

    def test_precioInicialZero(self,viaje_sin_destinos):
        assert viaje_sin_destinos.total_price == 0

    def test_anadirDestino_Destlist(self, viaje_anadir_destinos, destincacions):
        aux = viaje_anadir_destinos.Flights
        aux.append(destincacions[0])
        vol = FL.Flight(destincacions[0])  # la resta de parametres quede a NONE si no s'indiquen
        viaje_anadir_destinos.add_flight(vol)
        assert [f.get_destiny() for f in viaje_anadir_destinos.Flights] == aux  # mirem si ha quedat com ha de.

    def test_anadirDestino_Flighlist(self,viaje_anadir_destinos,destincacions):
        aux = viaje_anadir_destinos.Flights
        # aquí no pillo com funcionaria el què ha de passar perk un destino no porta incorporat el vol

    def test_anadirDestino_updatePrice(self):
        pass

    def test_anadirDestino_multiplesViajeros_updatePrice(self):
        pass

    def test_quitarDest_viajeMultiDest_Destlist(self):
        pass

    def test_quitarDest_viajeMultiDest_Flightlist(self):
        pass

    def test_quitarDest_viajeMultiDest_updatePrice(self):
        pass

    def test_multiDest_mulitViajeros_quitarDest_updatePrice(self):
        pass

    def test_multiDest_mulitViajeros_dopaymentOK_reportaOK(self): #  Aquest va al mock perquè cal mockejar la API perquè doni el TRUE a do_payment
        pass

    def test_multiDest_mulitViajeros_confirm_reserveOK_reportaOK(self):  # Aquest va al mock perquè cal mockejar la API perquè doni el TRUE a confirm_reserve
        pass