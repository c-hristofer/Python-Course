
# Prompt user to input a positive INTEGER until it is received, then tell the user if it is even or odd
while True:
    try:
        integer = input ("\nEnter an integer\n> ")
        if integer.isdigit():
            if float(integer) % 2 == 0:
                print("Even")
            else:
                print("Odd")
        else:
            print("\nInvalid input. Please enter a positive integer.")
    except ValueError:
        print("\nInvalid input. Please enter a positive integer.")