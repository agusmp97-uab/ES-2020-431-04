
from . import Flight


class Flights:
    def __init__(self, n_passenger):
        self.flights = []
        self.n_passenger = n_passenger
        self.total_price = 0

    def add_flight(self, flight) -> None:
        self.flights.append(flight)
        self.total_price += self.n_passenger * flight.get_price()

    def remove_destiny(self, destiny) -> None:
        flights_aux = []
        for flight in self.flights:
            if flight.get_destiny() != destiny:
                flights_aux.append(flight)
            else:
                self.total_price -= flight.get_price()
        self.flights = flights_aux

    def get_price(self) -> float:
        return self.total_price




