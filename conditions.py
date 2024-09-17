

number = 7  

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")





# Function to check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")




# age = int(input("Please enter your age: "))

# Check divisibility
divisible_by_2 = (age % 2 == 0)
divisible_by_3 = (age % 3 == 0)

# Determine the output based on the divisibility checks
if divisible_by_2 and divisible_by_3:
    print(f"Your age {age} is divisible by both 2 and 3.")
elif divisible_by_2:
    print(f"Your age {age} is divisible by 2 but not by 3.")
elif divisible_by_3:
    print(f"Your age {age} is divisible by 3 but not by 2.")
else:
    print(f"Your age {age} is not divisible by either 2 or 3.")



# Set age and nationality values
age = 20  # Replace with the desired age
nationality = "yes"  # Replace with "yes" or "no"

# Check if the age is 18 or above
if age >= 18:
    # Check if they have a nationality of "Pakistani"
    if nationality.strip().lower() == "yes":
        print("You are eligible to vote.")
    else:
        print("Please obtain a valid ID to vote.")
else:
    print("You must be at least 18 years old to vote.")
    
     



def days_in_month(month, year):
    # List of days in each month for a non-leap year
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if it's a leap year and the month is February
    if is_leap_year(year) and month == 2:
        return 29  # February has 29 days in a leap year

    if 1 <= month <= 12:
        return days[month - 1]
    else:
        return "Invalid month"

def is_leap_year(year):
    # Leap year is divisible by 4, but not divisible by 100 unless divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

