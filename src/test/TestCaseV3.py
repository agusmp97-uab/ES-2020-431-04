from src.main.Journey import Journey
from src.main.Cars import Cars
from src.main.Hotels import Hotels
from src.main.Flight import *


class TestCaseV3:
    """ When adding a car to a journey with multiple destinies and multiple passengers, the price is as expected"""
    def test_add_car(self, cars, journey):
        expected_output = journey.get_total_price()
        for i in range(len(cars[0])):
            n_days = journey.get_n_days(cars[0][i])
            expected_output += n_days * cars[2][i]
            journey.add_car(cars[0][i], cars[1][i])

        assert journey.get_total_price() == expected_output


    """ When removing a car from a journey with multiple destinies and multiple passengers, the price is as expected"""
    def test_remove_cars(self, journey_with_cars, car):
        expected_output = journey_with_cars.get_total_price()
        n_days = journey_with_cars.get_n_days(car[0])
        expected_output -= n_days * car[2]

        journey_with_cars.remove_car(car[0], car[1].get_code())
        x = journey_with_cars.get_total_price()
        assert journey_with_cars.get_total_price() == expected_output


    """ When adding a hotel to a journey with multiple destinies and multiple passengers, the price is as expected"""
    def test_add_hotels(self, hotels, journey_with_cars):
        expected_output = journey_with_cars.get_total_price()
        n_passengers = journey_with_cars.get_n_passengers()
        for i in range(len(hotels[0])):
            n_days = journey_with_cars.get_n_days(hotels[0][i])
            expected_output += n_passengers * n_days * hotels[2][i]
            journey_with_cars.add_hotel(hotels[0][i], hotels[1][i])

        assert journey_with_cars.get_total_price() == expected_output

    """ When removing a hotel from a journey with multiple destinies and multiple passengers,
     the price is as expected"""
    def test_remove_hotels(self, journey_with_cars_and_hotels, hotel):
        expected_output = journey_with_cars_and_hotels.get_total_price()
        n_passengers = journey_with_cars_and_hotels.get_n_passengers()
        n_days = journey_with_cars_and_hotels.get_n_days(hotel[0])
        expected_output -= n_passengers * n_days * hotel[2]

        journey_with_cars_and_hotels.remove_hotel(hotel[0])
        assert journey_with_cars_and_hotels.get_total_price() == expected_output

