from src.test.conftest import *
from src.main.Journey import Journey


class TestMockV5:

    def test_correct_billing_user(self,  journey_with_cars, billing_user):
        assert journey_with_cars.add_billing_user(billing_user) is True

    def test_incorrect_billing_user(self, journey_with_cars, incorrect_billing_user):
        assert journey_with_cars.add_billing_user(incorrect_billing_user) is False

    def test_complete_billing_data(self, journey_with_cars, billing_user):
        journey_with_cars.add_billing_user(billing_user)

        assert journey_with_cars.get_billing_user() == billing_user

    def test_retry_reserve_cars_success(self, journey_with_cars, user):
        Skyscanner.confirm_reserve.side_effect = [False, True]

        journey_with_cars.add_user(user)
        assert journey_with_cars.confirm_reserve_cars() is True

    def test_retry_reserve_cars_max_retries(self, monkeypatch, journey_with_cars, user):
        def mock_return(self, user, cars):
            return False
        monkeypatch.setattr(Rentalcars, "confirm_reserve", mock_return)

        journey_with_cars.add_user(user)
        assert journey_with_cars.confirm_reserve_cars() is False

    def test_retry_reserve_hotel(self, monkeypatch, journey_with_cars_and_hotels, user):
        def mock_return(self, user, hotels):
            return False
        monkeypatch.setattr(Booking, "confirm_reserve", mock_return)

        journey_with_cars_and_hotels.add_user(user)
        journey_with_cars_and_hotels.confirm_reserve_hotels()
        assert journey_with_cars_and_hotels.get_tryings() < 2

    def test_retry_reserve_hotels_success(self, journey_with_cars_and_hotels, user):
        Booking.confirm_reserve.side_effect = [False, True]

        journey_with_cars_and_hotels.add_user(user)
        assert journey_with_cars_and_hotels.confirm_reserve_hotels() is True

    def test_retry_hotels_reserve_max_retries(self, monkeypatch, journey_with_cars_and_hotels, user):
        def mock_return(self, user, hotels):
            return False
        monkeypatch.setattr(Booking, "confirm_reserve", mock_return)

        journey_with_cars_and_hotels.add_user(user)
        assert journey_with_cars_and_hotels.confirm_reserve_hotels() is False
