# Write a program that Prints the first n numbers of the Fibonacci sequence, where n is provided by the user. The program should:
# 1. Use a for loop to generate the Fibonacci sequence
# 2. Print the sequence up to the n-th number

print()
while True:
    try:
        # Prompt user
        n = int(input("How many values into the Fibonacci Sequense should I print?\n> "))
        if n > 0:
            break
        else:
            print("\nInvalid input. Please enter a non-zero integer.")
    except ValueError:
        print("\nInvalid input. Please enter a non-zero integer.")


a = 0
b = 1
print(a)

# 1. Use a for loop to generate the Fibonacci sequence
for i in range(n-1):
    # 2. Print the sequence up to the n-th number
    print(b)
    temp = a
    a = b
    b = temp + b