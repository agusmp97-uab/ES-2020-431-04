
class Flight:
    def __init__(self, destiny, id_flight, price):
        self.id = id_flight
        self.price = price
        self.destiny = destiny

    def get_destiny(self) -> str:
        return self.destiny

    def get_price(self) -> float:
        return self.price
