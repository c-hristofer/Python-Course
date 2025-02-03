
# Write a program that takes a list of numbers, then:
# 1. Prints the second and fourth elements in the list
# 2. Adds 60 to the list
# 3. Removes the first element
# 4. Prints the modified list

numbers = [10, 20, 30, 40, 50]

# 1. Prints the second and fourth elements in the list
print (f"\nSecond element of list called numbers is: {numbers[1]}")
print (f"Fourth element of list called numbers is: {numbers[3]}\n")

# 2. Adds 60 to the list
numbers.append(60)

# 3. Removes the first element
numbers.pop(0)

# 4. Prints the modified list
print (f"{numbers}")