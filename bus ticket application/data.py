# ============================================
# DATA.PY - All Global Data Structures
# ============================================
# This file contains all the data that the
# application uses. Think of it as a "database"
# stored in memory during program execution.
# ============================================

import json
import os
from copy import deepcopy

# Admin credentials (hardcoded for beginners)
admin_credentials = {
    "username": "admin",
    "password": "admin123"
}

DATA_FILE = os.path.join(os.path.dirname(__file__), "bus_booking_data.json")

DEFAULT_BUSES = {
    101: {
        "name": "Express Travels",
        "source": "Chennai",
        "destination": "Tirunelveli",
        "date": "2026-08-20",
        "departure": "08:00",
        "arrival": "14:00",
        "total_seats": 20,
        # available_seats is a list of seat numbers still available
        "available_seats": list(range(1, 21)),  # Creates [1, 2, 3, ..., 20]
        "price": 650
    },
    102: {
        "name": "City Express",
        "source": "Bangalore",
        "destination": "Mysore",
        "date": "2026-08-20",
        "departure": "09:30",
        "arrival": "13:00",
        "total_seats": 25,
        "available_seats": list(range(1, 26)),
        "price": 450
    },
    103: {
        "name": "Night Rider",
        "source": "Chennai",
        "destination": "Bangalore",
        "date": "2026-08-21",
        "departure": "22:00",
        "arrival": "06:00",
        "total_seats": 30,
        "available_seats": list(range(1, 31)),
        "price": 800
    },
    104: {
        "name": "Comfort Plus",
        "source": "Hyderabad",
        "destination": "Tirunelveli",
        "date": "2026-08-21",
        "departure": "10:00",
        "arrival": "18:30",
        "total_seats": 20,
        "available_seats": list(range(1, 21)),
        "price": 950
    }
}

# Dictionary to store all buses
# Key: Bus ID (integer)
# Value: Dictionary with bus details
buses = {}

# Dictionary to store all bookings
# Key: Booking ID (integer)
# Value: Dictionary with booking details
bookings = {}

# Counter for generating unique booking IDs
# It starts at 1001 and increments with each booking
booking_id_counter = 1001


def _convert_json_keys_to_int(data_dict):
    """Convert dictionary keys from strings back to integers."""
    converted = {}
    for key, value in data_dict.items():
        try:
            converted[int(key)] = value
        except (TypeError, ValueError):
            converted[key] = value
    return converted


def load_all_data():
    """Load buses, bookings, and booking counter from JSON file if available."""
    global buses, bookings, booking_id_counter

    if not os.path.exists(DATA_FILE):
        buses.clear()
        buses.update(deepcopy(DEFAULT_BUSES))
        bookings.clear()
        booking_id_counter = 1001
        save_all_data()
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        buses.clear()
        buses.update(deepcopy(DEFAULT_BUSES))
        bookings.clear()
        booking_id_counter = 1001
        save_all_data()
        return

    buses.clear()
    buses.update(_convert_json_keys_to_int(data.get("buses", {})))

    bookings.clear()
    bookings.update(_convert_json_keys_to_int(data.get("bookings", {})))

    stored_counter = data.get("booking_id_counter")
    if stored_counter is not None:
        booking_id_counter = int(stored_counter)
    else:
        booking_id_counter = max(bookings.keys(), default=1000) + 1

    if booking_id_counter < 1001:
        booking_id_counter = 1001


def save_all_data():
    """Save the in-memory data to the JSON file."""
    payload = {
        "buses": {str(bus_id): bus for bus_id, bus in buses.items()},
        "bookings": {str(booking_id): booking for booking_id, booking in bookings.items()},
        "booking_id_counter": booking_id_counter
    }

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)


# Load saved data when this module is imported.
load_all_data()
