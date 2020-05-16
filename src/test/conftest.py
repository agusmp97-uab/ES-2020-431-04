import pytest
from src.main.Flights import Flights
from src.main.Flight import Flight
from src.main.User import User
from src.main.PaymentData import PaymentData

@pytest.fixture(params=[1, 2, 3, 4, 5, 6, 7, 0, 23, 50])
def empty_flights(request):
    flights = Flights(request.param, "BCN")
    return flights

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
    (2, "BCN", [Flight("ROM", "2", 50), Flight("PAR", "21", 100), Flight("PRA", "22", 200), Flight("BCN", "432", 200)]),
    (3, "BCN", [Flight("ROM", "2", 50), Flight("BCN", "4", 40)]),
    (4, "BCN", [Flight("ROM", "2", 50), Flight("BCN", "4", 40)]),
    (2, "ROM", [Flight("PAR", "21", 100), Flight("ROM", "22", 200)]),
    (2, "BCN", [Flight("NY", "1", 5000), Flight("LA", "2", 400), Flight("BCN", "3", 200)]),
    (3, "BCN", [Flight("ATH", "2", 500), Flight("BER", "3", 700), Flight("BCN", "4", 300)]),
    (5, "BCN", [Flight("MAD", "2", 50), Flight("BCN", "21", 60)]),
    (2, "BCN", [Flight("MAD", "2", 50), Flight("BCN", "21", 60)]),
    (3, "BCN", []),
    (2, "BCN", []),
])
def flights_multiple_passengers(request):
    flights = Flights(request.param[0], request.param[1])
    flights.add_flights(request.param[2])
    return flights, request.param

@pytest.fixture(params=[
    Flight("ROM", "2", 50),
    Flight("PAR", "2", 50),
    Flight("ATH", "165", 300),
    Flight("NY", "58", 3000),
    Flight("MAD", "14", 10),
    Flight("SEV", "213", 30),
    Flight("LA", "165", 5000),
    Flight("ATH", "165", 300),
    Flight("ATH", "165", 300),
    Flight("ATH", "165", 300),
])
def flight(request):
    return request.param


@pytest.fixture(params=["PAR", "ROM", "ATH", "BER", "BAR", "MAD", "NY", "LON", "PRA", "LA"])
def destiny(request):
    return request.param

@pytest.fixture(params=[
    User("Pep Sanchez Sanchez", "12345678A", "09234", "666666666", "pep@sanchez.com"),
    User("Nora Castillo Pujol", "98765432Z", "93845", "678912345", "crispeta@gmail.es")
])
def user(request):
    return request.param


@pytest.fixture(params=[
    PaymentData("VISA", "Pep Sanchez Sanchez", "123456789", "1234"),
])
def payment_data(request):
    return request.param