# ============================================
# UTILS.PY - Helper Functions
# ============================================
# This file contains utility functions that
# help with common tasks like ID generation,
# printing, and data lookup.
# ============================================

def generate_booking_id():
    """
    Generates a unique booking ID.
    This imports the counter from data.py and increments it.
    
    Returns:
        int: A unique booking ID
    """
    # Import here to avoid circular imports
    import data
    
    current_id = data.booking_id_counter
    data.booking_id_counter += 1
    return current_id


def get_bus_by_id(bus_id, buses_dict):
    """
    Retrieves a bus's details by its ID.
    
    Args:
        bus_id (int): Bus ID to look up
        buses_dict (dict): The buses dictionary
    
    Returns:
        dict: Bus details if found, None if not found
    """
    if bus_id in buses_dict:
        return buses_dict[bus_id]
    return None


def print_separator(char="-", length=50):
    """
    Prints a decorative separator line.
    
    Args:
        char (str): Character to use (default "-")
        length (int): How many characters to print
    """
    print(char * length)


def print_header(title):
    """
    Prints a nice header for a section.
    
    Args:
        title (str): Title to display
    """
    print("\n")
    print("=" * 50)
    print(title.center(50))
    print("=" * 50)


def get_booking_by_id(booking_id, bookings_dict):
    """
    Retrieves a booking's details by its ID.
    
    Args:
        booking_id (int): Booking ID to look up
        bookings_dict (dict): The bookings dictionary
    
    Returns:
        dict: Booking details if found, None if not found
    """
    if booking_id in bookings_dict:
        return bookings_dict[booking_id]
    return None
