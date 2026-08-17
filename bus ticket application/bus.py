# ============================================
# BUS.PY - Bus Filtering & Display Functions
# ============================================
# This file handles all bus-related operations:
# - Filtering buses by date, source, destination
# - Displaying bus information
# ============================================

from utils import print_header, print_separator
from validation import validate_date_format


def filter_buses_by_date(travel_date, buses_dict):
    """
    Filters buses available on a specific date.
    
    Args:
        travel_date (str): Date in format YYYY-MM-DD
        buses_dict (dict): The buses dictionary
    
    Returns:
        dict: Filtered buses for that date
               Key: Bus ID, Value: Bus details
    """
    filtered = {}
    
    for bus_id, bus_info in buses_dict.items():
        if bus_info["date"] == travel_date:
            filtered[bus_id] = bus_info
    
    return filtered


def filter_buses_by_source(source, buses_dict):
    """
    Filters buses by source city (case-insensitive).
    
    Args:
        source (str): Source city name
        buses_dict (dict): The buses dictionary
    
    Returns:
        dict: Filtered buses from that source
    """
    filtered = {}
    source_lower = source.lower()
    
    for bus_id, bus_info in buses_dict.items():
        if bus_info["source"].lower() == source_lower:
            filtered[bus_id] = bus_info
    
    return filtered


def filter_buses_by_destination(destination, buses_dict):
    """
    Filters buses by destination city (case-insensitive).
    
    Args:
        destination (str): Destination city name
        buses_dict (dict): The buses dictionary
    
    Returns:
        dict: Filtered buses to that destination
    """
    filtered = {}
    destination_lower = destination.lower()
    
    for bus_id, bus_info in buses_dict.items():
        if bus_info["destination"].lower() == destination_lower:
            filtered[bus_id] = bus_info
    
    return filtered


def filter_buses_by_route(source, destination, buses_dict):
    """
    Filters buses by both source and destination.
    
    Args:
        source (str): Source city name
        destination (str): Destination city name
        buses_dict (dict): The buses dictionary
    
    Returns:
        dict: Filtered buses for that route
    """
    filtered = {}
    source_lower = source.lower()
    destination_lower = destination.lower()
    
    for bus_id, bus_info in buses_dict.items():
        if (bus_info["source"].lower() == source_lower and 
            bus_info["destination"].lower() == destination_lower):
            filtered[bus_id] = bus_info
    
    return filtered


def filter_buses_advanced(buses_dict, source=None, destination=None, date=None, max_price=None):
    """
    Advanced filter with multiple criteria.
    You can filter by any combination of: source, destination, date, price.
    None means "don't filter by this criteria".
    
    Args:
        buses_dict (dict): The buses dictionary
        source (str): Source city (optional)
        destination (str): Destination city (optional)
        date (str): Travel date in YYYY-MM-DD (optional)
        max_price (int/float): Maximum price (optional)
    
    Returns:
        dict: Filtered buses matching all criteria
    """
    filtered = buses_dict.copy()
    
    # Filter by source if provided
    if source:
        filtered = {bus_id: bus for bus_id, bus in filtered.items()
                   if bus["source"].lower() == source.lower()}
    
    # Filter by destination if provided
    if destination:
        filtered = {bus_id: bus for bus_id, bus in filtered.items()
                   if bus["destination"].lower() == destination.lower()}
    
    # Filter by date if provided
    if date:
        filtered = {bus_id: bus for bus_id, bus in filtered.items()
                   if bus["date"] == date}
    
    # Filter by max price if provided
    if max_price is not None:
        filtered = {bus_id: bus for bus_id, bus in filtered.items()
                   if bus["price"] <= max_price}
    
    return filtered


def display_bus_list(buses_dict, title="Available Buses"):
    """
    Displays a formatted list of buses.
    
    Args:
        buses_dict (dict): Dictionary of buses to display
        title (str): Title to display above the list
    """
    if not buses_dict:
        print("\n❌ No buses found matching your criteria.")
        return
    
    print_header(title)
    
    for bus_id, bus_info in buses_dict.items():
        print(f"\n🚌 Bus ID: {bus_id}")
        print(f"   Name: {bus_info['name']}")
        print(f"   Route: {bus_info['source']} → {bus_info['destination']}")
        print(f"   Date: {bus_info['date']}")
        print(f"   Departure: {bus_info['departure']} | Arrival: {bus_info['arrival']}")
        print(f"   Available Seats: {len(bus_info['available_seats'])}/{bus_info['total_seats']}")
        print(f"   Price: ₹{bus_info['price']}")
        print_separator("-", 50)


def display_bus_detailed(bus_id, bus_info):
    """
    Displays detailed information about a single bus.
    
    Args:
        bus_id (int): Bus ID
        bus_info (dict): Bus details
    """
    print_header(f"Bus Details - ID {bus_id}")
    print(f"Bus Name: {bus_info['name']}")
    print(f"Source: {bus_info['source']}")
    print(f"Destination: {bus_info['destination']}")
    print(f"Travel Date: {bus_info['date']}")
    print(f"Departure Time: {bus_info['departure']}")
    print(f"Arrival Time: {bus_info['arrival']}")
    print(f"Total Seats: {bus_info['total_seats']}")
    print(f"Available Seats: {len(bus_info['available_seats'])}")
    print(f"Price: ₹{bus_info['price']}")
    print()


def display_available_seats(bus_info, max_per_line=10):
    """
    Displays available seat numbers in a formatted way.
    
    Args:
        bus_info (dict): Bus details
        max_per_line (int): How many seats to show per line
    """
    seats = bus_info['available_seats']
    
    if not seats:
        print("❌ No seats available on this bus.")
        return
    
    print(f"\n📋 Available Seats ({len(seats)} seats): ")
    print("Seat Numbers: ", end="")
    
    for i, seat in enumerate(sorted(seats)):
        print(seat, end=" ")
        if (i + 1) % max_per_line == 0:
            print("\n              ", end="")
    
    print("\n")


def get_all_cities(buses_dict):
    """
    Gets a list of all unique cities (sources and destinations).
    Useful for showing users what routes are available.
    
    Args:
        buses_dict (dict): The buses dictionary
    
    Returns:
        dict: {"sources": [...], "destinations": [...]}
    """
    sources = set()
    destinations = set()
    
    for bus_info in buses_dict.values():
        sources.add(bus_info["source"])
        destinations.add(bus_info["destination"])
    
    return {
        "sources": sorted(list(sources)),
        "destinations": sorted(list(destinations))
    }


def get_all_dates(buses_dict):
    """
    Gets all unique dates buses are running.
    
    Args:
        buses_dict (dict): The buses dictionary
    
    Returns:
        list: Sorted list of dates in YYYY-MM-DD format
    """
    dates = set()
    
    for bus_info in buses_dict.values():
        dates.add(bus_info["date"])
    
    return sorted(list(dates))


def display_available_cities_and_dates(buses_dict):
    """
    Displays all available cities and dates to help user filter.
    
    Args:
        buses_dict (dict): The buses dictionary
    """
    cities_data = get_all_cities(buses_dict)
    dates = get_all_dates(buses_dict)
    
    print("\n📍 AVAILABLE CITIES:")
    print("   From:", ", ".join(cities_data["sources"]))
    print("   To:", ", ".join(cities_data["destinations"]))
    
    print("\n📅 AVAILABLE DATES:")
    for i, date in enumerate(dates, 1):
        print(f"   {i}. {date}")
    print()


def book_seat(bus_id, seat_number, buses_dict):
    """
    Books a seat on a bus.
    Removes the seat from available_seats list.
    
    Args:
        bus_id (int): Bus ID
        seat_number (int): Seat number to book
        buses_dict (dict): The buses dictionary
    
    Returns:
        bool: True if seat was booked successfully, False if already booked
    """
    if bus_id not in buses_dict:
        return False
    
    bus_info = buses_dict[bus_id]
    
    # Check if seat is available
    if seat_number not in bus_info["available_seats"]:
        return False
    
    # Remove seat from available list (book it)
    bus_info["available_seats"].remove(seat_number)
    return True


def unbook_seat(bus_id, seat_number, buses_dict):
    """
    Cancels a booking and makes seat available again.
    Adds the seat back to available_seats list.
    
    Args:
        bus_id (int): Bus ID
        seat_number (int): Seat number to unbook
        buses_dict (dict): The buses dictionary
    
    Returns:
        bool: True if seat was unboooked successfully, False if already available
    """
    if bus_id not in buses_dict:
        return False
    
    bus_info = buses_dict[bus_id]
    
    # Check if seat is already available (shouldn't unbook an already available seat)
    if seat_number in bus_info["available_seats"]:
        return False
    
    # Add seat back to available list
    bus_info["available_seats"].append(seat_number)
    bus_info["available_seats"].sort()  # Keep seats sorted
    return True
