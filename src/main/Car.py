class Car:
    def __init__(self, id_car, brand, pick_up_place, price, days_reserved):
        self.id = id_car
        self.brand = brand
        self.pick_up_place = pick_up_place
        self.price = price
        self.days_reserved = days_reserved

    def get_id(self) -> str:
        return self.id

    def get_price(self) -> float:
        total_price = self.price*self.days_reserved
        return total_price
