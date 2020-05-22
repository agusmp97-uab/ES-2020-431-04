import pytest
from src.main.Flights import Flights
from src.main.Flight import Flight
from src.main.User import User
from src.main.PaymentData import PaymentData
from src.main.Cars import Cars
from src.main.Car import Car
from src.main.Hotel import Hotel
from src.main.Hotels import Hotels
from src.main.Journey import Journey
from src.main.Bank import Bank
from src.main.Skyscanner import Skyscanner
from src.main.Booking import Booking
from src.main.Rentalcars import Rentalcars


@pytest.fixture(params=[1, 2, 3, 4, 5, 6, 7, 0, 23, 50])
def empty_journey(request):
    journey = Journey(request.param, "BCN")
    return journey


@pytest.fixture(params=[
    (1, "BCN", [1, 3, 2], [Flight("ROM", "2", 50), Flight("PAR", "21", 100), Flight("PRA", "22", 200),
                           Flight("BCN", "432", 200)]),
    (1, "BCN", [2], [Flight("ROM", "2", 50), Flight("BCN", "4", 40)]),
    (1, "BCN", [3], [Flight("ROM", "2", 50), Flight("BCN", "4", 40)]),
    (1, "ROM", [2], [Flight("PAR", "21", 100), Flight("ROM", "22", 200)]),
    (1, "BCN", [6, 7], [Flight("NY", "1", 5000), Flight("LA", "2", 400), Flight("BCN", "3", 200)]),
    (1, "BCN", [3], [Flight("MAD", "2", 50), Flight("BCN", "21", 60)]),
    (1, "BCN", [], []),
    (1, "BCN", [], []),
])
def journey_1_passenger(request):
    journey = Journey(request.param[0], request.param[1])
    n_days = request.param[2]
    flights = request.param[3]
    for i in range(len(n_days)):
        journey.add_destiny(flights[i], n_days[i])
    if len(flights) > 0:
        journey.add_return_flight(flights[-1])

    return journey, request.param


@pytest.fixture(params=[
    (2, "BCN", [1, 2, 3], [Flight("ROM", "2", 50), Flight("PAR", "21", 100), Flight("PRA", "22", 200),
                           Flight("BCN", "432", 200)]),
    (3, "BCN", [2, 3], [Flight("ROM", "2", 50), Flight("PEK", "789", 3000), Flight("BCN", "4", 40)]),
    (4, "BCN", [1, 1], [Flight("ROM", "2", 50), Flight("MAR", "3", 200), Flight("BCN", "4", 40)]),
    (2, "ROM", [5], [Flight("PAR", "21", 100), Flight("ROM", "22", 200)]),
    (2, "BCN", [4, 5], [Flight("NY", "1", 5000), Flight("LA", "2", 400), Flight("BCN", "3", 200)]),
    (3, "BCN", [2, 3], [Flight("ATH", "2", 500), Flight("BER", "3", 700), Flight("BCN", "4", 300)]),
    (5, "BCN", [2, 2], [Flight("MAD", "2", 50), Flight("SEV", "45", 30), Flight("BCN", "21", 60)]),
    (2, "BCN", [2, 4], [Flight("MAD", "2", 50), Flight("SEV", "45", 2), Flight("BCN", "21", 60)]),
])
def journey_multiple_passengers(request):
    journey = Journey(request.param[0], request.param[1])
    n_days = request.param[2]
    flights = request.param[3]
    for i in range(len(n_days)):
        journey.add_destiny(flights[i], n_days[i])
    journey.add_return_flight(flights[-1])

    return journey, request.param


@pytest.fixture(params=[
    Flight("ROM", "2", 50),
    Flight("PAR", "2", 50),
    Flight("ATH", "165", 300),
    Flight("NY", "58", 3000),
    Flight("MAD", "14", 10),
    Flight("LA", "165", 5000),
])
def flight(request):
    return request.param


@pytest.fixture(params=[2, 7])
def n_days(request):
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

@pytest.fixture()
def journey():
    flights = [Flight("ROM", "2", 50), Flight("PAR", "21", 100), Flight("PRA", "22", 200),
               Flight("BCN", "432", 200)]
    n_days = [2, 3, 4]
    journey = Journey(3, "BCN")
    for i in range(len(n_days)):
        journey.add_destiny(flights[i], n_days[i])
    journey.add_return_flight(flights[-1])
    return journey

@pytest.fixture(params=[
    (["ROM", "PAR", "PRA"], [Car("1234 ABC", "Toyota", "J. street", 120),
                             Car("6690 HKR", "Subaru", "Leicester Square", 150),
                             Car("7642 DPN", "Tesla", "Castell street", 400)], [120, 150, 400]),
    (["ROM", "PRA"], [Car("8321 SKR", "Tesla", "J. street", 400),
                             Car("9935 PAN", "Kia", "Leicester Square", 170)], [400, 170]),
    (["ROM", "PAR", "PRA"], [Car("1234 ABC", "Toyota", "J. street", 120),
                             Car("8654 FGN", "Peugeot", "Leicester Square", 200),
                             Car("1248 ARN", "Audi", "Castell street", 210)], [120, 200, 210]),
    (["PRA"], [Car("9621 XYZ", "Citroen", "J. street", 160)], [160]),
    (["PAR", "PRA"], [Car("6690 HKR", "Subaru", "J. street", 150),
                      Car("3420 BRM", "Nissan", "Leicester Square", 280)], [150, 280]),
    (["ROM", "PAR"], [Car("8902 MRR", "Mercedes-Benz", "J. street", 300),
                      Car("9935 PAN", "Kia", "Leicester Square", 170)], [300, 170]),
    (["ROM", "PAR", "PRA"], [Car("8902 MRR", "Mercedes-Benz", "J. street", 300),
                             Car("1234 ABC", "Toyota", "Leicester Square", 120),
                             Car("9621 XYZ", "Citroen", "Castell street", 160)], [300, 120, 160]),
    (["ROM", "PRA"], [Car("7642 DPN", "Ford", "J. street", 180),
                      Car("1248 ARN", "Audi", "Leicester Square", 210)], [180, 210]),
    (["ROM", "PAR"], [Car("8654 FGN", "Peugeot", "J. street", 200),
                      Car("9621 XYZ", "Citroen", "Leicester Square", 160)], [200, 160]),
    (["ROM", "PAR", "PRA"], [Car("9621 XYZ", "Citroen", "J. street", 160),
                             Car("9935 PAN", "Kia", "Leicester Square", 170),
                             Car("1234 ABC", "Toyota", "Castell street", 120)], [160, 170, 120]),
])
def cars(request):
    return request.param

@pytest.fixture()
def journey_with_cars():
    flights = [Flight("ROM", "2", 50), Flight("PAR", "21", 100), Flight("PRA", "22", 200),
               Flight("BCN", "432", 200)]
    n_days = [2, 3, 4]
    journey = Journey(3, "BCN")
    for i in range(len(n_days)):
        journey.add_destiny(flights[i], n_days[i])
    journey.add_return_flight(flights[-1])
    journey.add_car("ROM", Car("1234 ABC", "Toyota", "J. street", 120))
    journey.add_car("PAR", Car("6690 HKR", "Subaru", "Leicester Square", 150))
    journey.add_car("PRA", Car("7642 DPN", "Tesla", "Castell street", 400))
    return journey

@pytest.fixture(params=[
    ("ROM", Car("1234 ABC", "Toyota", "J. street", 120), 120),
    ("PAR", Car("6690 HKR", "Subaru", "Leicester Square", 150), 150),
    ("PRA", Car("7642 DPN", "Tesla", "Castell street", 400), 400),
])
def car(request):
    return request.param

@pytest.fixture(params=[
    (["ROM", "PAR", "PRA"], [Hotel("13314", "Grand Hotel Budapest", 4, 200), Hotel("66190", "Majestic", 4, 200),
      Hotel("76142", "Hillton", 4, 50)], [200,200,50]),
    (["ROM", "PRA"], [Hotel("83211", "Great Alex Resort", 2, 100), Hotel("99135", "Ibis", 2, 150)], [100, 150]),
    (["ROM", "PAR", "PRA"], [Hotel("99135", "Ibis", 3, 200), Hotel("66190", "Majestic", 3, 210),
      Hotel("77778", "Dubai Star", 3, 500)], [200, 210, 500]),
    (["PAR", "PRA"], [Hotel("13314", "Grand Hotel Budapest", 3, 40), Hotel("66190", "Majestic", 3, 50)], [40, 50]),
    (["ROM", "PAR", "PRA"], [Hotel("13456", "Imperial Hotel", 2, 120), Hotel("83211", "Great Alex Resort", 2, 150),
      Hotel("76142", "Hillton", 2, 180)], [120, 150, 180]),
    (["ROM"], [Hotel("99135", "Ibis", 2, 500)], [500]),
    (["ROM", "PAR", "PRA"], [Hotel("77778", "Dubai Star", 3, 210),Hotel("83211", "Great Alex Resort", 3, 210),
      Hotel("13314", "Grand Hotel Budapest", 3, 220)], [210, 210, 220]),
    (["ROM", "PAR"], [Hotel("83211", "Great Alex Resort", 6, 350), Hotel("99135", "Ibis", 6, 300)], [350, 300]),
    (["ROM", "PAR", "PRA"], [Hotel("99135", "Ibis", 1, 100), Hotel("66190", "Majestic", 1, 50),
      Hotel("77778", "Dubai Star", 1, 1000)], [100, 50, 1000]),
])
def hotels(request):
    return request.param


@pytest.fixture()
def journey_with_cars_and_hotels():
    flights = [Flight("ROM", "2", 50), Flight("PAR", "21", 100), Flight("PRA", "22", 200),
               Flight("BCN", "432", 200)]
    n_days = [2, 3, 4]
    journey = Journey(3, "BCN")
    for i in range(len(n_days)):
        journey.add_destiny(flights[i], n_days[i])
    journey.add_return_flight(flights[-1])

    journey.add_car("ROM", Car("1234 ABC", "Toyota", "J. street", 120))
    journey.add_car("PAR", Car("6690 HKR", "Subaru", "Leicester Square", 150))
    journey.add_car("PRA", Car("7642 DPN", "Tesla", "Castell street", 400))

    journey.add_hotel("ROM", Hotel("13314", "Grand Hotel Budapest", 4, 200))
    journey.add_hotel("PAR", Hotel("66190", "Majestic", 4, 200))
    journey.add_hotel("PRA", Hotel("76142", "Hillton", 4, 50))

    return journey

@pytest.fixture(params=[
    ("ROM", Hotel("13314", "Grand Hotel Budapest", 4, 200), 200),
    ("PAR", Hotel("66190", "Majestic", 4, 200), 200),
    ("PRA", Hotel("76142", "Hillton", 4, 50), 50)
])
def hotel(request):
    return request.param
