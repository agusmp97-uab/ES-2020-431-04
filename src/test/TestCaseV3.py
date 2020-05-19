from src.main.Journey import Journey

class TestCaseV3:
    def test_add_cars_multiple_passengers(self, flights_multiple_passengers, user, payment_data, cars, car):
        expected_output = cars
        expected_output.append(car)
        journey = Journey(flights_multiple_passengers[0], user, None, None, cars[0])
        journey.cars.add_car(car)

        assert journey.cars.get_cars() == expected_output

    """
    def test_add_flight_flights_multiple_passengers(self, flights_multiple_passengers, flight):
    expected_output = flights_multiple_passengers[1][2]
    expected_output.append(flight)
    
    flights_multiple_passengers[0].add_flight(flight)
    assert flights_multiple_passengers[0].get_flights() == expected_output
    """