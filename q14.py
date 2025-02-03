# Write a program that takes an integer as an input and applies the Collatz Conjecture algorithm to the number with these steps:
# 1. If the number is even, divide it by 2
# 2. If the number is odd, multiply it by 3 and add 1
# 3. Continue applying this rule until the number becomes 1
# 4. Print the sequence of numbers generated


while True:
    try:
        # Take a non-zero integer as input
        integer = int(input("\nEnter an integer:\n> "))
        if integer >= 1:
            break
        else:
            print("\nInvalid input. Please enter a positive integer.")
    except ValueError:
        print("\nInvalid input. Please enter a positive integer.")
print ("")

# 3. Continue applying this rule until the number becomes 1
while integer != 1:
    # 1. If the number is even, divide it by 2
    if integer % 2 == 0:
        integer/=2
    # 2. If the number is odd, multiply it by 3 and add 1
    else:
        integer = integer * 3 + 1
    # 4. Print the sequence of numbers generated
    print (integer)
print ("")