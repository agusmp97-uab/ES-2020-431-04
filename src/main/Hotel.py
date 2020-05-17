class Hotel:
    def __init__(self, id_hotel, hotel_name, n_guests, n_rooms, n_days, price):
        self.id = id_hotel
        self.name = hotel_name
        self.n_guests = n_guests
        self.n_rooms = n_rooms
        self.n_days = n_days
        self.price = price

    def get_id(self) -> str:
        return self.id

    def get_price(self) -> float:
        return self.price * self.n_rooms * self.n_days