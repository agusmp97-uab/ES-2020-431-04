from src.test.conftest import *
from src.main.Journey import Journey


class TestMockV5:

    def test_retry_reserve_cars(self, monkeypatch, journey_with_cars, user):
        def mock_return(self, user, cars):
            return False

        monkeypatch.setattr(Rentalcars, "confirm_reserve", mock_return)
        journey_with_cars.confirm_reserve_cars()
        assert journey_with_cars.get_tryings() < 2   # default nombre intents 3 si ha de fet reintent llavors 3-2 = 1

    def test_retry_reserve_cars_success(self, journey_with_cars, user):
        Skyscanner.confirm_reserve.side_effect = [False, True]

        assert journey_with_cars.confirm_reserve_cars() is True

    def test_retry_reserve_cars_max_retries(self, monkeypatch, journey_with_cars, user):
        def mock_return(self, user, aux):
            return False

        monkeypatch.setattr(Rentalcars, "confirm_reserve", mock_return)
        assert journey_with_cars.confirm_reserve_cars() is False


    def test_retry_reserve_hotel(self, monkeypatch, journey_with_cars_and_hotels, user, hotels):
        def mock_return(self, user, hotels):
            return False

        monkeypatch.setattr(Booking, "confirm_reserve", mock_return)

        journey_with_cars_and_hotels.confirm_reserve_hotels()
        assert journey_with_cars_and_hotels.get_tryings() < 2  # default nombre intents 3 si ha de fet reintent llavors 3-2 = 1

    def test_retry_reserve_hotels_success(self, journey_with_cars_and_hotels, user):
        Booking.confirm_reserve.side_effect = [False, True]

        assert journey_with_cars_and_hotels.confirm_reserve_hotels() is True


    def test_retry_hotels_reserve_max_retries(self, monkeypatch, journey_with_cars_and_hotels, user, hotels):
        def mock_return(self, user, hotels):
            return False

        monkeypatch.setattr(Booking, "confirm_reserve", mock_return)
        assert journey_with_cars_and_hotels.confirm_reserve_hotels() is False
