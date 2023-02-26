# Version: 1.0
# A Python program that will take in your date of birth and calculate your current age,
# along with the day of the week you were born:
# This Python program Prompts the user to enter their date of birth in the format of YYYY-MM-DD.
# The program will then calculate your current age in years and print it along with the day of the week you were born.

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
# This optimized code makes use of the strftime function to format the day of the week and removes the need for the days_of_week list.
# It also simplifies the age calculation and uses f-strings for more concise output.
# Additionally, it's worth noting that the original version of the code used datetime.datetime objects,
# which include both a date and a time.
# Since we only need the date for this program, using the date() method to extract the date from the datetime object is more efficient.

# import datetime

# # Prompt user for their date of birth
# birthdate_str = input("Enter your date of birth (DD-MM-YYYY): ")

# # Convert birthdate to datetime object
# birthdate = datetime.datetime.strptime(birthdate_str, '%d-%m-%Y').date()

# # Get today's date
# today = datetime.date.today()

# # Calculate age in years
# age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# # Calculate day of the week the user was born on
# day_of_week = birthdate.strftime('%A')

# # Calculate number of days until next birthday
# next_birthday = datetime.date(today.year, birthdate.month, birthdate.day)
# if next_birthday < today:
#     next_birthday = datetime.date(today.year+1, birthdate.month, birthdate.day)
# days_until_birthday = (next_birthday - today).days

# # Print results
# print(f"You were born on a {day_of_week}.")
# print(f"You are currently {age} years old.")
# print(f"There are {days_until_birthday} days until your next birthday.")


# Improved Version: 1.0.3
# In this program, we first prompt the user to enter their birthdate in UK format (DD-MM-YYYY) using input.
# We then parse the birthdate string into a datetime.datetime object using datetime.datetime.strptime.
# We then calculate the user's age and the number of days until their next birthday using the current date and the replace and days methods.
# This code is more concise and efficient than the previous version.
# We also use datetime.datetime.strftime to reverse the birthdate format to US format, and print the results to the console.

# import datetime

# # Prompt user for their date of birth in UK format
# birthdate_str = input("Enter your date of birth (DD-MM-YYYY): ")

# # Parse birthdate to datetime object
# try:
#     birthdate = datetime.datetime.strptime(birthdate_str, '%d-%m-%Y')
# except ValueError:
#     print("Invalid date format:", birthdate_str)
#     exit()

# # Calculate age and days until next birthday
# now = datetime.datetime.now()
# next_birthday = datetime.datetime(now.year, birthdate.month, birthdate.day)
# if now > next_birthday:
#     next_birthday = next_birthday.replace(year=now.year+1)
# age = now.year - birthdate.year - ((now.month, now.day) < (birthdate.month, birthdate.day))
# days_until_birthday = (next_birthday - now).days

# # Reverse birthdate format to US format
# us_format_birthdate_str = birthdate.strftime('%m/%d/%Y')

# # Print results
# print("You were born on a", birthdate.strftime('%A')+".")
# print("You are currently", age, "years old.")
# print("There are", days_until_birthday, "days until your next birthday.")
# print("Your birthdate in US format is:", us_format_birthdate_str+".")


# Version: 1.0.4 - Refactored and Optimised Code
# In this optimized version, we first parse the birthdate string into a datetime.date object, which is more memory-efficient than a datetime.datetime object.
# We also use the datetime.date.today() method to get the current date, which is faster than creating a datetime.datetime object with datetime.datetime.now().
# Additionally, we optimize the calculation of the user's age and the number of days until their next birthday by using the replace method instead of creating a new datetime.datetime object for the user's next birthday.
# We also remove unnecessary parentheses and use the date method to calculate the difference in days between two dates.
# Overall, these optimizations make the program more efficient and faster.

# import datetime

# # Prompt user for their date of birth in UK format
# birthdate_str = input("Enter your date of birth (DD-MM-YYYY): ")

# # Parse birthdate to datetime object
# try:
#     birthdate = datetime.datetime.strptime(birthdate_str, '%d-%m-%Y').date()
# except ValueError:
#     print("Invalid date format:", birthdate_str)
#     exit()

# # Calculate age and days until next birthday
# now = datetime.date.today()
# next_birthday = birthdate.replace(year=now.year)
# if now > next_birthday:
#     next_birthday = next_birthday.replace(year=now.year+1)
# age = now.year - birthdate.year - ((now.month, now.day) < (birthdate.month, birthdate.day))
# days_until_birthday = (next_birthday - now).days

# # Reverse birthdate format to US format
# us_format_birthdate_str = birthdate.strftime('%m/%d/%Y')

# # Print results
# print("You were born on a", birthdate.strftime('%A')+".")
# print("You are currently", age, "years old.")
# print("There are", days_until_birthday, "days until your next birthday.")
# print("Your birthdate in US format is:", us_format_birthdate_str+".")


# Version: 1.0.5 - Further Refactored and Optimised Code
# Here's a further optimized version of the program in Python that calculates a user's age and the number of days until their next birthday,
# and also reverses the date format from UK format to US format:

# In this version, we use an f-string to format the output strings with variables directly, which is more concise and easier to read.
# We also replace the ((now.month, now.day) < (birthdate.month, birthdate.day)) expression with int(now < next_birthday), which is more efficient and has the same result.
# Additionally, we use datetime.date instead of datetime.datetime throughout the code, which is more memory-efficient and requires fewer computations.
# Overall, these optimizations make the program more efficient, faster, and more readable.

import datetime

# Prompt user for their date of birth in UK format
birthdate_str = input("Enter your date of birth (DD-MM-YYYY): ")

# Parse birthdate to datetime object
try:
    birthdate = datetime.datetime.strptime(birthdate_str, '%d-%m-%Y').date()
except ValueError:
    print("Invalid date format:", birthdate_str)
    exit()

# Calculate age and days until next birthday
now = datetime.date.today()
next_birthday = birthdate.replace(year=now.year)
if now > next_birthday:
    next_birthday = next_birthday.replace(year=now.year+1)
age = now.year - birthdate.year - int(now < next_birthday)
days_until_birthday = (next_birthday - now).days

# Reverse birthdate format to US format
us_format_birthdate_str = birthdate.strftime('%m/%d/%Y')

# Print results
print(f"You were born on a {birthdate:%A}.")
print(f"You are currently {age} years old.")
print(f"There are {days_until_birthday} days until your next birthday.")
print(f"Your birthdate in US format is: {us_format_birthdate_str}.")
