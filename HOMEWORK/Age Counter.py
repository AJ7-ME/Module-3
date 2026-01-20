# Set current year and month manually
current_year = 2026
current_month = 1  # January

try:
    # Get user input and convert to integers
    birth_year = int(input("Enter your birth year (YYYY): "))
    birth_month = int(input("Enter your birth month (1-12): "))

    # Check valid month range
    if birth_month < 1 or birth_month > 12:
        raise ValueError("Month out of range")
    age = current_year - birth_year
    if birth_month > current_month:
        age -= 1
    if age < 0:
        raise ValueError("Negative age")
    if age % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"You are {age} years old.")
    print(f"Your age is {even_or_odd}.")
except ValueError:
    print("Invalid input! Please enter valid numbers only.")
