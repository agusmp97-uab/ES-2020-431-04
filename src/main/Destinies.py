from src.main.Destiny import *


class Destinies:
    def __init__(self):
        self.destinies = []

    def add_destiny(self, destiny):
        self.destinies.append(destiny)

    def get_price(self, i):
        return self.destinies[i].get_price()

    def get_destiny(self, i):
        return self.destinies[i]

    def get_flight(self, i):
        return self.destinies[i].get_flight()

    def get_cars(self, i):
        return self.destinies[i].get_cars()

    def get_hotel(self, i):
        return self.destinies[i].get_hotel()

    def get_name(self, i):
        return self.destinies[i].get_name()

    def add_hotel(self, i, hotel):
        self.destinies[i].add_hotel(hotel)

    def add_car(self, i, car):
        self.destinies[i].add_car(car)

    def remove_hotel(self, i):
        self.destinies[i].remove_hotel()

    def remove_car(self, i, code):
        self.destinies[i].remove_car(code)

    def get_len(self):
        return len(self.destinies)
