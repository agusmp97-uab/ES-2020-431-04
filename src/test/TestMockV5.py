from src.test.conftest import *
from src.main.Journey import Journey


class TestMockV5:

    """ When there is an error on the reserve of the cars, the reserve is retry"""
    def test_retry_reserve_cars(self, monkeypatch, journey_with_cars, user):
        def mock_return(self, user, cars):
            return False
        monkeypatch.setattr(Rentalcars, "confirm_reserve", mock_return)

        journey_with_cars.add_user(user)
        journey_with_cars.confirm_reserve_cars()
        assert journey_with_cars.get_tryings() < 2

    """ When the reserve of the cars is successful on a retry, the program reports it"""
    def test_retry_reserve_cars_success(self, journey_with_cars, user):
        Skyscanner.confirm_reserve.side_effect = [False, True]

        journey_with_cars.add_user(user)
        assert journey_with_cars.confirm_reserve_cars() is True

    """ When the maximum of retries of the reservation of the cars is reached, the program reports it"""
    def test_retry_reserve_cars_max_retries(self, monkeypatch, journey_with_cars, user):
        def mock_return(self, user, cars):
            return False
        monkeypatch.setattr(Rentalcars, "confirm_reserve", mock_return)

        journey_with_cars.add_user(user)
        assert journey_with_cars.confirm_reserve_cars() is False

    """ When there is an error on the reserve of the hotels, the reserve is retry"""
    def test_retry_reserve_hotel(self, monkeypatch, journey_with_cars_and_hotels, user):
        def mock_return(self, user, hotels):
            return False
        monkeypatch.setattr(Booking, "confirm_reserve", mock_return)

        journey_with_cars_and_hotels.add_user(user)
        journey_with_cars_and_hotels.confirm_reserve_hotels()
        assert journey_with_cars_and_hotels.get_tryings() < 2

    """ When the reserve of the hotels is successful on a retry, the program reports it"""
    def test_retry_reserve_hotels_success(self, journey_with_cars_and_hotels, user):
        Booking.confirm_reserve.side_effect = [False, True]

        journey_with_cars_and_hotels.add_user(user)
        assert journey_with_cars_and_hotels.confirm_reserve_hotels() is True

    """ When the maximum of retries of the reservation of the hotels is reached, the program reports it"""
    def test_retry_hotels_reserve_max_retries(self, monkeypatch, journey_with_cars_and_hotels, user):
        def mock_return(self, user, hotels):
            return False
        monkeypatch.setattr(Booking, "confirm_reserve", mock_return)

        journey_with_cars_and_hotels.add_user(user)
        assert journey_with_cars_and_hotels.confirm_reserve_hotels() is False
