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
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def add_reservation(self, movie, time):
		self.movie = movie

new_movie = Movie("Titanic", "150", ["12:30-12:50", "14:00-15:50"])
new_movie.display_details()

new_movie.add_showtime("19:29-22:33")
new_movie.display_details()

new_movie.remove_showtime("12:30-12:50")
new_movie.display_details()