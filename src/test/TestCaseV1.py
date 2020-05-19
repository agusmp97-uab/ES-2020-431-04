from src.test.conftest import *


class TestCaseV1:
    def test_passengers(self, flights_multiple_passengers):
        assert flights_multiple_passengers[0].get_n_passengers() == flights_multiple_passengers[1][0]

    def test_empty_flights_destinies(self, empty_flights):
        assert empty_flights.get_destinies() == []

    def test_empty_flights_flights(self, empty_flights):
        assert empty_flights.get_flights() == []

    def test_empty_flights_flights(self, empty_flights):
        assert empty_flights.get_price() == 0

    def test_add_flight_destinies(self, flights_1_passenger, flight):
        expected_output = []
        for f in flights_1_passenger[1][2]:
            if f.get_destiny() not in expected_output and f.get_destiny() != flights_1_passenger[1][1]:
                expected_output.append(f.get_destiny())
        if flight.get_destiny() not in expected_output and flight.get_destiny() != flights_1_passenger[1][1]:
            expected_output.append(flight.get_destiny())

        flights_1_passenger[0].add_flight(flight)
        assert flights_1_passenger[0].get_destinies() == expected_output

    def test_add_flight_flights(self, flights_1_passenger, flight):
        expected_output = flights_1_passenger[1][2]
        expected_output.append(flight)

        flights_1_passenger[0].add_flight(flight)
        assert flights_1_passenger[0].get_flights() == expected_output

    def test_add_flight_price(self, flights_1_passenger, flight):
        expected_output = flight.get_price()
        for f in flights_1_passenger[1][2]:
            expected_output += f.get_price()

        flights_1_passenger[0].add_flight(flight)
        assert flights_1_passenger[0].get_price() == expected_output

    def test_add_flight_destinies_multiple_passengers(self, flights_multiple_passengers, flight):
        expected_output = []
        for f in flights_multiple_passengers[1][2]:
            if f.get_destiny() not in expected_output and f.get_destiny() != flights_multiple_passengers[1][1]:
                expected_output.append(f.get_destiny())
        if flight.get_destiny() not in expected_output and flight.get_destiny() != flights_multiple_passengers[1][1]:
            expected_output.append(flight.get_destiny())

        flights_multiple_passengers[0].add_flight(flight)
        assert flights_multiple_passengers[0].get_destinies() == expected_output

    def test_add_flight_flights_multiple_passengers(self, flights_multiple_passengers, flight):
        expected_output = flights_multiple_passengers[1][2]
        expected_output.append(flight)

        flights_multiple_passengers[0].add_flight(flight)
        assert flights_multiple_passengers[0].get_flights() == expected_output

    def test_add_flight_price_multiple_passengers(self, flights_multiple_passengers, flight):
        expected_output = flight.get_price()
        for f in flights_multiple_passengers[1][2]: 
            expected_output += f.get_price()
        expected_output *= flights_multiple_passengers[1][0]

        flights_multiple_passengers[0].add_flight(flight)
        assert flights_multiple_passengers[0].get_price() == expected_output

    def test_remove_flight_destiny(self, flights_multiple_passengers, destiny):
        expected_output = []
        for f in flights_multiple_passengers[1][2]:
            if f.get_destiny() not in expected_output and f.get_destiny() != flights_multiple_passengers[1][1]\
                    and f.get_destiny() != destiny:
                expected_output.append(f.get_destiny())

        flights_multiple_passengers[0].remove_destiny(destiny)
        assert flights_multiple_passengers[0].get_destinies() == expected_output

    def test_remove_flight_flights(self, flights_multiple_passengers, destiny):
        expected_output = []
        for f in flights_multiple_passengers[1][2]:
            if f.get_destiny() != destiny:
                expected_output.append(f)

        flights_multiple_passengers[0].remove_destiny(destiny)
        assert flights_multiple_passengers[0].get_flights() == expected_output

    def test_remove_flight_price(self, flights_multiple_passengers, destiny):
        expected_output = 0
        for f in flights_multiple_passengers[1][2]:
            if f.get_destiny() != destiny:
                expected_output += f.get_price()*flights_multiple_passengers[1][0]

        flights_multiple_passengers[0].remove_destiny(destiny)
        assert flights_multiple_passengers[0].get_price() == expected_output



