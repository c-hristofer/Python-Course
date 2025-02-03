
def reverse_string(word):
    reversed_word = ""  # Initialize as an empty string
    for letter in range(len(word) - 1, -1, -1):  # Iterate backwards
        reversed_word += word[letter]  # Append characters in reverse order
    return reversed_word  # Return the reversed string

print(reverse_string("Python"))