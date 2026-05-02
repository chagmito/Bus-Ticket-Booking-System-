class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus


class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []

    def add_bus(self, number, route, seats):
        bus = Bus(number, route, seats)
        self.buses.append(bus)
        print("Bus Added Successfully")

    def show_buses(self):
        if not self.buses:
            print("No buses available")
            return
        print("\n Available Buses:")
        for bus in self.buses:
            print("------------------------")
            print(f"Bus No : {bus.number}")
            print(f"Route : {bus.route}")
            print(f"Available Seats : {bus.available_seats()}")

    def book_ticket(self, bus_number, name, phone):
        for bus in self.buses:
            if bus.number == bus_number:
                if bus.book_seat():
                    passenger = Passenger(name, phone, bus)
                    self.passengers.append(passenger)
                    print(" Ticket Booked Successfully")
                    print("Fare : TK 500")
                    return
                else:
                    print(" No Seats Available")
                    return

        print(" Bus Not Found")


class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"

    def login(self, username, password):
        return username == self.username and password == self.password

#Object
system = BusSystem()
admin = Admin()

while True:
    print('\n........ Bus Ticket System ............')
    print('1. Admin Login')
    print('2. Book Ticket')
    print('3. View Buses')
    print('4. Exit')

    choice = input('Enter Your Choice: ')

    if choice == '1':
        username = input('Username: ')
        password = input('Password: ')

        if admin.login(username, password):
            print('Login Successful!')

            while True:
                print('\n........ Admin Menu .........')
                print('1. Add Bus')
                print('2. View All Buses')
                print('3. Logout')

                admin_choice = input('Enter Your Choice: ')

                if admin_choice == '1':
                    number = input('Bus Number: ')
                    route = input('Route: ')

                    try:
                        seats = int(input('Total Seats: '))
                        system.add_bus(number, route, seats)
                    except ValueError:
                        print("Invalid seat number")

                elif admin_choice == '2':
                    system.show_buses()

                elif admin_choice == '3':
                    print('Logged Out!')
                    break

                else:
                    print('Invalid Choice')

        else:
            print('Invalid Username or Password')

    elif choice == '2':
        bus_number = input('Enter Bus Number: ')
        name = input('Enter Name: ')
        phone = input('Enter Phone No: ')

        system.book_ticket(bus_number, name, phone)

    elif choice == '3':
        system.show_buses()

    elif choice == '4':
        print('Thank You!')
        break

    else:
        print('Invalid Choice! Try Again.')
