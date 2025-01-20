import re

class Movie:
	def __init__(self, title:str, duration:str, showtimes:list):
		'''Creates a movie with a title, duration and showtimes.'''
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
		'''Checks if the duration is a positive integer.'''
		try:
			int(duration)
		except:
			raise TypeError("Duration should be an integer.")

		return int(duration) > 0

	@staticmethod
	def validate_showtime(showtime):
		'''Checks if the showtime is in the correct format.'''
		pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d-(?:[01]\d|2[0-3]):[0-5]\d$"
		return bool(re.match(pattern, showtime))

	def add_showtime(self, time:str):
		'''Adds a showtime to the movie.'''
		if not self.validate_showtime(time):
			raise ValueError("Showtime must be in correct range: 00-00 to 23-59.")

		if time in self.showtimes:
			print("Requested showtime already exists for that movie. It will be skipped.")
			return False

		self.showtimes.append(time)

	def remove_showtime(self, time:str):
		'''Removes a showtime from the movie.'''
		if time in self.showtimes:
			self.showtimes.remove(time)
		print("Showtime removed successfully, if there was any.")

	def display_details(self):
		'''Shows all details of the movie.'''
		print(f"Title: {self.title}\nDuration: {self.duration} minutes\nShowtimes: {self.showtimes}\n")

class Customer:
	def __init__(self, first_name: str, last_name: str):
		'''Creates a customer with a first and last name and an empty list of reservations.'''
		self.first_name = first_name
		self.last_name = last_name
		self.reservations = {"Movies": [], "Showtimes": [], "Private": []}

	def add_reservation(self, movie: str, time: int, private: bool):
		'''Adds a reservation to the customer's list.'''
		if not self.validate_time(time):
			raise ValueError("Incorrect number.")
		self.reservations["Movies"].append(movie)
		self.reservations["Showtimes"].append(time)
		self.reservations["Private"].append(private)

	@staticmethod
	def validate_time(time):
		'''Checks if the time is correct.'''
		if time in range(00, 23):
			return True
		else:
			return False

	def display_reservations(self):
		'''Shows all reservations of the customer, numbered.'''
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
		'''Returns the price of the ticket with a VIP discount.'''
		vip_discount = price * 0.75
		print(f"Greetings sir, your ticket price, including Your VIP discount, is {vip_discount}$")
		return vip_discount

	def book_private_show(self, movie: str, time: int):
		'''Adds a private show to the VIP customer's reservations.'''
		self.movie = movie
		if not super().validate_time(time):
			raise ValueError("Incorrect number.")
		super().add_reservation(movie, time, True)

class Cinema:
	def __init__(self):
		'''Creates empty lists for movies and customers.'''
		self.movies = []
		self.customers = []

	def add_movie(self, movie: str):
		self.movies.append(movie)

	def add_customer(self, customer: str):
		self.customers.append(customer)

	def display_movies(self):
		'''Shows all movies in the cinema, numbered.'''
		for movie in self.movies:
			movie.display_details()

	def display_customers(self):
		'''Shows all customers in the cinema, numbered.'''
		for customer in self.customers:
			customer.display_reservations()

def main():
    # Creation of a new movie with 2 showtimes
	new_movie = Movie("Titanic", "150", ["12:30-12:50", "14:00-15:50"])
	new_movie.display_details()

	# Adding a new showtime to the movie
	new_movie.add_showtime("19:29-22:33")
	new_movie.display_details()

	# Removing a showtime from the movie
	new_movie.remove_showtime("12:30-12:50")
	new_movie.display_details()

	new_movie_2 = Movie("Them", "120", ["10:30-12:30", "16:00-18:50"])

	# Creating a new customer with 2 reservations
	new_customer = Customer("Tom", "Cruise")
	new_customer.add_reservation("Titanic", 20, False)
	new_customer.add_reservation("Them", 15, False)
	new_customer.display_reservations()

	# Creating a new VIP customer with a private show reservation
	vip_customer = VIPCustomer("Tom", "Holland")
	vip_customer.book_private_show("Jones", 12)
	vip_customer.get_discounted_price(20)
	vip_customer.display_reservations()

	# Creating a cinema and adding movies and customers to it, then displaying them
	cinema = Cinema()
	cinema.add_movie(new_movie)
	cinema.add_movie(new_movie_2)
	cinema.display_movies()
	cinema.add_customer(new_customer)
	cinema.add_customer(vip_customer)
	cinema.display_customers()

if __name__ == "__main__":
    main()