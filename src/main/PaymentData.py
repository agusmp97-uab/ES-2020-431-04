class PaymentData:

    def __init__(self, payment_type, holder_name, number, security_code):
        self.payment_type = payment_type
        self.holder_name = holder_name
        self.number = number
        self.security_code = security_code
        self.reserve_amount = 0

    def set_reserve_amount(self, amount) -> None :
        self.reserve_amount = amount
