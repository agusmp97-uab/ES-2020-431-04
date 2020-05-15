import pytest
from src.main.Flights import Flights
from src.main.Flight import Flight


@pytest.mark.parametrize("n_passengers, journey", [
    (1, Flights(1, "BCN").add_flights([Flight("ROM", "1", 20), Flight("PAR","2",50), Flight("BCN","3",70)])),
    (4, Flights(4, "BCN")),
    (6, Flights(6, "BCN").add_flights([Flight("ROM", "1", 20), Flight("BCN","5",100)])),
])

def test_get_n_passengers(n_passengers, journey):
    assert journey.get_n_passengers() == n_passengers  # Need n_passatgers per guardar el nombre de viatjers

@pytest.mark.parametrize("journey", [
    (Flights(1, "BCN")),
    (Flights(4, "BCN")),
    (Flights(6, "BCN")),
])
def test_get_destinies_journey_wo_destinies(journey):
    assert len(journey.get_destinies()) == 0  # Need atribut flights per guardar les destinacions

@pytest.mark.parametrize("journey", [
    (Flights(1, "BCN")),
    (Flights(4, "BCN")),
    (Flights(6, "BCN")),
])
def test_get_flights_journey_wo_destinies(journey):
    assert len(journey.get_flights()) == 0  # Need atribut flights per guardar les destinacions

@pytest.mark.parametrize("journey", [
    (Flights(1, "BCN")),
    (Flights(4, "BCN")),
    (Flights(6, "BCN")),
])
def test_get_price_journey_wo_destinies(journey):
    assert journey.get_price() == 0

@pytest.mark.parametrize("journey, flight, destinies", [
    (Flights(1, "BCN").add_flights([Flight("ROM", "1", 20), Flight("PAR","2",50), Flight("BCN","3",70)])),
    (Flights(4, "BCN")),
    (Flights(6, "BCN").add_flights([Flight("ROM", "1", 20), Flight("BCN","5",100)])),
])

def test_anadirDestino_Destlist(self, viaje_anadir_destinos, destincacions):
    #aux = viaje_anadir_destinos.Flights
    # aux.append(destincacions[0])
    # vol = Flight(destincacions[0])  # la resta de parametres quede a NONE si no s'indiquen
# viaje_anadir_destinos.add_flight(vol)
    #assert [f.get_destiny() for f in viaje_anadir_destinos.Flights] == aux  # mirem si ha quedat com ha de.

#def test_anadirDestino_Flighlist(self, viaje_anadir_destinos,destincacions):
   # aux = viaje_anadir_destinos.Flights
    # aquí no pillo com funcionaria el què ha de passar perk un destino no porta incorporat el vol

