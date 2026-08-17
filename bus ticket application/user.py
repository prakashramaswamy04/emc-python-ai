# ============================================
# USER.PY - User Booking Functions
# ============================================
# Functions for users to:
# - Book tickets
# - Cancel tickets
# - View their bookings
# ============================================

import data
import bus
from utils import print_header, generate_booking_id, get_bus_by_id, get_booking_by_id
from validation import (
    validate_menu_choice, validate_date_format, validate_price,
    validate_seat_number, validate_passenger_name, validate_age,
    validate_phone_number, validate_bus_id
)


def show_user_menu():
    """
    Main user menu.
    Displays options for booking, cancellation, and viewing bookings.
    """
    while True:
        print_header("👤 USER MENU")
        print("\nChoose an option:\n")
        print("1. 📖 Book Ticket")
        print("2. ❌ Cancel Ticket")
        print("3. 📋 View My Bookings")
        print("4. 🚌 View Available Buses")
        print("5. 🚪 Back to Main Menu")
        print()
        
        choice = input("Enter your choice (1-5): ").strip()
        
        choice_num = validate_menu_choice(choice, 5)
        
        if choice_num is None:
            print()
            continue
        
        if choice_num == 1:
            book_ticket()
        elif choice_num == 2:
            cancel_ticket()
        elif choice_num == 3:
            view_my_bookings()
        elif choice_num == 4:
            view_available_buses()
        elif choice_num == 5:
            print("✅ Returning to main menu...\n")
            break
        
        print()


def book_ticket():
    """
    Complete booking workflow:
    1. Show available buses (with optional filtering)
    2. User selects a bus
    3. Show available seats on bus
    4. User selects a seat
    5. Collect passenger details
    6. Create booking
    7. Show confirmation ticket
    """
    print_header("📖 BOOK A TICKET")
    
    # Step 1: Let user find and select a bus
    selected_bus_id = select_bus_for_booking()
    if selected_bus_id is None:
        print("❌ Booking cancelled.\n")
        return
    
    # Get bus details
    bus_info = get_bus_by_id(selected_bus_id, data.buses)
    if bus_info is None:
        print("❌ Bus not found.\n")
        return
    
    # Step 2: Show bus details and available seats
    print()
    bus.display_bus_detailed(selected_bus_id, bus_info)
    
    # Step 3: Ask how many passengers are traveling
    passenger_count = get_passenger_count()

    # Step 4: Let user select one seat for each passenger
    selected_seats = select_seat_for_booking(bus_info, passenger_count)
    if selected_seats is None:
        print("❌ Booking cancelled.\n")
        return

    # Step 5: Collect passenger details and assign each seat
    passengers = []
    print()
    print_header("👤 ENTER PASSENGER DETAILS")

    for index, seat_num in enumerate(selected_seats, start=1):
        print(f"\n--- Passenger {index} | Seat {seat_num} ---")

        passenger_name = get_passenger_name()
        if passenger_name is None:
            print("❌ Booking cancelled.\n")
            return

        passenger_age = get_passenger_age()
        if passenger_age is None:
            print("❌ Booking cancelled.\n")
            return

        passenger_phone = get_passenger_phone()
        if passenger_phone is None:
            print("❌ Booking cancelled.\n")
            return

        passengers.append({
            "seat": seat_num,
            "passenger_name": passenger_name,
            "passenger_age": passenger_age,
            "passenger_phone": passenger_phone,
        })

    # Step 6: Create booking
    booking_id = generate_booking_id()
    total_price = bus_info["price"] * passenger_count

    # Store booking in data.bookings
    data.bookings[booking_id] = {
        "passengers": passengers,
        "passenger_name": passengers[0]["passenger_name"],
        "passenger_age": passengers[0]["passenger_age"],
        "passenger_phone": passengers[0]["passenger_phone"],
        "bus_id": selected_bus_id,
        "seat": ", ".join(str(p["seat"]) for p in passengers),
        "seats": selected_seats,
        "seat_count": passenger_count,
        "date": bus_info["date"],
        "price": total_price,
        "price_per_seat": bus_info["price"],
        "status": "confirmed"
    }

    # Book each seat (remove from available_seats)
    for seat_num in selected_seats:
        bus.book_seat(selected_bus_id, seat_num, data.buses)

    data.save_all_data()

    # Step 7: Display confirmation
    print()
    display_booking_ticket(booking_id, data.bookings[booking_id], bus_info)


def select_bus_for_booking():
    """
    Lets user find a bus by:
    1. Browsing all buses
    2. Filtering by date
    3. Filtering by route
    4. Advanced filter
    
    Returns:
        int: Selected bus ID, or None if cancelled
    """
    while True:
        print_header("🚌 SELECT A BUS")
        print("\nChoose how to find a bus:\n")
        print("1. 👀 View All Buses")
        print("2. 📅 Filter by Date")
        print("3. 🗺️  Filter by Route")
        print("4. 💰 Filter by Price")
        print("5. 🔍 Advanced Filter")
        print("6. 🚪 Cancel Booking")
        print()
        
        choice = input("Enter your choice (1-6): ").strip()
        choice_num = validate_menu_choice(choice, 6)
        
        if choice_num is None:
            print()
            continue
        
        filtered_buses = None
        
        if choice_num == 1:
            filtered_buses = data.buses
        elif choice_num == 2:
            filtered_buses = get_buses_by_date_input()
        elif choice_num == 3:
            filtered_buses = get_buses_by_route_input()
        elif choice_num == 4:
            filtered_buses = get_buses_by_price_input()
        elif choice_num == 5:
            filtered_buses = get_buses_by_advanced_input()
        elif choice_num == 6:
            return None
        
        if filtered_buses is None or len(filtered_buses) == 0:
            print("❌ No buses found. Try different filters.\n")
            input("Press Enter to continue...")
            continue
        
        # Display filtered buses
        bus.display_bus_list(filtered_buses, "AVAILABLE BUSES")
        
        # Ask user to select a bus
        print()
        bus_id_input = input("Enter Bus ID to book (or press Enter to filter again): ").strip()
        
        if not bus_id_input:
            print()
            continue
        
        try:
            bus_id = int(bus_id_input)
        except ValueError:
            print("❌ Invalid Bus ID. Please enter a number.\n")
            continue
        
        # Validate bus exists in filtered list
        if bus_id not in filtered_buses:
            print("❌ Bus ID not found. Please select from the list above.\n")
            continue
        
        # Check if bus still has seats
        if len(filtered_buses[bus_id]["available_seats"]) == 0:
            print("❌ No seats available on this bus.\n")
            continue
        
        return bus_id


def parse_selected_seats(seat_input):
    """
    Converts user input like '1, 3, 5' or '1 3 5' into a clean list of seat numbers.
    Returns a list of ints, or None if the input is invalid.
    """
    if not seat_input:
        return None

    cleaned = seat_input.replace(',', ' ').replace(';', ' ')
    parts = cleaned.split()
    if not parts:
        return None

    seats = []
    for part in parts:
        try:
            seat_num = int(part)
        except ValueError:
            return None

        if seat_num <= 0:
            return None
        seats.append(seat_num)

    # Remove duplicates while preserving order
    unique_seats = []
    seen = set()
    for seat_num in seats:
        if seat_num in seen:
            continue
        seen.add(seat_num)
        unique_seats.append(seat_num)

    return unique_seats


def get_passenger_count():
    """Ask how many passengers are traveling and validate 1 to 6."""
    while True:
        count_input = input("How many passengers? (1-6): ").strip()

        if not count_input:
            print("❌ Passenger count cannot be empty.")
            continue

        try:
            passenger_count = int(count_input)
        except ValueError:
            print("❌ Please enter a valid number between 1 and 6.")
            continue

        if passenger_count < 1 or passenger_count > 6:
            print("❌ Total passengers must be between 1 and 6.")
            continue

        return passenger_count


def select_seat_for_booking(bus_info, passenger_count):
    """
    Lets user select exactly as many seats as passengers.
    Example: if 3 passengers are traveling, the user must select 3 seats.
    """
    while True:
        print_header("💺 SELECT SEATS")

        bus.display_available_seats(bus_info)

        if not bus_info["available_seats"]:
            print("❌ No seats available on this bus.")
            return None

        if len(bus_info["available_seats"]) < passenger_count:
            print(f"❌ Not enough seats available. You requested {passenger_count}, but only {len(bus_info['available_seats'])} are free.")
            return None

        print(f"💡 You need {passenger_count} seat(s).")
        print("  Example: 1, 3, 5 or 1 3 5")
        seat_input = input("Enter seat number(s) for all passengers (or press Enter to cancel): ").strip()

        if not seat_input:
            return None

        selected_seats = parse_selected_seats(seat_input)
        if selected_seats is None:
            print("❌ Invalid seat input. Please enter numbers like 1, 3, 5\n")
            continue

        if len(selected_seats) != passenger_count:
            print(f"❌ You entered {len(selected_seats)} seat(s), but you need {passenger_count} seat(s).")
            continue

        invalid_seats = []
        for seat_num in selected_seats:
            if not validate_seat_number(seat_num, bus_info["available_seats"]):
                invalid_seats.append(seat_num)

        if invalid_seats:
            print(f"❌ These seats are not available: {invalid_seats}")
            print(f"❌ Available seats: {sorted(bus_info['available_seats'])}\n")
            continue

        return sorted(selected_seats)


def get_passenger_name():
    """
    Gets and validates passenger name.
    
    Returns:
        str: Passenger name, or None if cancelled/invalid
    """
    while True:
        name = input("Passenger Name: ").strip()
        
        if not name:
            print("❌ Name cannot be empty.")
            continue
        
        if not validate_passenger_name(name):
            print("❌ Name should contain only letters and spaces.")
            continue
        
        return name


def get_passenger_age():
    """
    Gets and validates passenger age.
    
    Returns:
        int: Passenger age, or None if cancelled/invalid
    """
    while True:
        age_input = input("Passenger Age: ").strip()
        
        if not age_input:
            print("❌ Age cannot be empty.")
            continue
        
        age = validate_age(age_input)
        if age is None:
            continue
        
        return age


def get_passenger_phone():
    """
    Gets and validates passenger phone number.
    
    Returns:
        str: Passenger phone number, or None if cancelled/invalid
    """
    while True:
        phone = input("Passenger Phone Number: ").strip()
        
        if not phone:
            print("❌ Phone number cannot be empty.")
            continue
        
        if not validate_phone_number(phone):
            print("❌ Phone number should have at least 10 digits.")
            continue
        
        return phone


def display_booking_ticket(booking_id, booking_info, bus_info):
    """
    Displays a beautiful booking confirmation ticket.
    
    Args:
        booking_id (int): Booking ID
        booking_info (dict): Booking details
        bus_info (dict): Bus details
    """
    print_header("🎫 BOOKING CONFIRMED!")
    
    print(f"\n{'Booking ID':<25}: {booking_id}")
    print(f"{'Status':<25}: ✅ {booking_info['status'].upper()}")
    print(f"{'Passengers':<25}: {booking_info.get('seat_count', 1)}")

    print("\n--- Passenger List ---")
    for index, passenger in enumerate(booking_info.get('passengers', []), start=1):
        print(f"Passenger {index}: {passenger['passenger_name']} | Age: {passenger['passenger_age']} | Phone: {passenger['passenger_phone']} | Seat: {passenger['seat']}")

    print(f"\n{'Bus Name':<25}: {bus_info['name']}")
    print(f"{'Bus ID':<25}: {booking_info['bus_id']}")
    print(f"{'Route':<25}: {bus_info['source']} → {bus_info['destination']}")
    print(f"{'Travel Date':<25}: {booking_info['date']}")
    print(f"{'Departure Time':<25}: {bus_info['departure']}")
    print(f"{'Arrival Time':<25}: {bus_info['arrival']}")

    seats = booking_info.get('seats')
    if seats:
        seat_text = ", ".join(str(seat) for seat in seats)
    else:
        seat_text = booking_info.get('seat', 'N/A')

    print(f"\n{'Seat Number':<25}: {seat_text}")
    print(f"{'Price':<25}: ₹{booking_info['price']}")

    print("\n" + "=" * 50)
    print("\n✅ Your ticket has been booked successfully!")
    print(f"📌 Please save your Booking ID: {booking_id}")
    print("⏰ Please arrive 30 minutes before departure.\n")


def get_buses_by_date_input():
    """Helper: Filter buses by date input from user"""
    bus.display_available_cities_and_dates(data.buses)
    
    date_input = input("Enter date (YYYY-MM-DD): ").strip()
    
    if not validate_date_format(date_input):
        print("❌ Invalid date format.\n")
        return None
    
    return bus.filter_buses_by_date(date_input, data.buses)


def get_buses_by_route_input():
    """Helper: Filter buses by route input from user"""
    bus.display_available_cities_and_dates(data.buses)
    
    source = input("Enter Source City: ").strip()
    if not source:
        print("❌ Source cannot be empty.\n")
        return None
    
    destination = input("Enter Destination City: ").strip()
    if not destination:
        print("❌ Destination cannot be empty.\n")
        return None
    
    return bus.filter_buses_by_route(source, destination, data.buses)


def get_buses_by_price_input():
    """Helper: Filter buses by price input from user"""
    all_prices = sorted(set(b["price"] for b in data.buses.values()))
    print("\nAvailable prices: ₹" + ", ₹".join(map(str, all_prices)))
    
    price_input = input("Enter maximum price (₹): ").strip()
    max_price = validate_price(price_input)
    
    if max_price is None:
        return None
    
    return bus.filter_buses_advanced(data.buses, max_price=max_price)


def get_buses_by_advanced_input():
    """Helper: Advanced filter with multiple criteria"""
    bus.display_available_cities_and_dates(data.buses)
    
    print("\nLeave any field blank to skip that filter\n")
    
    source = input("Source City (optional): ").strip() or None
    destination = input("Destination City (optional): ").strip() or None
    
    date_str = input("Travel Date - YYYY-MM-DD (optional): ").strip() or None
    if date_str and not validate_date_format(date_str):
        print("❌ Invalid date format. Skipping date filter.")
        date_str = None
    
    max_price = None
    price_input = input("Maximum Price ₹ (optional): ").strip()
    if price_input:
        max_price = validate_price(price_input)
    
    print()  # Blank line
    
    return bus.filter_buses_advanced(
        data.buses,
        source=source,
        destination=destination,
        date=date_str,
        max_price=max_price
    )


def filter_buses_by_date():
    """
    Filter buses by travel date.
    Shows available dates for user to choose from.
    """
    print_header("📅 FILTER BY DATE")
    
    bus.display_available_cities_and_dates(data.buses)
    
    available_dates = bus.get_all_dates(data.buses)
    
    print("Enter date (YYYY-MM-DD) or select from above:")
    date_input = input("Date: ").strip()
    
    if not validate_date_format(date_input):
        print("❌ Invalid date format. Please use YYYY-MM-DD")
        return
    
    filtered = bus.filter_buses_by_date(date_input, data.buses)
    
    if not filtered:
        print(f"\n❌ No buses found for date: {date_input}")
        print("Available dates:", ", ".join(available_dates))
    else:
        bus.display_bus_list(filtered, f"BUSES ON {date_input}")


def filter_buses_by_route():
    """
    Filter buses by source and destination.
    Shows available cities for user to choose from.
    """
    print_header("🗺️  FILTER BY ROUTE")
    
    bus.display_available_cities_and_dates(data.buses)
    
    source = input("Enter Source City: ").strip()
    if not source:
        print("❌ Source city cannot be empty")
        return
    
    destination = input("Enter Destination City: ").strip()
    if not destination:
        print("❌ Destination city cannot be empty")
        return
    
    filtered = bus.filter_buses_by_route(source, destination, data.buses)
    
    if not filtered:
        print(f"\n❌ No buses found from {source} to {destination}")
    else:
        bus.display_bus_list(
            filtered, 
            f"BUSES FROM {source.upper()} TO {destination.upper()}"
        )


def filter_buses_by_price():
    """
    Filter buses by maximum price.
    Shows all available prices for reference.
    """
    print_header("💰 FILTER BY PRICE")
    
    all_prices = sorted(set(bus_info["price"] for bus_info in data.buses.values()))
    print("Available prices: ₹" + ", ₹".join(map(str, all_prices)))
    print()
    
    price_input = input("Enter maximum price (₹): ").strip()
    max_price = validate_price(price_input)
    
    if max_price is None:
        return
    
    filtered = bus.filter_buses_advanced(data.buses, max_price=max_price)
    
    if not filtered:
        print(f"\n❌ No buses found within budget of ₹{max_price}")
    else:
        bus.display_bus_list(filtered, f"BUSES UP TO ₹{max_price}")


def advanced_filter_buses():
    """
    Advanced filter with multiple criteria.
    User can filter by:
    - Source city (optional)
    - Destination city (optional)
    - Date (optional)
    - Maximum price (optional)
    """
    print_header("🔍 ADVANCED FILTER")
    
    bus.display_available_cities_and_dates(data.buses)
    
    print("Leave any field blank to skip that filter")
    source = input("Source City (optional): ").strip() or None
    
    destination = input("Destination City (optional): ").strip() or None
    
    date_str = input("Travel Date - YYYY-MM-DD (optional): ").strip() or None
    if date_str and not validate_date_format(date_str):
        print("❌ Invalid date format. Skipping date filter.")
        date_str = None
    
    max_price = None
    price_input = input("Maximum Price ₹ (optional): ").strip()
    if price_input:
        max_price = validate_price(price_input)
    
    filters_applied = []
    if source:
        filters_applied.append(f"From: {source}")
    if destination:
        filters_applied.append(f"To: {destination}")
    if date_str:
        filters_applied.append(f"Date: {date_str}")
    if max_price:
        filters_applied.append(f"Price: ≤ ₹{max_price}")
    
    filtered = bus.filter_buses_advanced(
        data.buses,
        source=source,
        destination=destination,
        date=date_str,
        max_price=max_price
    )
    
    print()
    if not filtered:
        print("❌ No buses found matching your criteria:")
        for filter_text in filters_applied:
            print(f"   • {filter_text}")
    else:
        if filters_applied:
            title = "FILTERED BUSES - " + " | ".join(filters_applied)
        else:
            title = "ALL BUSES (No filters applied)"
        bus.display_bus_list(filtered, title)


def view_available_buses():
    """
    Main function to view buses with multiple filter options.
    Users can:
    1. View ALL buses
    2. Filter by date only
    3. Filter by route (source + destination)
    4. Filter by price
    5. Advanced filter (combination of all)
    """
    while True:
        print_header("🚌 VIEW AVAILABLE BUSES")
        print("\nChoose filter option:\n")
        print("1. 👀 View ALL Buses")
        print("2. 📅 Filter by Date")
        print("3. 🗺️  Filter by Route (Source → Destination)")
        print("4. 💰 Filter by Price")
        print("5. 🔍 Advanced Filter (Multiple criteria)")
        print("6. 🚪 Back to User Menu")
        print()
        
        choice = input("Enter your choice (1-6): ").strip()
        choice_num = validate_menu_choice(choice, 6)
        
        if choice_num is None:
            print()
            continue
        
        if choice_num == 1:
            bus.display_bus_list(data.buses, "ALL AVAILABLE BUSES")
        elif choice_num == 2:
            filter_buses_by_date()
        elif choice_num == 3:
            filter_buses_by_route()
        elif choice_num == 4:
            filter_buses_by_price()
        elif choice_num == 5:
            advanced_filter_buses()
        elif choice_num == 6:
            print("✅ Returning to user menu...\n")
            break
        
        input("Press Enter to continue...")
        print()


def cancel_ticket():
    """
    Cancel a booking by Booking ID.
    - Ask for Booking ID
    - Show booking details
    - Ask for confirmation
    - Release seat and update booking status
    """
    print_header("❌ CANCEL TICKET")
    
    booking_id_input = input("Enter Booking ID to cancel (or press Enter to go back): ").strip()
    if not booking_id_input:
        return
    
    try:
        booking_id = int(booking_id_input)
    except ValueError:
        print("❌ Invalid Booking ID. It must be a number.")
        return
    
    # Find booking
    booking = get_booking_by_id(booking_id, data.bookings)
    if not booking:
        print(f"❌ Booking ID {booking_id} not found.")
        return
    
    # Display booking summary
    bus_info = get_bus_by_id(booking.get("bus_id"), data.buses)
    print("\nBooking Details:")
    print(f"  Booking ID : {booking_id}")
    print(f"  Passenger  : {booking.get('passenger_name')}")
    print(f"  Phone      : {booking.get('passenger_phone')}")
    print(f"  Bus ID     : {booking.get('bus_id')}")
    if bus_info:
        print(f"  Bus Name   : {bus_info.get('name')}")
        print(f"  Route      : {bus_info.get('source')} → {bus_info.get('destination')}")
    print(f"  Date       : {booking.get('date')}")
    print(f"  Seat       : {booking.get('seat')}")
    print(f"  Price      : ₹{booking.get('price')}")
    print(f"  Status     : {booking.get('status')}")
    
    confirm = input("\nAre you sure you want to cancel this booking? (y/n): ").strip().lower()
    if confirm != 'y':
        print("✅ Cancellation aborted.")
        return
    
    # If already cancelled
    if booking.get('status') == 'cancelled':
        print("❌ This booking is already cancelled.")
        return
    
    # Try to release the seat(s)
    bus_id = booking.get('bus_id')
    booked_seats = booking.get('seats')
    if booked_seats is None:
        single_seat = booking.get('seat')
        booked_seats = [single_seat] if single_seat is not None else []

    seats_released = 0
    if bus_id in data.buses:
        for seat_num in booked_seats:
            if bus.unbook_seat(bus_id, seat_num, data.buses):
                seats_released += 1

    # Update booking status
    booking['status'] = 'cancelled'
    data.save_all_data()

    print("\n✅ Booking cancelled successfully!")
    if seats_released:
        print(f"✅ Seat(s) {booked_seats} on Bus {bus_id} are now available again.")
    else:
        print(f"⚠️ Seat(s) {booked_seats} on Bus {bus_id} could not be released (they may already be available or the bus was removed).")
    print(f"📌 Booking ID {booking_id} status updated to CANCELLED.")


def view_my_bookings():
    """
    View bookings made during this program execution.
    Since there are no user accounts, user can filter by phone number
    or press Enter to view all bookings.
    """
    print_header("📋 VIEW BOOKINGS")
    
    if not data.bookings:
        print("\nNo bookings have been made yet.")
        return
    
    phone_input = input("Enter your phone number to filter bookings (or press Enter to view all): ").strip()
    filter_by_phone = False
    phone_digits = None
    if phone_input:
        if not validate_phone_number(phone_input):
            print("❌ Invalid phone number format. Showing all bookings instead.")
        else:
            filter_by_phone = True
            phone_digits = ''.join(ch for ch in phone_input if ch.isdigit())
    
    # Collect matching bookings
    matching = []
    for bid, booking in data.bookings.items():
        if filter_by_phone:
            bphone_digits = ''.join(ch for ch in booking.get('passenger_phone', '') if ch.isdigit())
            if bphone_digits.endswith(phone_digits):
                matching.append((bid, booking))
        else:
            matching.append((bid, booking))
    
    if not matching:
        print("\nNo bookings found for the provided phone number.")
        return
    
    # Display bookings
    print()
    print(f"{'Booking ID':<12} {'Passenger':<20} {'Bus':<15} {'Date':<12} {'Seat':<10} {'Status':<10} {'Price':<6}")
    print('-' * 95)
    for bid, booking in sorted(matching, key=lambda x: x[0]):
        bus_id = booking.get('bus_id')
        bus_info = get_bus_by_id(bus_id, data.buses)
        bus_name = bus_info['name'] if bus_info else f"Bus {bus_id}"
        seat_value = booking.get('seat')
        if isinstance(seat_value, list):
            seat_value = ', '.join(str(seat) for seat in seat_value)
        elif seat_value is None:
            seat_value = str(booking.get('seats', ''))
        print(f"{bid:<12} {booking.get('passenger_name')[:20]:<20} {bus_name[:15]:<15} {booking.get('date'):<12} {str(seat_value):<10} {booking.get('status'):<10} ₹{booking.get('price'):<6}")
    print('\n')
