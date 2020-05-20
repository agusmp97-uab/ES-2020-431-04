from src.main.Journey import Journey
from src.main.Cars import Cars
from src.main.Hotels import Hotels

class TestCaseV3:

    def test_add_cars(self, cars, car):
        expected_output = car.get_price()

        for c in cars[1]:
            expected_output += c.get_price()

        cars[0].add_car(car)
        assert cars[0].get_price() == expected_output


    def test_remove_cars(self, cars, car):
        expected_output = 0
        for c in cars[1]:
            if c.get_id() != car.get_id():
                expected_output += c.get_price()

        cars[0].remove_car(car)
        assert cars[0].get_price() == expected_output


    def test_add_hotels(self, hotels, hotel):
        expected_output = hotel.get_price()

        for h in hotels[1]:
            expected_output += h.get_price()

        hotels[0].add_hotel(hotel)
        assert hotels[0].get_price() == expected_output

    def test_remove_hotels(self, hotels, hotel):
        expected_output = 0

        for h in hotels[1]:
            if h.get_id() != hotel.get_id():
                expected_output += h.get_price()

        hotels[0].remove_hotel(hotel)
        assert hotels[0].get_price() == expected_output