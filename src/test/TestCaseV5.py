from src.test.conftest import *
from src.main.Journey import Journey


class TestCaseV5:
    """ If the billing data is correct, the program reports it """
    def test_correct_billing_user(self,  journey_with_cars, billing_user):
        assert journey_with_cars.add_billing_user(billing_user) is True

    """ If the billing data is not correct, the program reports it """
    def test_incorrect_billing_user(self, journey_with_cars, incorrect_billing_user):
        assert journey_with_cars.add_billing_user(incorrect_billing_user) is False

    """ When the user introduces the billing data, the billing data of the journey is as expected"""
    def test_complete_billing_data(self, journey_with_cars, billing_user):
        journey_with_cars.add_billing_user(billing_user)

        assert journey_with_cars.get_billing_user() == billing_user