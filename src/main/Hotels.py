class Hotels:

    def __init__(self):
        self.hotels = []
        self.total_price = 0

    def get_price(self):
        return self.total_price

    def add_hotel(self, hotel) -> None:
        self.hotels.append(hotel)
        self.total_price += hotel.get_price()

    def add_hotels(self, hotels):
        for hotel in hotels:
            self.hotels.append(hotel)
            self.total_price += hotel.get_price()
        return self

    def remove_hotel(self, hotel) -> None:
        hotels_aux = []
        for hotel in self.hotels:
            if hotel.get_id() == hotel.get_id():
                self.total_price -= hotel.get_price()
            else:
                hotels_aux.append(hotel)
        self.hotels = hotels_aux