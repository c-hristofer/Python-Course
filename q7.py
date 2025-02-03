
# Prompt user for a string of characters, then output each character in the string on a different line
string = input("\n Enter a string of characters\n> ")

for i in range(len(string)):
    character = string[i]
    print(f"{character}")