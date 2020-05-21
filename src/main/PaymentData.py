from . import Flights
from . import Hotels
from . import Cars


class PaymentData:

    def __init__(self, payment_type, holder_name, number, security_code):
        self.payment_type = payment_type
        self.holder_name = holder_name
        self.number = number
        self.security_code = security_code
        self.reserve_amount = 0

    def set_reserve_amount(self, reserve_amount) -> None:
        self.reserve_amount = reserve_amount

    def get_payment_type(self):
        return self.payment_type

