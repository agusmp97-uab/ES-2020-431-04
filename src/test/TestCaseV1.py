from src.test.conftest import *


class TestCaseV1:
    def test_passengers(self, journey_multiple_passengers):

        assert journey_multiple_passengers[0].get_n_passengers() == journey_multiple_passengers[1][0]

    def test_empty_flights_destinies(self, empty_journey):
        assert empty_journey.get_destinies_names() == []

    def test_empty_flights_flights(self, empty_journey):
        assert empty_journey.get_flights().flights == Flights().flights

    def test_empty_flights_price(self, empty_journey):
        assert empty_journey.get_total_price() == 0

    def test_add_flight_destinies(self, journey_1_passenger, flight, n_days):
        expected_output = []
        for f in journey_1_passenger[1][3]:
            if f.get_destiny() not in expected_output and f.get_destiny() != journey_1_passenger[1][1]:
                expected_output.append(f.get_destiny())
        if flight.get_destiny() not in expected_output and flight.get_destiny() != journey_1_passenger[1][1]:
            expected_output.append(flight.get_destiny())

        journey_1_passenger[0].add_destiny(flight, n_days)
        assert journey_1_passenger[0].get_destinies_names() == expected_output

    def test_add_flight_flights(self, journey_1_passenger, flight, n_days):
        flights = journey_1_passenger[1][3]
        expected_output = Flights()
        expected_output.add_flights(flights)
        expected_output.add_flight(flight)

        journey_1_passenger[0].add_destiny(flight, n_days)
        assert journey_1_passenger[0].get_flights() == expected_output

    def test_add_flight_price(self, journey_1_passenger, flight, n_days):
        expected_output = 0
        for f in journey_1_passenger[1][3]:
            expected_output += f.get_price()
        if flight.get_destiny() not in [journey_1_passenger[1][3][i].get_destiny()
                                        for i in range(len(journey_1_passenger[1][3]))]:
            expected_output += flight.get_price()

        journey_1_passenger[0].add_destiny(flight, n_days)
        assert journey_1_passenger[0].get_total_price() == expected_output

    def test_add_flight_destinies_multiple_passengers(self, journey_multiple_passengers, flight, n_days):
        expected_output = []
        for f in journey_multiple_passengers[1][3]:
            if f.get_destiny() not in expected_output and f.get_destiny() != journey_multiple_passengers[1][1]:
                expected_output.append(f.get_destiny())
        if flight.get_destiny() not in expected_output and flight.get_destiny() != journey_multiple_passengers[1][1]:
            expected_output.append(flight.get_destiny())

        journey_multiple_passengers[0].add_destiny(flight, n_days)
        assert journey_multiple_passengers[0].get_destinies_names() == expected_output

    def test_add_flight_flights_multiple_passengers(self, journey_multiple_passengers, flight, n_days):
        flights = journey_multiple_passengers[1][3]
        expected_output = Flights()
        expected_output.add_flights(flights)
        expected_output.add_flight(flight)

        journey_multiple_passengers[0].add_destiny(flight, n_days)
        assert journey_multiple_passengers[0].get_flights() == expected_output

    def test_add_flight_price_multiple_passengers(self, journey_multiple_passengers, flight):
        expected_output = 0
        for f in journey_multiple_passengers[1][3]:
            expected_output += f.get_price()*journey_multiple_passengers[1][0]
        if flight.get_destiny() not in [journey_multiple_passengers[1][3][i].get_destiny()
                                        for i in range(len(journey_multiple_passengers[1][3]))]:
            expected_output += flight.get_price()*journey_multiple_passengers[1][0]

        journey_multiple_passengers[0].add_destiny(flight, n_days)
        assert journey_multiple_passengers[0].get_total_price() == expected_output

    def test_remove_destiny_destiny(self, journey_multiple_passengers, destiny):
        expected_output = []
        for f in journey_multiple_passengers[1][3]:
            if f.get_destiny() not in expected_output and f.get_destiny() != journey_multiple_passengers[1][1]\
                    and f.get_destiny() != destiny:
                expected_output.append(f.get_destiny())

        journey_multiple_passengers[0].remove_destiny(destiny)
        assert journey_multiple_passengers[0].get_destinies_names() == expected_output

    def test_remove_destiny_flights(self, journey_multiple_passengers, destiny):
        expected_output = Flights()
        for f in journey_multiple_passengers[1][3][0:-1]:
            if f.get_destiny() != destiny:
                expected_output.add_flight(f)
        expected_output.add_flight(journey_multiple_passengers[1][3][-1])

        journey_multiple_passengers[0].remove_destiny(destiny)
        assert journey_multiple_passengers[0].get_flights() == expected_output

    def test_remove_destiny_price(self, journey_multiple_passengers, destiny):
        expected_output = 0
        for f in journey_multiple_passengers[1][3][0:-1]:
            if f.get_destiny() != destiny:
                expected_output += f.get_price()*journey_multiple_passengers[1][0]
        expected_output += journey_multiple_passengers[1][3][-1].get_price() * journey_multiple_passengers[1][0]

        journey_multiple_passengers[0].remove_destiny(destiny)
        assert journey_multiple_passengers[0].get_total_price() == expected_output



