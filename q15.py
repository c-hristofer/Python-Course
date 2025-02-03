# Write a program that takes 2 integers as inputs and swaps their values without using a temporary variable. You can use multiple assignments for this

print()
while True:
    try:
        # Take an integer as input
        integer1 = int(input("Enter the first integer:\n> "))
        
        # Take an integer as input
        integer2 = int(input("\nEnter the second integer:\n> "))

        break

    except ValueError:
        print("\nInvalid input.")

# Swap values without using a temporary value
integer1, integer2 = integer2, integer1

print(f"\nAfter swapping:\nInteger 1 = {integer1}\nInteger 2 = {integer2}\n")
