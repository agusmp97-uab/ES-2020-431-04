
from src.main.Flight import Flight


class Flights:
    def __init__(self, n_passengers, origin):
        self.flights = []
        self.n_passengers = n_passengers
        self.total_price = 0
        self.origin = origin

    def add_flight(self, flight) -> None:
        self.flights.append(flight)
        self.total_price += self.n_passengers * flight.get_price()

    def add_flights(self, flights):
        for flight in flights:
            self.flights.append(flight)
            self.total_price += self.n_passengers * flight.get_price()
        return self

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

    def get_n_passengers(self) -> int:
        return self.n_passengers

    def get_destinies(self) -> list:
        destinies = []
        for flight in self.flights:
            if flight.get_destiny() not in destinies and flight.get_destiny() != self.origin:
                destinies.append(flight.get_destiny())
        return destinies

    def get_flights(self) -> list:
        return self.flights


