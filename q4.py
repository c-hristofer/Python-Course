import math

# Get a positive number input from user, repeat prompt if incorrect inputis received
def get_input():
    while True:
        try:
            number = float(input("Enter a positive value\n> "))
            if number > 0:
                return number  # Return only if it's a valid positive number
            else:
                print("\nYou inputted a non-positive number. Try again.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

# Calculate square root of the number
def calculate(number):
    sqrt = math.sqrt(number)
    print(f"The square root of {number} is {sqrt}")

print("\n")

# Call functions
number = get_input()
calculate(number)