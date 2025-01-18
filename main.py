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
		display = {
			"First name": self.first_name,
			"Last name": self.last_name,
			"Movie": self.movie,
			"Time": self.time
		}
		print(display)

movie_library = Movie("Władca Pierścieni", "2 godziny", ["9:00-12:00"])
movie_library.add_showtime("14:00-15:30")

movie_library.display_details()

customer = Customer("Tom", "Holland")
customer.add_reservation("Titanic", "12:30")
customer.display_reservations()

time_to_remove = input("Podaj czas: ")
movie_library.remove_showtime(time_to_remove)
movie_library.display_details()