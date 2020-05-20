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
        for h in self.hotels:
            if h.get_id() == hotel.get_id():
                self.total_price -= h.get_price()
            else:
                hotels_aux.append(h)
        self.hotels = hotels_aux