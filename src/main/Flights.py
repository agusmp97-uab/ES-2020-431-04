
class Flights:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        if flight.get_destiny() not in self.get_destinies_names():
            self.flights.append(flight)

    def get_destinies_names(self):
        destinies_names = []
        for flight in self.flights:
            destinies_names.append(flight.get_destiny())
        return destinies_names

    def add_flights(self, flights):
        self.flights = self.flights + flights

    def get_flights(self):
        return self.flights

    def __eq__(self, other):
        return set(self.flights) == set(other.flights)