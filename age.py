# Version: 1.0

# A Python program that will take in your date of birth and calculate your current age,
# along with the day of the week you were born:

# This Python program Prompts the user to enter their date of birth in the format of YYYY-MM-DD.
# The program will then calculate your current age in years and print it along with the day of the week you were born.

# import datetime

# # Prompt user for their date of birth
# birthdate_str = input("Enter your date of birth (YYYY-MM-DD): ")

# # Convert birthdate to datetime object
# birthdate = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d')

# # Get today's date
# today = datetime.date.today()

# # Calculate age in years
# age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# # Calculate day of the week the user was born on
# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# day_of_week = days_of_week[birthdate.weekday()]

# # Print results
# print("You were born on a {}.".format(day_of_week))
# print("You are currently {} years old.".format(age))




# Improved Version: 1.0.1

# This program will prompt you for your date of birth, and then it will calculate your current age,
# the day of the week you were born on, and the number of days until your next birthday.
# To use the program, simply run it in a Python environment and follow the prompts.
# import datetime

# # Prompt user for their date of birth
# birthdate_str = input("Enter your date of birth (DD-MM-YYYY): ")

# # Convert birthdate to datetime object
# birthdate = datetime.datetime.strptime(birthdate_str, '%d-%m-%Y')

# # Get today's date
# today = datetime.date.today()

# # Calculate age in years
# age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# # Calculate day of the week the user was born on
# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# day_of_week = days_of_week[birthdate.weekday()]

# # Calculate number of days until next birthday
# next_birthday = datetime.date(today.year, birthdate.month, birthdate.day)
# if next_birthday < today:
#     next_birthday = datetime.date(today.year+1, birthdate.month, birthdate.day)
# days_until_birthday = (next_birthday - today).days

# # Print results
# print("You were born on a {}.".format(day_of_week))
# print("You are currently {} years old.".format(age))
# print("There are {} days until your next birthday.".format(days_until_birthday))


# Optimised Version: 1.0.2

import datetime

# Prompt user for their date of birth
birthdate_str = input("Enter your date of birth (YYYY-MM-DD): ")

# Convert birthdate to datetime object
birthdate = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d').date()

# Get today's date
today = datetime.date.today()

# Calculate age in years
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Calculate day of the week the user was born on
day_of_week = birthdate.strftime('%A')

# Calculate number of days until next birthday
next_birthday = datetime.date(today.year, birthdate.month, birthdate.day)
if next_birthday < today:
    next_birthday = datetime.date(today.year+1, birthdate.month, birthdate.day)
days_until_birthday = (next_birthday - today).days

# Print results
print(f"You were born on a {day_of_week}.")
print(f"You are currently {age} years old.")
print(f"There are {days_until_birthday} days until your next birthday.")

# This optimized code makes use of the strftime function to format the day of the week and removes the need for the days_of_week list.
# It also simplifies the age calculation and uses f-strings for more concise output.

# Additionally, it's worth noting that the original version of the code used datetime.datetime objects,
# which include both a date and a time.
# Since we only need the date for this program, using the date() method to extract the date from the datetime object is more efficient.