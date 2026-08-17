# 📚 Quick Reference Guide

## Getting Started

### Run the Application
```bash
cd "/Users/prakash.ramaswamy/Documents/EMC/day_2/bus ticket application"
python3 main.py
```

---

## 🚀 Quick Flows

### Data is saved automatically
- Bus details and bookings are stored in `bus_booking_data.json`
- When you restart the app, the saved data is loaded again
- This means bookings and admin-edited buses are not lost between runs


### **FLOW 1: Book a Ticket**
```
Main Menu: 1 (User Login)
  ↓
User Menu: 1 (Book Ticket)
  ↓
Select Bus Options:
  1. View All Buses
  2. Filter by Date
  3. Filter by Route
  4. Filter by Price
  5. Advanced Filter
  ↓
Choose Bus ID (e.g., 101)
  ↓
Choose Seat Number (e.g., 5)
  ↓
Enter Passenger Details:
  - Name: Prakash
  - Age: 25
  - Phone: 9876543210
  ↓
✅ Booking Confirmed! (ID: 1001)
```

### **FLOW 2: View Available Buses**
```
Main Menu: 1 (User Login)
  ↓
User Menu: 4 (View Available Buses)
  ↓
Choose Filter:
  1. View ALL
  2. Filter by Date
  3. Filter by Route
  4. Filter by Price
  5. Advanced Filter
  ↓
See filtered bus list
```

### **FLOW 3: Admin Login**
```
Main Menu: 2 (Admin Login)
  ↓
Username: admin
Password: admin123
  ↓
✅ Access Admin Panel
  ↓
Options:
  1. View All Buses
  2. Add New Bus
  3. Edit Bus
  4. Remove Bus
  5. View All Bookings
  6. Logout
```

### **FLOW 4: Cancel Ticket**
```
Main Menu: 1 (User Login)
  ↓
User Menu: 2 (Cancel Ticket)
  ↓
Enter Booking ID (e.g., 1001)
  ↓
Confirm Cancellation
  ↓
✅ Seat Released & Booking Cancelled
```

---

## 📋 Sample Data

### **Buses Available**

```
Bus 101 - Express Travels
  Route: Chennai → Tirunelveli
  Date: 2026-08-20
  Time: 08:00 - 14:00
  Seats: 20, Price: ₹650

Bus 102 - City Express
  Route: Bangalore → Mysore
  Date: 2026-08-20
  Time: 09:30 - 13:00
  Seats: 25, Price: ₹450

Bus 103 - Night Rider
  Route: Chennai → Bangalore
  Date: 2026-08-21
  Time: 22:00 - 06:00
  Seats: 30, Price: ₹800

Bus 104 - Comfort Plus
  Route: Hyderabad → Tirunelveli
  Date: 2026-08-21
  Time: 10:00 - 18:30
  Seats: 20, Price: ₹950
```

### **Admin Credentials**
- Username: `admin`
- Password: `admin123`

---

## 🎯 Filtering Options

### **Filter by Date**
Shows buses on a specific date (YYYY-MM-DD format)

Example: `2026-08-20` → Shows Bus 101, 102

### **Filter by Route**
Shows buses between two cities (case-insensitive)

Example: `Chennai` → `Tirunelveli` → Shows Bus 101

### **Filter by Price**
Shows buses within budget

Example: `500` → Shows Bus 102 (₹450)

### **Advanced Filter**
Combine multiple criteria (all optional)

Example:
- Date: `2026-08-20`
- Price: `700`
- Result: Bus 101 (₹650), Bus 102 (₹450)

---

## ✅ Input Validation

### **Passenger Name**
- ✅ Letters only (a-z, A-Z)
- ✅ Spaces allowed
- ❌ Numbers not allowed
- ❌ Special characters not allowed

### **Passenger Age**
- ✅ Must be 1-120
- ❌ Cannot be negative
- ❌ Cannot be zero
- ❌ Cannot be > 120

### **Phone Number**
- ✅ Must have at least 10 digits
- ✅ Can include spaces and hyphens
- Examples: `9876543210`, `98-7654-3210`, `98 7654 3210`

### **Date Format**
- ✅ Must be YYYY-MM-DD
- Examples: `2026-08-20`, `2026-08-21`
- ❌ Wrong: `20/08/2026`, `08-20-2026`

### **Bus/Seat Numbers**
- ✅ Must be numeric
- ✅ Bus ID must exist
- ✅ Seat must be available
- ❌ Seat cannot be already booked

---

## 🔍 Finding Your Booking

When you book, you get a **Booking ID** (e.g., 1001, 1002, 1003...)

**Save this ID!** You'll need it to cancel or view the booking later.

---

## 💡 Tips & Tricks

1. **Case-Insensitive:** City names work in any case
   - `Chennai`, `CHENNAI`, `chennai` all work

2. **Optional Fields:** In advanced filter, skip fields by pressing Enter

3. **Seat Visualization:** Seats are shown with best layout (10 per line)

4. **Availability Updates:** Available seats update instantly after booking

5. **Error Messages:** All errors clearly explain what went wrong

---

## 🚀 Phase Completion Status

| Phase | Feature | Files | Status |
|-------|---------|-------|--------|
| 1 | Core Structure | data.py, main.py, utils.py | ✅ |
| 2 | View Buses | bus.py, user.py | ✅ |
| 3 | Book Ticket | user.py, bus.py | ✅ |
| 4 | Cancel Ticket | user.py, bus.py | ✅ |
| 5 | View Bookings | user.py | ✅ |
| 6 | Admin Features | admin.py | ✅ |

---

## 📁 File Reference

### Core Files
- **main.py** - Entry point, main menu loop
- **data.py** - All data (buses, bookings, admin)
- **user.py** - User features (booking, cancellation, viewing)
- **admin.py** - Admin authentication and features
- **bus.py** - Bus operations (filtering, display, seat management)

### Utility Files
- **validation.py** - Input validation functions
- **utils.py** - Helper functions

### Documentation
- **requirements.txt** - Dependencies (none!)
- **README.md** - Full documentation
- **GUIDE.md** - This quick reference

---

## 🐛 Common Issues

### **"No buses found"**
- Check date format is YYYY-MM-DD
- Verify the date actually has buses (2026-08-20 or 2026-08-21)

### **"Seat not available"**
- Seat is already booked
- Look at the available seats list
- Choose a different seat

### **"Invalid name"**
- Name contains numbers
- Use letters and spaces only

### **"Age must be between 1 and 120"**
- Age is negative, zero, or > 120
- Enter valid age

### **"Phone must have 10+ digits"**
- Phone number is too short
- Use at least 10 digits

---

## 🎓 Learning Concepts Used

- Dictionaries & nested data
- Lists & list operations
- Loops & conditionals
- Functions & parameters
- String methods (`.lower()`, `.strip()`, `.split()`)
- Input validation
- Error handling
- Menu-driven UI
- Data persistence (in memory)
- Module organization

---

## 📞 Quick Help

| Question | Answer |
|----------|--------|
| How to start? | `python3 main.py` |
| How to book? | User → Book Ticket → Select Bus → Select Seat → Enter Details |
| How to cancel? | User → Cancel Ticket → Enter Booking ID → Confirm |
| How to view bookings? | User → View My Bookings (Phase 5) |
| Admin password? | admin/admin123 |
| Where's the data stored? | In memory (resets on restart) |
| Can I add buses? | Yes, edit data.py or use Admin features (Phase 6) |

---

**🎉 Enjoy exploring the Bus Ticket Booking System!**

