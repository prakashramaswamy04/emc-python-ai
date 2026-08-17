# ============================================
# ADMIN.PY - Admin Functions
# ============================================
# Functions for admin to:
# - View all buses
# - Add new bus
# - Edit bus details
# - Remove bus
# - View all bookings
# ============================================

import data
import bus
from utils import print_header, get_bus_by_id
from validation import (
    validate_menu_choice,
    validate_date_format,
    validate_price,
    validate_bus_name,
    validate_location,
    validate_bus_id,
)


def admin_login():
    """
    Admin login authentication.
    Asks for username and password.
    """
    print_header("🔐 ADMIN LOGIN")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Check credentials
    if username == data.admin_credentials["username"] and password == data.admin_credentials["password"]:
        print("\n✅ Login successful! Welcome Admin.\n")
        show_admin_menu()
    else:
        print("\n❌ Invalid username or password. Login failed.\n")


def show_admin_menu():
    """
    Admin main menu.
    Displays options for bus and booking management.
    """
    while True:
        print_header("🔧 ADMIN PANEL")
        print("\nChoose an option:\n")
        print("1. 👀 View All Buses")
        print("2. ➕ Add New Bus")
        print("3. ✏️  Edit Bus")
        print("4. 🗑️  Remove Bus")
        print("5. 📋 View All Bookings")
        print("6. 🚪 Logout")
        print()

        choice = input("Enter your choice (1-6): ").strip()
        choice_num = validate_menu_choice(choice, 6)

        if choice_num is None:
            print()
            continue

        if choice_num == 1:
            view_all_buses()
        elif choice_num == 2:
            add_bus()
        elif choice_num == 3:
            edit_bus()
        elif choice_num == 4:
            remove_bus()
        elif choice_num == 5:
            view_all_bookings_admin()
        elif choice_num == 6:
            print("✅ Logging out...\n")
            break

        print()


def view_all_buses():
    """Display all buses in the system."""
    print_header("👀 ALL BUSES")
    if not data.buses:
        print("No buses available.")
        return

    bus.display_bus_list(data.buses, "ALL BUSES")


def add_bus():
    """
    Add a new bus to the system.
    Admin enters all required bus information.
    """
    print_header("➕ ADD NEW BUS")

    while True:
        bus_id_input = input("Enter Bus ID: ").strip()
        if not bus_id_input:
            print("❌ Bus ID cannot be empty.")
            continue
        try:
            bus_id = int(bus_id_input)
        except ValueError:
            print("❌ Invalid Bus ID. Please enter a number.")
            continue

        if bus_id <= 0:
            print("❌ Bus ID must be greater than 0.")
            continue

        if bus_id in data.buses:
            print("❌ Bus ID already exists. Please choose another ID.")
            continue
        break

    while True:
        bus_name = input("Bus Name: ").strip()
        if validate_bus_name(bus_name):
            break
        print("❌ Bus name cannot be empty.")

    while True:
        source = input("Source City: ").strip()
        if validate_location(source):
            break
        print("❌ Source city cannot be empty.")

    while True:
        destination = input("Destination City: ").strip()
        if validate_location(destination):
            break
        print("❌ Destination city cannot be empty.")

    while True:
        travel_date = input("Travel Date (YYYY-MM-DD): ").strip()
        if validate_date_format(travel_date):
            break
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

    while True:
        departure = input("Departure Time (HH:MM): ").strip()
        if departure:
            break
        print("❌ Departure time cannot be empty.")

    while True:
        arrival = input("Arrival Time (HH:MM): ").strip()
        if arrival:
            break
        print("❌ Arrival time cannot be empty.")

    while True:
        total_seats_input = input("Total Seats: ").strip()
        try:
            total_seats = int(total_seats_input)
            if total_seats > 0:
                break
            print("❌ Total seats must be greater than 0.")
        except ValueError:
            print("❌ Please enter a valid number for total seats.")

    while True:
        price_input = input("Ticket Price: ").strip()
        price = validate_price(price_input)
        if price is not None:
            break

    data.buses[bus_id] = {
        "name": bus_name,
        "source": source,
        "destination": destination,
        "date": travel_date,
        "departure": departure,
        "arrival": arrival,
        "total_seats": total_seats,
        "available_seats": list(range(1, total_seats + 1)),
        "price": price,
    }

    data.save_all_data()

    print(f"\n✅ Bus {bus_id} added successfully.")
    print(f"Bus Name: {bus_name}")
    print(f"Route: {source} → {destination}")
    print(f"Date: {travel_date}")
    print(f"Price: ₹{price}")


def edit_bus():
    """Edit one or more details of an existing bus."""
    print_header("✏️  EDIT BUS")

    while True:
        bus_id_input = input("Enter Bus ID to edit: ").strip()
        if not bus_id_input:
            print("❌ Bus ID cannot be empty.")
            continue
        try:
            bus_id = int(bus_id_input)
        except ValueError:
            print("❌ Invalid Bus ID. Please enter a number.")
            continue

        if not validate_bus_id(bus_id, data.buses):
            print("❌ Bus ID does not exist.")
            return
        break

    bus_info = data.buses[bus_id]

    while True:
        print("\nSelect the field to edit:")
        print("1. Bus Name")
        print("2. Source")
        print("3. Destination")
        print("4. Travel Date")
        print("5. Departure Time")
        print("6. Arrival Time")
        print("7. Price")
        print("8. Done")

        field_choice = input("Enter choice (1-8): ").strip()
        choice_num = validate_menu_choice(field_choice, 8)

        if choice_num is None:
            print()
            continue

        if choice_num == 1:
            while True:
                new_name = input("Enter new bus name: ").strip()
                if validate_bus_name(new_name):
                    bus_info["name"] = new_name
                    print("✅ Bus name updated.")
                    break
                print("❌ Bus name cannot be empty.")

        elif choice_num == 2:
            while True:
                new_source = input("Enter new source city: ").strip()
                if validate_location(new_source):
                    bus_info["source"] = new_source
                    print("✅ Source updated.")
                    break
                print("❌ Source city cannot be empty.")

        elif choice_num == 3:
            while True:
                new_destination = input("Enter new destination city: ").strip()
                if validate_location(new_destination):
                    bus_info["destination"] = new_destination
                    print("✅ Destination updated.")
                    break
                print("❌ Destination city cannot be empty.")

        elif choice_num == 4:
            while True:
                new_date = input("Enter new travel date (YYYY-MM-DD): ").strip()
                if validate_date_format(new_date):
                    bus_info["date"] = new_date
                    print("✅ Travel date updated.")
                    break
                print("❌ Invalid date format. Please use YYYY-MM-DD.")

        elif choice_num == 5:
            while True:
                new_departure = input("Enter new departure time (HH:MM): ").strip()
                if new_departure:
                    bus_info["departure"] = new_departure
                    print("✅ Departure time updated.")
                    break
                print("❌ Departure time cannot be empty.")

        elif choice_num == 6:
            while True:
                new_arrival = input("Enter new arrival time (HH:MM): ").strip()
                if new_arrival:
                    bus_info["arrival"] = new_arrival
                    print("✅ Arrival time updated.")
                    break
                print("❌ Arrival time cannot be empty.")

        elif choice_num == 7:
            while True:
                new_price = input("Enter new ticket price: ").strip()
                validated_price = validate_price(new_price)
                if validated_price is not None:
                    bus_info["price"] = validated_price
                    print("✅ Price updated.")
                    break

        elif choice_num == 8:
            data.save_all_data()
            print("\n✅ Bus details updated successfully.")
            return

        print("\nCurrent bus details:")
        bus.display_bus_detailed(bus_id, bus_info)


def has_active_bookings(bus_id):
    """Return True if the bus still has active bookings."""
    for booking in data.bookings.values():
        if booking.get("bus_id") == bus_id and booking.get("status") != "cancelled":
            return True
    return False


def remove_bus():
    """Remove a bus only if it has no active bookings."""
    print_header("🗑️  REMOVE BUS")

    while True:
        bus_id_input = input("Enter Bus ID to remove: ").strip()
        if not bus_id_input:
            print("❌ Bus ID cannot be empty.")
            continue
        try:
            bus_id = int(bus_id_input)
        except ValueError:
            print("❌ Invalid Bus ID. Please enter a number.")
            continue

        if not validate_bus_id(bus_id, data.buses):
            print("❌ Bus ID does not exist.")
            return
        break

    bus_info = data.buses[bus_id]
    if has_active_bookings(bus_id):
        print(f"❌ Cannot remove bus {bus_id}. It has active bookings.")
        print("Please cancel the bookings first.")
        return

    print("\nBus to remove:")
    bus.display_bus_detailed(bus_id, bus_info)

    confirm = input("Are you sure you want to remove this bus? (y/n): ").strip().lower()
    if confirm != 'y':
        print("✅ Removal cancelled.")
        return

    del data.buses[bus_id]
    data.save_all_data()
    print(f"✅ Bus {bus_id} removed successfully.")


def view_all_bookings_admin():
    """Show all bookings made during the current program execution."""
    print_header("📋 ALL BOOKINGS")

    if not data.bookings:
        print("No bookings have been made yet.")
        return

    print(f"{'Booking ID':<12} {'Passenger':<18} {'Bus':<15} {'Date':<12} {'Seat':<6} {'Status':<10} {'Price':<8}")
    print('-' * 95)

    for booking_id, booking in sorted(data.bookings.items()):
        bus_id = booking.get('bus_id')
        bus_info = get_bus_by_id(bus_id, data.buses)
        bus_name = bus_info['name'] if bus_info else 'Removed Bus'
        print(
            f"{booking_id:<12} "
            f"{booking.get('passenger_name', 'N/A'):<18} "
            f"{bus_name[:15]:<15} "
            f"{booking.get('date', 'N/A'):<12} "
            f"{str(booking.get('seat', 'N/A')):<6} "
            f"{booking.get('status', 'N/A'):<10} "
            f"₹{booking.get('price', 0):<8}"
        )
