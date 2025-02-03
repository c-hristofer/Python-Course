# Write a program that calculates the factorial of a number using a while loop. The program should:
# 1. Prompt the user for a non-negative number
# 2. Calculate the factorial of the number. Be sure to use a while loop to calculate the product
# 3. Display the result


# Ensure correct value type
while True:
    try:
        # 1. Promput user for a non-negative number
        number = float(input("\nEnter a non-negative number\n> "))
        if number >= 0:
            break
        else:
            print("\nInvalid input. Please enter a non-negative number.")
    except ValueError:
        print("\nInvalid input. Please enter a non-negative number.")

factorial = 1

# 2. Calculate the factorial of the number. Be sure to use a while loop to calculate the product
while number > 0:
    factorial *= number
    number -= 1

# 3. Display the result
print(factorial)