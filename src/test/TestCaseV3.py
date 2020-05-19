from src.main.Journey import Journey

class TestCaseV3:
    def test_add_cars_multiple_passengers(self, flights_multiple_passengers, user, payment_data, cars, car):
        expected_output = cars[0]
        expected_output.cars.append(car)
        journey = Journey(flights_multiple_passengers[0], user, None, None, cars[0])
        journey.cars.add_car(car)

        assert journey.cars.get_cars() == expected_output.cars