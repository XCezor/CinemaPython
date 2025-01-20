## Cinema

### Classes and Functions

1. `Movie(title, duration, showtimes)` - Creates a new **Movie object** with a title, duration in minutes and showtimes.

- `add_showtime(time)` - Adds new showtime to the current **Movie object**
- `remove_showtime(time)` - Removes showtime from the current **Movie object**
- `display_details()` - Displays all movies with all details and numbers them.

2. `Customer(first_name, last_name)` - Creates new **Customer object** with the first and last names.

- `add_reservation(movie, time, private)` - Creates new reservation for the current **Customer object**. If the customer is **VIP**, the private reservation can be created instead.
- `display_reservations()` - Displays all customers and their reservations, numbering reserved movie titles.

3. `VIPCustomer(Customer)` - Creates new **VIP Customer object**, which has access to VIP discount and private reservation.

- `get_discounted_price(price)` - Takes a ticket price and adds 25% discount on it, then returns new ticket price.
- `book_private_show(movie, time)` - Allows **VIP Customer object** to book a private show using `add_reservation` from `Customer` class.

4. `Cinema()` - A class that takes **Movie objects** and **Customer/VIP Customer objects** to store them in a lists.

- `add_movie(movie)` - Adds new movie that was created using `Movie` class.
- `add_customer(customer)` - Adds new customer or VIP customer that was created using `Customer/VIP Customer` class.
- `display_movies()` and `display_customers()` - Displays all stored movies and customers.

5. Example usage of the code is inside `main.py` file under `main()` function.