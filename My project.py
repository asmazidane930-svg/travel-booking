# ==============================
# Class User
# ==============================
class User:
    def __init__(self, id_user, name, email, password):
        self.id_user = id_user
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.name} ({self.email})"


# ==============================
# Class Trip
# ==============================
class Trip:
    def __init__(self, id_trip, departure, destination, date, price, seats):
        self.id_trip = id_trip
        self.departure = departure
        self.destination = destination
        self.date = date
        self._price = price     # Encapsulation
        self._seats = seats     # Encapsulation

    # Getter price
    @property
    def price(self):
        return self._price

    # Getter seats
    @property
    def seats(self):
        return self._seats

    def book_seat(self):
        if self._seats > 0:
            self._seats -= 1
            return True
        return False

    def __str__(self):
        return (f"ID: {self.id_trip} | {self.departure} -> {self.destination} | "
                f"Date: {self.date} | Price: {self.price} | Seats: {self.seats}")


# ==============================
# Class Booking
# ==============================
class Booking:
    def __init__(self, id_booking, user, trip, seat_number):
        self.id_booking = id_booking
        self.user = user
        self.trip = trip
        self.seat_number = seat_number

    def __str__(self):
        return (f"Booking {self.id_booking} | {self.user.name} | "
                f"{self.trip.departure}->{self.trip.destination} | Seat: {self.seat_number}")


# ==============================
# Data Storage
# ==============================
users = []
trips = []
bookings = []


# ==============================
# Add User
# ==============================
def add_user():
    id_user = input("User ID: ")
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")

    user = User(id_user, name, email, password)
    users.append(user)

    print("✅ User added successfully")


# ==============================
# Add Trip
# ==============================
def add_trip():
    id_trip = input("Trip ID: ")
    departure = input("Departure: ")
    destination = input("Destination: ")
    date = input("Date: ")

    price = float(input("Price: "))   # ✅ تعديل
    seats = int(input("Seats: "))     # ✅ تعديل

    trip = Trip(id_trip, departure, destination, date, price, seats)
    trips.append(trip)

    print("✅ Trip added successfully")


# ==============================
# Show Trips
# ==============================
def show_trips():
    if not trips:
        print("❌ No trips available")
        return

    print("\n📍 Available Trips:")
    for trip in trips:
        print(trip)


# ==============================
# Search User
# ==============================
def find_user(user_id):
    for u in users:
        if u.id_user == user_id:
            return u
    return None


# ==============================
# Search Trip
# ==============================
def find_trip(trip_id):
    for t in trips:
        if t.id_trip == trip_id:
            return t
    return None


# ==============================
# Book Trip
# ==============================
def book_trip():
    user_id = input("Enter user ID: ")
    trip_id = input("Enter trip ID: ")
    seat = input("Seat number: ")

    user = find_user(user_id)
    trip = find_trip(trip_id)

    if not user:
        print("❌ User not found")
        return

    if not trip:
        print("❌ Trip not found")
        return

    if trip.book_seat():
        booking = Booking(len(bookings)+1, user, trip, seat)
        bookings.append(booking)
        print("✅ Booking successful")
        print(booking)
    else:
        print("❌ No seats available")


# ==============================
# Show Bookings
# ==============================
def show_bookings():
    if not bookings:
        print("❌ No bookings yet")
        return

    print("\n📖 Bookings:")
    for b in bookings:
        print(b)


# ==============================
# Main Menu
# ==============================
while True:
    print("\n===== Travel Booking System =====")
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
        print("👋 Goodbye")
        break

    else:
        print("❌ Invalid choice")
