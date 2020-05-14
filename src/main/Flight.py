
class Flight:
    def __init__(self, id_flight, price, origin, destiny):
        self.id = id_flight
        self.price = price
        self.destiny

    def get_destiny(self) -> str:
        return self.destiny

    def get_price(self) -> float:
        return self.price
