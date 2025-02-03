
# Take input from the user and convert it into a list of integers
numbers = [list(map(int, input("Enter numbers separated by spaces: ").split()))]

# List comprehension to filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Print the result
print("Even numbers:", even_numbers)