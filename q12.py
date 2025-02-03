
# Get lead, make sure it is a valid input
# 1. Take Input for the number of points the team is ahead
# 2. Subtract 3 from the score
# 3. Add 0.5 if the leading team has the ball, subtract 0.5 if the trailing team has the ball
# 4. Square the result
# 5. If the result is greater than the number of seconds left in the game, print "Lead is Safe". Otherwise, print "Lead is Not Safe"


# Ensure correct value type
while True:
    try:
        # 1. Take Input for the number of points the team is ahead
        lead = int(input("\nHow many points is the team ahead by\n> "))
        if lead >= 0:
            break
        else:
                print("\nInvalid input. Please enter a positive integer.")
    except ValueError:
        print("\nInvalid input. Please enter a positive integer.")

# 2. Subtract 3 from the score
lead -= 3

# Ensure correct value type
while True:
    try:
        # Determine who has the ball
        possession = input("\nDoes the leading team have the ball? Enter Y or N\n> ").upper()
        if possession == "Y" or possession == "N":
            break
        else:
                print("\nInvalid input. Please enter 'Y' or 'N'.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# 3. Add 0.5 if the leading team has the ball, subtract 0.5 if the trailing team has the ball
if possession == 'Y':
    lead += 0.5
else:
    lead -=0.5

# 4. Square the result
lead_squared = lead * lead


while True:
    try:
        # Determine how many seconds are left in the game
        seconds_left = int(input("\nHow many seconds are left in the game?\n> "))
        if seconds_left >= 0:
            break
        else:
                print("\nInvalid input. Please enter a positive integer.")
    except ValueError:
        print("\nInvalid input. Please enter a positive integer.")

# 5. If the result is greater than the number of seconds left in the game, print "Lead is Safe". Otherwise, print "Lead is Not Safe"
if lead_squared > seconds_left:
    print("\nLead is Safe\n")
else:
    print("\nLead is Not Safe\n")