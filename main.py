from cinema_data_and_structure import *
import json
import os

def check_cinema_halls():
	'''Checks if the .json file with cinema halls data exists. If not, creates one with the correct formatting.'''
	if os.path.isfile(CINEMA_HALLS_PATH) and os.access(CINEMA_HALLS_PATH, os.R_OK):
		return True
	else:
		data = []
		for hall_number in TOTAL_AVAILABLE_HALLS:
			default_data = {
				"Hall_number": hall_number,
				"Status": "Free",
				"Available_seats": SEATS_PER_HALL
			}
			data.append(default_data)
		with open(CINEMA_HALLS_PATH, "a") as default_file:
			json.dump(data, default_file, indent=4)

class Movie:
	def __init__(self, title, duration, showtimes=None):
		self.title = title
		self.duration = duration
		self.showtimes = showtimes if showtimes else []

	def add_showtime(self, time):
		if time not in self.showtimes:
			self.showtimes.append(time)
		else:
			print("Requested showtime is currently occupied.")

	def remove_showtime(self, time):
		if time in self.showtimes:
			self.showtimes.remove(time)
		else:
			print("No movie is reserved for that timestamp.")

	def display_details(self):
		details = {
			"Title": self.title,
			"Duration": self.duration,
			"Showtimes": self.showtimes
		}
		print(details)

class Customer:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.movie = []
		self.time = []

	def add_reservation(self, movie, time):
		self.movie.append(movie)
		self.time.append(time)

	def display_reservations(self):
		reservations = {
			"First name": self.first_name,
			"Last name": self.last_name,
			"Movies": self.movie,
			"Times": self.time
		}
		print(reservations)

class VIPCustomer(Customer):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.discount_access = True
		self.private_show_access = True

	def get_discounted_price(self, price):
		price = price * VIP_DISCOUNT
		print(f"Greetings sir, your ticket price, including Your VIP discount, is {price}$")
		return price

	def book_private_show(self, movie, time, hall):
		self.movie = movie
		self.time = time
		self.hall = hall


check_cinema_halls()

movie_library = Movie("Władca Pierścieni", "2 godziny", ["9:00-12:00"])
movie_library.add_showtime("14:00-15:30")

movie_library.display_details()

customer = Customer("Tom", "Holland")
customer.add_reservation("Titanic", "12:30")
customer.add_reservation("Pulp Fiction", "14:30")
customer.display_reservations()

#time_to_remove = input("Podaj czas: ")
#movie_library.remove_showtime(time_to_remove)
#movie_library.display_details()

print("Welcome to CinemaCity registration!\n")
option = input("What do you want to do? Type the correct number please:\n1. Modify movies.\n2. Modify customers and their registrations.\n3. Modify VIP customers.\n4. Display all movies.\n5. Display all customers and registrations.")