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
		if self.title and self.duration and self.showtimes:
			details = {
				"Title": self.title,
				"Duration": self.duration,
				"Showtimes": self.showtimes
			}
			print(details)
		else:
			print("There's currently no movie to display.")

movie_library = Movie("Władca Pierścieni", "2 godziny", ["9:00-12:00"])
movie_library.add_showtime("14:00-15:30")

movie_library.display_details()

time_to_remove = input("Podaj czas: ")
movie_library.remove_showtime(time_to_remove)
movie_library.display_details()