from src.main.Destiny import *

""" Class encapsulating a list of destinies"""
class Destinies:
    def __init__(self):
        self.destinies = []

    """ Add a destiny"""
    def add_destiny(self, destiny):
        self.destinies.append(destiny)

    """ Get the price of the destiny on the i index (flight + hotel + cars)"""
    def get_price(self, i):
        return self.destinies[i].get_price()

    """ Return the destiny object on the i index"""
    def get_destiny(self, i):
        return self.destinies[i]

    """ Return the flight of the destiny on the i index"""
    def get_flight(self, i):
        return self.destinies[i].get_flight()

    """ Return the cars of the destiny on the i index"""
    def get_cars(self, i):
        return self.destinies[i].get_cars()

    """ Return the hotel of the destiny on the i index"""
    def get_hotel(self, i):
        return self.destinies[i].get_hotel()

    """ Return the name of the destiny on the i index"""
    def get_name(self, i):
        return self.destinies[i].get_name()

    """ Add a hotel to the destiny on the i index"""
    def add_hotel(self, i, hotel):
        self.destinies[i].add_hotel(hotel)

    """ Add a car to the destiny on the i index"""
    def add_car(self, i, car):
        self.destinies[i].add_car(car)

    """ Remove the hotel from the destiny on the i index"""
    def remove_hotel(self, i):
        self.destinies[i].remove_hotel()

    """ Remove the car with the given code from the destiny on the i index"""
    def remove_car(self, i, code):
        self.destinies[i].remove_car(code)

    """ Return the number of destinies"""
    def get_len(self):
        return len(self.destinies)
