name = input("What is your name? ")
age = input("How old are you? ")
age = int(age)  # Convert age to an integer
city = input("Which city do you live in? ")
working = input("Are you currently working? ")

if working == "yes":
    working = True
else:
    working = False

working = bool(working)  # Convert working to a boolean
profile = {
    "name": name,
    "age": age,
    "city": city,
    "working": working
    }

print("Profile Summary:")
print(f"Name: {profile['name']}")
print(f"Age: {profile['age']}")
print(f"City: {profile['city']}")
print(f"Working: {profile['working']}")