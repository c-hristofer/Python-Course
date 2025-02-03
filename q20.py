# Write a program that checks if a person is eligible to vote based on the following conditions:
# 1. The person must be at least 18 years old
# 2. The person must be a citizen of the country
# 3. The program should prompt the user for their age and citizenship status (Yes/No). Based on these inputs, the program should output:
#   A. "Elibible to vote" if the person is 18 or older and is a citizen
#   B. "Not Elibible to vote" otherwise


print()
while True:
    try:
        # Prompt user for age
        age = int(input("Enter your age:\n> "))
        if age > 0:
            break
        else:
            print("\nInvalid input. Please enter a non-zero integer.")
    except ValueError:
        print("\nInvalid input. Please enter a non-zero integer.")

print()
while True:
    try:
        # 3. The program should prompt the user for their age and citizenship status (Yes/No). Based on these inputs
        citizen = input("Are you a Citizen of this country? Enter 'Yes' or 'No'\n> ").upper()
        if citizen == "YES" or citizen == "NO":
            break
        else:
            print("\nInvalid input.")
    except ValueError:
        print("\nInvalid input.")

# 1. The person must be at least 18 years old
# 2. The person must be a citizen of the country
if age >= 18 and citizen == 'YES':
    # A. "Elibible to vote" if the person is 18 or older and is a citizen
    print("\nEligible to vote\n")
else:
    # B. "Not Elibible to vote" otherwise
    print("\nNot Eligible to Vote")