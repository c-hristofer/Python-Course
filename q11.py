
# Take the user's age as an input, then output "Adult," "Teenager," "Child,", or "Baby" depending on their age

while True:
    try:
        age = float(input("\nEnter your age\n> "))
        if age >=0:
            if age >= 18:
                print("Adult")
            elif age >= 13 and age <= 17:
                print("Teenager")
            elif age >= 3 and age <= 12:
                print("Child")
            else:
                print("Baby")
        else:
            print("\nInvalid Input, please enter a positive number")
    except ValueError:
        print("\nInvalid Input, please enter a positive number")