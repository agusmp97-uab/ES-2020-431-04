
class Flight:
    def __init__(self,destiny, id_flight=None, price=0, origin=None):
        self.id = id_flight
        self.price = price
        self.destiny

    def get_destiny(self) -> str:
        return self.destiny

    def get_price(self) -> float:
        return self.price
