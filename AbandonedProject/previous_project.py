from cinema_data_and_structure import *
import json
import os
import re

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
				"Available_seats": SEATS_PER_HALL,
				"Reserved_showtimes": []
			}
			data.append(default_data)
		with open(CINEMA_HALLS_PATH, "a") as default_file:
			json.dump(data, default_file, indent=4)

def get_halls_data():
    check_cinema_halls()
    with open(CINEMA_HALLS_PATH, "r") as halls_file:
        halls_data = json.load(halls_file)
    return halls_data

def save_halls_data(halls_data):
    check_cinema_halls()
    with open(CINEMA_HALLS_PATH, "w") as halls_file:
        json.dump(halls_data, halls_file, indent=4)

def check_movies():
	'''Checks if the .json file with movies data exists. If not, creates one.'''
	if os.path.isfile(MOVIES_PATH) and os.access(MOVIES_PATH, os.R_OK):
		return True
	else:
		return False

def check_movie_duration(movie_duration):
	try:
		int(movie_duration)
	except ValueError:
		print("Incorrect number, try again.")
		return False
	if int(movie_duration) > 0:
			return True
	else:
		return False

def check_movie_showtime(movie_showtime):
	pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d-(?:[01]\d|2[0-3]):[0-5]\d$"
	return bool(re.match(pattern, movie_showtime))

def check_available_halls(movie_hall, movie_showtime):
	halls_data = get_halls_data()
	return any(hall["Hall_number"] == movie_hall and movie_showtime not in hall["Reserved_showtimes"] for hall in halls_data)

def add_showtime(movie_title, new_movie_showtime):
	halls_data = get_halls_data()
	pass

class Movie:
	def __init__(self, title, duration, showtimes, hall_number):
		self.title = title
		self.duration = duration
		self.showtimes = showtimes
		self.hall_number = hall_number
		self.save_movie()
		self.save_showtime_to_hall()

	def remove_showtime(self, time):
		if time in self.showtimes:
			self.showtimes.remove(time)
			self.save_movie()
		else:
			print("No movie is reserved for that timestamp.")

	def display_details(self):
		details = {
			"Title": self.title,
			"Duration": self.duration,
			"Showtimes": self.showtimes
		}
		print(details)

	def save_showtime_to_hall(self):
		halls_data = get_halls_data()
		for hall in halls_data:
			if self.hall_number == hall["Hall_number"]:
				hall["Reserved_showtimes"].append(self.showtimes)
		save_halls_data(halls_data)

	def save_movie(self):
		file_exists = check_movies()
		if file_exists:
			with open(MOVIES_PATH, "r") as movie_file:
				movie_data = json.load(movie_file)
			data = {"Title": self.title, "Duration": self.duration, "Showtimes": self.showtimes}
			movie_data.append(data)
		else:
			movie_data = []
			data = {"Title": self.title, "Duration": self.duration, "Showtimes": self.showtimes}
			movie_data.append(data)

		with open(MOVIES_PATH, "w") as movie_file:
			json.dump(movie_data, movie_file, indent=4)

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

		halls_data = get_halls_data()
		for hall_data in halls_data:
			if hall_data["Hall_number"] == hall:
				hall_data["Status"] = "VIP Reserved"
		save_halls_data(halls_data)

class Cinema():
	def __init__(self):
		pass

check_cinema_halls()

#movie_library = Movie("Władca Pierścieni", "2 godziny", ["9:00-12:00"])
#movie_library.add_showtime("14:00-15:30")

#movie_library.display_details()

# customer = Customer("Tom", "Holland")
# customer.add_reservation("Titanic", "12:30")
# customer.add_reservation("Pulp Fiction", "14:30")
# customer.display_reservations()

# vip = VIPCustomer("Marcus", "Person")
# vip.book_private_show("Titanic", "12:30", 2)

#time_to_remove = input("Podaj czas: ")
#movie_library.remove_showtime(time_to_remove)
#movie_library.display_details()

print("Welcome to CinemaCity registration!\n")

program_running = True
while program_running:
	option = input("What do you want to do? Type the correct number please:\n1. Modify movies.\n2. Modify customers and their registrations.\n3. Modify VIP customers.\n4. Display all movies.\n5. Display all customers and registrations.\n")

	if option == "1" or option == "one":
		movie_option = input("What do you want to do?\n1. Add new movie.\n2. Add new showtime to the existing movie.\n3. Remove showtime from the existing movie.\n")

		if movie_option == "1" or movie_option == "one":
			movie_title = input("Enter title of the movie: ")

			valid_duration = False
			while valid_duration == False:
				movie_duration = input("Enter duration of the movie in minutes: ")
				valid_duration = check_movie_duration(movie_duration)

			valid_showtime = False
			while valid_showtime == False:
				movie_showtime = input("Enter starting showtime of a movie (e.g. 12:30-14:45): ")
				valid_showtime = check_movie_showtime(movie_showtime)
				if valid_showtime == False:
					print("Incorrect showtime, try again using the correct format.")

			valid_hall = False
			while valid_hall == False:
				movie_hall = int(input("Enter number of the hall: "))
				valid_hall = check_available_halls(movie_hall, movie_showtime)
				if valid_hall == False:
					print("Incorrect hall number or the showtime is already reserved. Try again.")

			new_movie = Movie(movie_title, movie_duration, movie_showtime, movie_hall)

		elif movie_option == "2" or movie_option == "two":
			movie_title = input("Enter title of the movie: ")

			new_valid_showtime = False
			while new_valid_showtime == False:
				new_movie_showtime = input("Enter starting showtime of a movie (e.g. 12:30-14:45): ")
				new_valid_showtime = check_movie_showtime(new_movie_showtime)
				if new_valid_showtime == False:
					print("Incorrect showtime, try again using the correct format.")

			add_showtime(movie_title, new_movie_showtime)