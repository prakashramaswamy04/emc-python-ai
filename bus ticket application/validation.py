# ============================================
# VALIDATION.PY - Input Validation Functions
# ============================================
# This file contains all validation logic
# to check if user input is valid.
# ============================================

def validate_menu_choice(choice, max_choice):
    """
    Validates if user's menu choice is valid.
    
    Args:
        choice (str): The input from user
        max_choice (int): Maximum valid choice number
    
    Returns:
        int: The choice if valid, None if invalid
    """
    try:
        choice_num = int(choice)
        if 1 <= choice_num <= max_choice:
            return choice_num
        else:
            print(f"❌ Please enter a number between 1 and {max_choice}")
            return None
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
        return None


def validate_date_format(date_string):
    """
    Validates if date is in YYYY-MM-DD format.
    Does NOT check if date is valid or in future.
    
    Args:
        date_string (str): Date in format YYYY-MM-DD
    
    Returns:
        bool: True if format is correct, False otherwise
    """
    if len(date_string) != 10:
        return False
    
    parts = date_string.split("-")
    if len(parts) != 3:
        return False
    
    year, month, day = parts
    
    # Check if all parts are digits
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    
    return True


def validate_bus_id(bus_id, buses_dict):
    """
    Checks if bus ID exists in our buses dictionary.
    
    Args:
        bus_id (int): Bus ID to check
        buses_dict (dict): The buses dictionary
    
    Returns:
        bool: True if bus exists, False otherwise
    """
    return bus_id in buses_dict


def validate_seat_number(seat_num, available_seats):
    """
    Checks if seat number is available.
    
    Args:
        seat_num (int): Seat number to check
        available_seats (list): List of available seats
    
    Returns:
        bool: True if seat is available, False otherwise
    """
    return seat_num in available_seats


def validate_passenger_name(name):
    """
    Validates passenger name is not empty and contains only letters and spaces.
    
    Args:
        name (str): Passenger name
    
    Returns:
        bool: True if valid, False otherwise
    """
    if not name or len(name.strip()) == 0:
        return False
    
    # Allow letters and spaces only
    for char in name:
        if not (char.isalpha() or char.isspace()):
            return False
    
    return True


def validate_age(age_string):
    """
    Validates if age is a valid positive number between 1 and 120.
    
    Args:
        age_string (str): Age as string
    
    Returns:
        int: Age if valid, None if invalid
    """
    try:
        age = int(age_string)
        if 1 <= age <= 120:
            return age
        else:
            print("❌ Age must be between 1 and 120")
            return None
    except ValueError:
        print("❌ Please enter a valid age number")
        return None


def validate_phone_number(phone):
    """
    Validates if phone number has at least 10 digits.
    
    Args:
        phone (str): Phone number
    
    Returns:
        bool: True if valid, False otherwise
    """
    # Remove all spaces and hyphens
    digits_only = phone.replace(" ", "").replace("-", "")
    
    # Check if it has at least 10 digits
    if digits_only.isdigit() and len(digits_only) >= 10:
        return True
    
    return False


def validate_price(price_string):
    """
    Validates if price is a positive number.
    
    Args:
        price_string (str): Price as string
    
    Returns:
        int/float: Price if valid, None if invalid
    """
    try:
        price = float(price_string)
        if price > 0:
            return price
        else:
            print("❌ Price must be greater than 0")
            return None
    except ValueError:
        print("❌ Please enter a valid price")
        return None


def validate_bus_name(name):
    """
    Validates bus name is not empty.
    
    Args:
        name (str): Bus name
    
    Returns:
        bool: True if valid, False otherwise
    """
    return name and len(name.strip()) > 0


def validate_location(location):
    """
    Validates location (city name) is not empty.
    
    Args:
        location (str): Location/City name
    
    Returns:
        bool: True if valid, False otherwise
    """
    return location and len(location.strip()) > 0
