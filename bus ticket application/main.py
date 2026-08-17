# ============================================
# MAIN.PY - Entry Point
# ============================================
# This is where the program starts.
# It displays the main menu and controls
# the overall flow of the application.
# ============================================

import data
import user
import admin
from utils import print_header, print_separator
from validation import validate_menu_choice


def show_main_menu():
    """
    Displays the main menu with options for:
    - User Login (Book/Cancel/View tickets)
    - Admin Login (Manage buses)
    - Exit
    """
    print_header("🚌 BUS TICKET BOOKING SYSTEM 🚌")
    print("\nChoose an option:\n")
    print("1. 👤 User Login (Book/Cancel Tickets)")
    print("2. 🔐 Admin Login (Manage Buses)")
    print("3. 🚪 Exit")
    print()


def main():
    """
    Main program loop.
    Keeps running until user selects Exit.
    """
    while True:
        show_main_menu()
        
        choice = input("Enter your choice (1-3): ").strip()
        
        # Validate the choice
        choice_num = validate_menu_choice(choice, 3)
        
        if choice_num is None:
            print()
            continue
        
        # Option 1: User Login
        if choice_num == 1:
            print()
            user.show_user_menu()
        
        # Option 2: Admin Login
        elif choice_num == 2:
            print()
            admin.admin_login()
        
        # Option 3: Exit
        elif choice_num == 3:
            data.save_all_data()
            print_header("Thank you for using Bus Ticket Booking System!")
            print("👋 Goodbye!\n")
            break
        
        print()


# This is the standard way to run Python programs
# It ensures main() only runs when this file is executed directly,
# not when it's imported by another file
if __name__ == "__main__":
    main()
