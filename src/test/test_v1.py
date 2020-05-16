import pytest
from src.main.Flights import Flights
from src.main.Flight import Flight


@pytest.fixture(params=[1, 2, 3, 4, 5, 6, 7, 0, 23, 50])
def empty_flights(request):
    flights_list = []

@pytest.fixture(params=[
    (1, "BCN", [Flight("ROM", "2", 50), Flight("PAR", "21", 100), Flight("PRA", "22", 200), Flight("BCN", "432", 200)]),
    (1, "BCN", [Flight("ROM", "2", 50), Flight("BCN", "4", 40)]),
    (1, "BCN", [Flight("ROM", "2", 50), Flight("BCN", "4", 40)]),
    (1, "ROM", [Flight("PAR", "21", 100), Flight("ROM", "22", 200)]),
    (1, "BCN", [Flight("NY", "1", 5000), Flight("LA", "2", 400), Flight("BCN", "3", 200)]),
    (1, "BCN", [Flight("ATH", "2", 500), Flight("BER", "3", 700), Flight("BCN", "4", 300)]),
    (1, "BCN", [Flight("MAD", "2", 50), Flight("BCN", "21", 60)]),
    (1, "BCN", [Flight("MAD", "2", 50), Flight("BCN", "21", 60)]),
    (1, "BCN", []),
    (1, "BCN", []),
])
def flights_1_passenger(request):
    flights = Flights(request.param[0], request.param[1])
    flights.add_flights(request.param[2])
    return flights, request.param

@pytest.fixture(params=[
    (1, "BCN", [Flight("ROM", "2", 50), Flight("PAR", "21", 100), Flight("PRA", "22", 200), Flight("BCN", "432", 200)]),
    (1, "BCN", [Flight("ROM", "2", 50), Flight("BCN", "4", 40)]),
    (1, "BCN", [Flight("ROM", "2", 50), Flight("BCN", "4", 40)]),
    (1, "ROM", [Flight("PAR", "21", 100), Flight("ROM", "22", 200)]),
    (1, "BCN", [Flight("NY", "1", 5000), Flight("LA", "2", 400), Flight("BCN", "3", 200)]),
    (1, "BCN", [Flight("ATH", "2", 500), Flight("BER", "3", 700), Flight("BCN", "4", 300)]),
    (1, "BCN", [Flight("MAD", "2", 50), Flight("BCN", "21", 60)]),
    (1, "BCN", [Flight("MAD", "2", 50), Flight("BCN", "21", 60)]),
    (1, "BCN", []),
    (1, "BCN", []),
])
def flights_multiple_passenger(request):
    flights = Flights(request.param[0], request.param[1])
    flights.add_flights(request.param[2])
    return flights, request.param

@pytest.fixture(params=[Flight("ROM", "2", 50), Flight("PAR", "2", 50)])
def flight(request):
    return request.param

flights = Flights(request.param, "BCN")
return flights



def test_add_flight(flights, flight):
    expected_output = flight.get_price()
    for f in flights[1][2]:
        expected_output += f.get_price()
    expected_output *= flights[1][0]

    flights[0].add_flight(flight)
    assert flights[0].get_price() == expected_output

def test_add_flight_destinies(flights, flight):
    expected_output = []
    expected_output.append(flight.get_destiny())
    for i in flights[1][2]:
        expected_output += i.get_destiny()

    flights[0].add_flight(flight)
    assert flights[0].get_destinies() == expected_output


@pytest.fixture(params=[
    (1, "BCN", [Flight("ROM", "2", 50), Flight("PAR", "21", 100), Flight("PRA", "22", 200), Flight("BCN", "432", 200)]),
    (2, "BCN", [Flight("ROM", "2", 50), Flight("BCN", "4", 40)]),
    (4, "BCN", [Flight("ROM", "2", 50), Flight("BCN", "4", 40)]),
    (2, "ROM", [Flight("PAR", "21", 100), Flight("ROM", "22", 200)]),
    (1, "BCN", [Flight("NY", "1", 5000), Flight("LA", "2", 400), Flight("BCN", "3", 200)]),
    (1, "BCN", [Flight("ATH", "2", 500), Flight("BER", "3", 700), Flight("BCN", "4", 300)]),
    (1, "BCN", [Flight("MAD", "2", 50), Flight("BCN", "21", 60)]),
    (2, "BCN", [Flight("MAD", "2", 50), Flight("BCN", "21", 60)]),
    (1, "BCN", []),
    (2, "BCN", []),
])
def flights(request):
    flights = Flights(request.param[0], request.param[1])
    flights.add_flights(request.param[2])
    return flights, request.param

def test_get_destinies_journey_wo_destinies2(empty_flights):
    assert len(empty_flights.get_destinies()) == 0  # Need atribut flights per guardar les destinacions

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



#def test_anadirDestino_Destlist(self, viaje_anadir_destinos, destincacions):
    #aux = viaje_anadir_destinos.Flights
    # aux.append(destincacions[0])
    # vol = Flight(destincacions[0])  # la resta de parametres quede a NONE si no s'indiquen
# viaje_anadir_destinos.add_flight(vol)
    #assert [f.get_destiny() for f in viaje_anadir_destinos.Flights] == aux  # mirem si ha quedat com ha de.

#def test_anadirDestino_Flighlist(self, viaje_anadir_destinos,destincacions):
   # aux = viaje_anadir_destinos.Flights
    # aquí no pillo com funcionaria el què ha de passar perk un destino no porta incorporat el vol

