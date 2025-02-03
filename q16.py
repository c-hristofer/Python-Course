# Write a program that:
# 1. Prompts the user for a number
# 2. Determines if the number is a perfect number
# 3. Prints:
#   A. "Perfect Number" if the number is perfect
#   B. "Not a Perfect Number" if the number is not perfect


# 2. Determines if the number is a perfect number
def perfect_number(num):
    return sum([i for i in range(1, num) if num % i == 0]) == num

while True:
    try:
        # 1. Prompts the user for a number
        number = int(input("\nEnter a number:\n> "))
        break

    except ValueError:
        print("\nInvalid input.")

# 3. Prints:
#   A. "Perfect Number" if the number is perfect
if perfect_number(number) == True:
    print("Perfect Number\n")
#   B. "Not a Perfect Number" if the number is not perfect
else:
    print("Not a Perfect Number\n")
    