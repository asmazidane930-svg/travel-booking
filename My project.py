# Class User
class User:
    def __init__(self, id_user, name, email, password):
        self.id_user = id_user
        self.name = name
        self.email = email
        self.password = password


# Class Trip
class Trip:
    def __init__(self, id_trip, departure, destination, date, price, seats):
        self.id_trip = id_trip
        self.departure = departure
        self.destination = destination
        self.date = date
        self.price = price
        self.seats = seats


# Class Booking
class Booking:
    def __init__(self, id_booking, user, trip, seat_number):
        self.id_booking = id_booking
        self.user = user
        self.trip = trip
        self.seat_number = seat_number


# Lists to store data
users = []
trips = []
bookings = []


# Add Trip
def add_trip():
    id_trip = input("Trip ID: ")
    departure = input("Departure: ")
    destination = input("Destination: ")
    date = input("Date: ")
    price = input("Price: ")
    seats = input("Seats: ")

    trip = Trip(id_trip, departure, destination, date, price, seats)
    trips.append(trip)
    print("Trip added successfully")


# Show Trips
def show_trips():
    for trip in trips:
        print("ID:", trip.id_trip,
              "|", trip.departure, "->", trip.destination,
              "| Date:", trip.date,
              "| Price:", trip.price)


# Add User
def add_user():
    id_user = input("User ID: ")
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")

    user = User(id_user, name, email, password)
    users.append(user)

    print("User added")


# Booking Trip
def book_trip():
    user_id = input("Enter user id: ")
    trip_id = input("Enter trip id: ")
    seat = input("Seat number: ")

    user = None
    trip = None

    for u in users:
        if u.id_user == user_id:
            user = u

    for t in trips:
        if t.id_trip == trip_id:
            trip = t

    if user and trip:
        booking = Booking(len(bookings)+1, user, trip, seat)
        bookings.append(booking)
        print("Booking successful")
    else:
        print("User or Trip not found")


# Show Bookings
def show_bookings():
    for b in bookings:
        print("Booking ID:", b.id_booking,
              "| User:", b.user.name,
              "| Trip:", b.trip.departure, "->", b.trip.destination,
              "| Seat:", b.seat_number)


# Main Menu
while True:
    print("\n--- Travel Booking System ---")
    print("1. Add User")
    print("2. Add Trip")
    print("3. Show Trips")
    print("4. Book Trip")
    print("5. Show Bookings")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_user()

    elif choice == "2":
        add_trip()

    elif choice == "3":
        show_trips()

    elif choice == "4":
        book_trip()

    elif choice == "5":
        show_bookings()

    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Invalid choice")