class Car:
    def __init__(self, code, brand, pick_up_place, price, days_reserved):
        self.code = code
        self.brand = brand
        self.pick_up_place = pick_up_place
        self.price = price
        self.days_reserved = days_reserved

    def get_price(self) -> float:
        total_price = self.price*self.days_reserved
        return total_price

    def get_code(self) -> str:
        return self.code
