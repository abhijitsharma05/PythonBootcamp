#base
class Flight:
    def __init__(self, flight_number, airline):
        self.flight_number = flight_number
        self.airline = airline

    def display_info(self):
        print(f"Flight Number: {self.flight_number}, Airline: {self.airline}")


class ScheduledFlight(Flight):
    def __init__(self, flight_number, airline, departure_time, arrival_time):
        super().__init__(flight_number, airline)
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def display_info(self):
        super().display_info()
        print(f"Departure: {self.departure_time}, Arrival: {self.arrival_time}")


# Base Class Person
class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.person_id}")


# Derived Class CrewMember
class CrewMember(Person):
    def __init__(self, name, person_id, role):
        super().__init__(name, person_id)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")


# Derived Class: Pilot
class Pilot(CrewMember):
    def __init__(self, name, person_id, role, license_number, rank):
        super().__init__(name, person_id, role)
        self.license_number = license_number
        self.rank = rank

    def display_info(self):
        super().display_info()
        print(f"License Number: {self.license_number}, Rank: {self.rank}")


# Base Class Service
class Service:
    def service_info(self):
        print("General airport service.")


# Derived Class SecurityService
class SecurityService(Service):
    def service_info(self):
        print("Security Service")


# Derived Class: BaggageService
class BaggageService(Service):
    def service_info(self):
        print("Baggage Service.")


# PassengerDetails Class
class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# TicketDetails Class
class TicketDetails:
    def __init__(self, ticket_number, seat_number):
        self.ticket_number = ticket_number
        self.seat_number = seat_number


# Multiple Inheritance Booking
class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticket_number, seat_number):
        PassengerDetails.__init__(self, name, age)
        TicketDetails.__init__(self, ticket_number, seat_number)

    def display_booking(self):
        print(f"Passenger: {self.name}, Age: {self.age}")
        print(f"Ticket Number: {self.ticket_number}, Seat Number: {self.seat_number}")


# Example
if __name__ == "__main__":
    # Flight and ScheduledFlight
    sf = ScheduledFlight("AI101", "Air India", "10:00 AM", "12:00 PM")
    sf.display_info()
    print()

    # Person -> CrewMember -> Pilot
    pilot = Pilot("Abhijit Sharma", "P123", "Pilot", "LIC4567", "Captain")
    pilot.display_info()
    print()

    # Services
    service1 = SecurityService()
    service2 = BaggageService()
    service1.service_info()
    service2.service_info()
    print()

    # Booking (Multiple Inheritance)
    booking = Booking("Alice", 28, "T7890", "12A")
    booking.display_booking()
