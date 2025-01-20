import os
import re

class Movie:
	def __init__(self, title:str, duration:str, showtimes:list):
		self.title = title

		if not self.validate_duration(duration):
			raise ValueError("Duration should be a number larger than 0.")
		self.duration = duration

		for showtime in showtimes:
			if not self.validate_showtime(showtime):
				raise ValueError("Showtime must be in correct range: 00:00-23:59.")
		self.showtimes = showtimes

	@staticmethod
	def validate_duration(duration):
		try:
			int(duration)
		except:
			raise TypeError("Duration should be an integer.")

		return int(duration) > 0

	@staticmethod
	def validate_showtime(showtime):
		pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d-(?:[01]\d|2[0-3]):[0-5]\d$"
		return bool(re.match(pattern, showtime))

	def add_showtime(self, time:str):
		if not self.validate_showtime(time):
			raise ValueError("Showtime must be in correct range: 00-00 to 23-59.")

		if time in self.showtimes:
			print("Requested showtime already exists for that movie. It will be skipped.")
			return False

		self.showtimes.append(time)

	def remove_showtime(self, time:str):
		if time in self.showtimes:
			self.showtimes.remove(time)
		print("Showtime removed successfully, if there was any.")

	def display_details(self):
		print(f"Title: {self.title}\nDuration: {self.duration} minutes\nShowtimes: {self.showtimes}\n")

class Customer:
	def __init__(self, first_name: str, last_name: str):
		self.first_name = first_name
		self.last_name = last_name
		self.reservations = {"Movies": [], "Showtimes": [], "Private": []}

	def add_reservation(self, movie: str, time: int, private: bool):
		if not self.validate_time(time):
			raise ValueError("Incorrect number.")
		self.reservations["Movies"].append(movie)
		self.reservations["Showtimes"].append(time)
		self.reservations["Private"].append(private)

	@staticmethod
	def validate_time(time):
		if time in range(00, 23):
			return True
		else:
			return False

	def display_reservations(self):
		print(f"First name: {self.first_name}\nLast name: {self.last_name}")
		movie_number = 1
		for movie, showtime, private in zip(self.reservations["Movies"], self.reservations["Showtimes"], self.reservations["Private"]):
			print(f"Movie {movie_number}: {movie}, showtime: {showtime}, private: {private}")
			movie_number += 1
		print("")

class VIPCustomer(Customer):
	def __init__(self, first_name: str, last_name: str):
		super().__init__(first_name, last_name)

	def get_discounted_price(self, price: int) -> float:
		vip_discount = price * 0.75
		print(f"Greetings sir, your ticket price, including Your VIP discount, is {vip_discount}$")
		return vip_discount

	def book_private_show(self, movie: str, time: int):
		self.movie = movie
		if not super().validate_time(time):
			raise ValueError("Incorrect number.")
		super().add_reservation(movie, time, True)

class Cinema:
	def __init__(self):
		self.movies = []
		self.customers = []

	def add_movie(self, movie: str):
		self.movies.append(movie)

	def add_customer(self, customer: str):
		self.customers.append(customer)

	def display_movies(self):
		movie_number = 1
		for movie in self.movies:
			print(f"Movie {movie_number}: {movie}")
			movie_number += 1

def main():
	new_movie = Movie("Titanic", "150", ["12:30-12:50", "14:00-15:50"])
	new_movie.display_details()

	new_movie.add_showtime("19:29-22:33")
	new_movie.display_details()

	new_movie.remove_showtime("12:30-12:50")
	new_movie.display_details()

	new_customer = Customer("Tom", "Cruise")
	new_customer.add_reservation("Titanic", 20, False)
	new_customer.add_reservation("Them", 15, False)
	new_customer.display_reservations()

	vip_customer = VIPCustomer("Tom", "Holland")
	vip_customer.book_private_show("Jones", 12)
	vip_customer.get_discounted_price(20)
	vip_customer.display_reservations()

	cinema = Cinema()
	cinema.add_movie("Titanic")
	cinema.display_movies()

if __name__ == "__main__":
    main()