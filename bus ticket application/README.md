# 🚌 Bus Ticket Booking System

A **beginner-friendly** Python terminal application for booking and managing bus tickets. Built entirely with Python's standard library to teach core programming concepts.

---

## ✨ Features

### 👤 **User Features**
- ✅ **Book Tickets** with 5 different filter options
  - View all buses
  - Filter by travel date
  - Filter by route (source → destination)
  - Filter by price
  - Advanced filter (combine multiple criteria)
- ✅ **Select Seats** with availability checking
- ✅ **View My Bookings** (shows bookings for the current run; can filter by phone)
- ✅ **Cancel Tickets** (enter Booking ID to cancel; seat is released)
- ✅ **Beautiful Ticket Display** with confirmation details
- ✅ **Data Persistence** using a JSON file so buses and bookings remain saved between runs

### 🔐 **Admin Features**
- ✅ **Admin Login** (Username: `admin`, Password: `admin123`)
- ✅ **View All Buses**
- ✅ **Add New Bus**
- ✅ **Edit Bus Details**
- ✅ **Remove Bus**
- ✅ **View All Bookings**

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.6 or higher**
- No external dependencies needed!

### Installation

1. **Open the project folder:**
```bash
cd "/Users/prakash.ramaswamy/Documents/EMC/day_2/bus ticket application"
```

2. **Run the app:**
```bash
python3 main.py
```

---

## 📖 How to Use

### **Main Menu**
```
1. 👤 User Login (Book/Cancel/View bookings)
2. 🔐 Admin Login (Manage Buses)
3. 🚪 Exit
```

### **User Menu**
```
1. 📖 Book Ticket
2. ❌ Cancel Ticket
3. 📋 View My Bookings
4. 🚌 View Available Buses
5. 🚪 Back to Main Menu
```

### **Booking Flow (Book a Ticket)**
```
1. Select "User Login"
2. Select "Book Ticket"
3. Choose filter (e.g., "View All Buses")
4. Select a bus by Bus ID
5. Select a seat from available options
6. Enter passenger details:
   - Name (letters only)
   - Age (1-120)
   - Phone number (10+ digits)
7. See your booking confirmation with Booking ID
```

### **View Bookings**
```
1. Select "User Login"
2. Select "View My Bookings"
3. Press Enter to view all bookings, or enter your phone number to filter results
4. Bookings show Booking ID, Passenger, Bus, Date, Seat, Status and Price
```

### **Cancel a Booking**
```
1. Select "User Login"
2. Select "Cancel Ticket"
3. Enter your Booking ID (e.g., 1001)
4. Confirm with 'y' to cancel
5. Booking status will be updated to "cancelled" and seat will be released back to the bus
```

### **Example Admin Login**
```
Username: admin
Password: admin123
```

---

## 📁 Project Structure

```
bus ticket application/
│
├── main.py                 # Entry point - main program loop
├── data.py                 # All data structures (buses, bookings, admin)
├── user.py                 # User booking, cancellation, view functions
├── admin.py                # Admin authentication & management (placeholders)
├── bus.py                  # Bus operations (filtering, display, seat management)
├── validation.py           # Input validation functions
├── utils.py                # Helper functions (ID generation, printing)
│
├── requirements.txt        # Dependencies (none needed!)
├── README.md               # This file
├── GUIDE.md                # Quick reference guide
└── PROJECT_SUMMARY.txt     # Detailed project summary
```

---

## 🗂️ Sample Data

### **Available Buses** (Initial Data)

| Bus ID | Name | Route | Date | Departure | Arrival | Seats | Price |
|--------|------|-------|------|-----------|---------|-------|-------|
| 101 | Express Travels | Chennai → Tirunelveli | 2026-08-20 | 08:00 | 14:00 | 20 | ₹650 |
| 102 | City Express | Bangalore → Mysore | 2026-08-20 | 09:30 | 13:00 | 25 | ₹450 |
| 103 | Night Rider | Chennai → Bangalore | 2026-08-21 | 22:00 | 06:00 | 30 | ₹800 |
| 104 | Comfort Plus | Hyderabad → Tirunelveli | 2026-08-21 | 10:00 | 18:30 | 20 | ₹950 |

### **Admin Credentials**
- **Username:** `admin`
- **Password:** `admin123`

---

## 🎯 PHASE STATUS

| Phase | Feature | Status |
|-------|---------|--------|
| 1 | Data & Menu Structure | ✅ Complete |
| 2 | View/Filter Buses | ✅ Complete |
| 3 | Book Ticket | ✅ Complete |
| 4 | Cancel Ticket | ✅ Complete |
| 5 | View My Bookings | ✅ Complete |
| 6 | Admin Management | ✅ Complete |

---

## ✅ DETAILS ON NEW FEATURES (Phase 4 & 5)

### Cancel Ticket (Phase 4)
- Users can cancel a booking by entering the Booking ID.
- The system shows booking details for confirmation.
- On confirmation (`y`), the booking status is changed to `cancelled` and the seat is added back to the bus's available seats (if the bus still exists and the seat is not already available).
- The booking record is retained (status updated) so history is preserved.

### View My Bookings (Phase 5)
- Users can view all bookings made during the current program run.
- Optionally filter bookings by passenger phone number (enter phone to filter; press Enter to show all).
- Displays a neat table with booking summary: Booking ID, Passenger, Bus, Date, Seat, Status, Price.

---

## 🧪 Testing

Try the following flows:

1. Book a ticket (User → Book Ticket) and note the Booking ID.
2. View bookings (User → View My Bookings) and filter by your phone.
3. Cancel the booking (User → Cancel Ticket) using the Booking ID and confirm.
4. Verify that the booking status is `cancelled` and the seat is available again.

---

## 🎓 Learning Concepts

This project teaches:

- Dictionaries and nested data structures
- Lists and list operations
- Loops and conditional statements
- Functions and parameters
- Input validation and error handling
- Modular code organization

---

## 📚 Future Improvements

- Persist data to JSON file so bookings survive restarts
- Refactor into classes (OOP)
- Add user accounts and authentication
- Add extra admin reporting or filtering options

---

## 📞 Support

If you need help with the project flow, validation, or a beginner-level explanation of any function, I can walk through it with you.

---

**Happy Learning! 🎓**

Start with: `python3 main.py`

