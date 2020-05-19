import pytest
from src.main.Flights import Flights
from src.main.Flight import Flight
from src.main.User import User
from src.main.PaymentData import PaymentData
from src.main.Journey import Journey
from src.main.Bank import Bank
from src.main.Skyscanner import Skyscanner
from src.main.Booking import Booking
from src.main.Rentalcars import Rentalcars


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
    (3, "BCN", [Flight("ROM", "2", 50), Flight("PEK", "789", 3000), Flight("BCN", "4", 40)]),
    (4, "BCN", [Flight("ROM", "2", 50), Flight("MAR", "3", 200), Flight("BCN", "4", 40)]),
    (2, "ROM", [Flight("PAR", "21", 100), Flight("ROM", "22", 200)]),
    (2, "BCN", [Flight("NY", "1", 5000), Flight("LA", "2", 400), Flight("BCN", "3", 200)]),
    (3, "BCN", [Flight("ATH", "2", 500), Flight("BER", "3", 700), Flight("BCN", "4", 300)]),
    (5, "BCN", [Flight("MAD", "2", 50), Flight("SEV", "45", 30), Flight("BCN", "21", 60)]),
    (2, "BCN", [Flight("MAD", "2", 50), Flight("SEV", "45", 2), Flight("BCN", "21", 60)]),
    (3, "LON", [Flight("PAR","1", 90), Flight("BRU", "2", 50), Flight("ROM", "4", 200), Flight("LON", "5", 500)]),
    (2, "BCN", [Flight("PAR","1", 90), Flight("BRU", "2", 50), Flight("ROM", "4", 200), Flight("BCN", "5", 500)]),
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
    ("VISA", "Pep Sanchez Sanchez", "123456789", "1234"),
])
def payment_data(request):
    payment_data = PaymentData(request.param[0], request.param[1], request.param[2], request.param[3])
    return payment_data, request.param

@pytest.fixture(params=[
    ("VISA", "Pep Sanchez Sanchez", "123456789", "1234"),
    ("MASTER_CARD", "Pep Sanchez Sanchez", "123456789", "1234"),
])
def payment_data_type(request):
    payment_data = PaymentData(request.param[0], request.param[1], request.param[2], request.param[3])
    return payment_data, request.param


@pytest.fixture(params=[
    ([Car("1234 ABC", "Toyota", "BCN", 120, 4), Car("6690 HKR", "Subaru", "ROM", 150, 4), Car("7642 DPN", "Tesla", "ATH", 400, 3)]),
    ([Car("8321 SKR", "Tesla", "ATH", 400, 3), Car("9935 PAN", "Kia", "LYN", 170, 4)])
    ([Car("1234 ABC", "Toyota", "BCN", 120, 4), Car("8654 FGN", "Peugeot", "NYC", 200, 5), Car("1248 ARN", "Audi", "LA", 210, 6)]),
    ([Car("9621 XYZ", "Citroen", "PAR", 160, 5)]),
    ([Car("6690 HKR", "Subaru", "ROM", 150, 4), Car("3420 BRM", "Nissan", "BER", 280, 6)]),
    ([Car("8902 MRR", "Mercedes-Benz", "LON", 300, 5), Car("9935 PAN", "Kia", "LYN", 170, 4)]),
    ([Car("8902 MRR", "Mercedes-Benz", "LON", 300, 5), Car("1234 ABC", "Toyota", "BCN", 120, 4), Car("9621 XYZ", "Citroen", "PAR", 160, 5)]),
    ([Car("7642 DPN", "Ford", "PRA", 180, 4), Car("1248 ARN", "Audi", "LA", 210, 6)]),
    ([Car("8654 FGN", "Peugeot", "NYC", 200, 5), Car("9621 XYZ", "Citroen", "PAR", 160, 5)]),
    ([Car("9621 XYZ", "Citroen", "PAR", 160, 5), Car("9935 PAN", "Kia", "LYN", 170, 4), Car("1234 ABC", "Toyota", "BCN", 120, 4)]),
])
def cars(request):
    cars = cars()
    cars.add_cars(request.param)
    return cars, request.param

@pytest.fixture(params=[
    Car("1234 ABC", "Toyota", "BCN", 120, 4),
    Car("3420 BRM", "Nissan", "BER", 280, 6),
    Car("9621 XYZ", "Citroen", "PAR", 160, 5),
    Car("8902 MRR", "Mercedes-Benz", "LON", 300, 5),
    Car("6690 HKR", "Subaru", "ROM", 150, 4),
    Car("7642 DPN", "Ford", "PRA", 180, 4),
    Car("8321 SKR", "Tesla", "ATH", 400, 3),
    Car("9935 PAN", "Kia", "LYN", 170, 4),
    Car("8654 FGN", "Peugeot", "NYC", 200, 5),
    Car("1248 ARN", "Audi", "LA", 210, 6),

])
def car(request):
    return request.param

@pytest.fixture(params=[

])
def hotels(request):
    pass

@pytest.fixture(params=[

])
def hotel(request):
    pass