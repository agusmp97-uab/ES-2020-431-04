class Hotel:
    def __init__(self, id_hotel, hotel_name, n_rooms, price):
        self.id = id_hotel
        self.name = hotel_name
        self.n_guests = 0
        self.n_rooms = n_rooms
        self.n_days = 0
        self.price = price

    def set_n_days(self, n_days):
        self.n_days = n_days

    def set_n_guests(self, n_guests):
        self.n_guests = n_guests

    def get_id(self) -> str:
        return self.id

    def get_price(self) -> float:
        return self.price * self.n_guests * self.n_days
