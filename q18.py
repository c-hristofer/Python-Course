# Write a program to check if a number is prime. The program should:
# 1. Take an integer as an input
# 2. Print "Not Prime" if the number isn't prime
# 3. Print "Prime" if the number prime

import math

# Input validation
while True:
    try:
        # 1. Take an integer as an input
        integer = int(input("\nEnter an integer:\n> "))
        if integer >= 1:
            break
        else:
            print("\nInvalid input. Please enter a positive integer.")
    except ValueError:
        print("\nInvalid input. Please enter a positive integer.")

# Handle special cases
if integer == 1:
    print("1 is neither prime nor composite.")
elif integer == 2:
    print("2 is a prime number.")
else:
    flag = False  # Assume the number is prime

    # Check divisibility from 2 to sqrt(integer)
    for i in range(2, int(math.sqrt(integer)) + 1):
        if integer % i == 0:
            flag = True
            break  # No need to check further, number is not prime

    if flag:
        print("\nNumber is Not Prime\n")
    else:
        print("\nNumber is Prime\n")