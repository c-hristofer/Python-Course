# Import all necessary modules
import math
import random
from datetime import datetime



# Allows user to keep playing as much as they want
def repeat():
    again = input("\nWould you like to play? Enter Y or N:\n> ").lower()
    if again == "y":
        return again
    else:
        quit()


# Script for problem 1
def problem_1(): 
    # Problem 1: The Great Lakes Are How Big?
    # Solution: Divide the volume of the lakes by the area they will cover. Then convert to meters to make it more easily understandable


    # According to geographyrealm.com, the 48 contiguous states are 8,080,470 km^2
    # Calculate depth of the water

    depth = 22_810/8_080_470 * 1000

    print (f"\n\nGiven: There are 22,810 km^3 of water in the great lakes & the 48 contiguous U.S. States are 8,080,470 km^2. If the water in the great lakes was spread out over the contiguous 48 states, it would be: \n{depth} meters deep\n")

    return()


# Script for problem 2
def problem_2():
    # Problem 2: Where is Voyager 1?
    # Solution: Take input from user to get the days since 09/25/2009. Then, multiple the days times 24 hours and add 16,637,000,000 for miles. Multiply miles times 1.609344 for miles. Divide miles by 92,955,887.6 for AU. For round trip radio communication time in hours, assuming speed of light is 299,792,458 m/s, convert km from previous calulation to meters by multiplying by 1000 then doubling it for the 2 way distance, then divide the 2 way distance by the speed of light, then divide by 3600 seconds to get the time in hours.

    # Test Case: Input is: 1
    # Output is:
    # Distance in miles: 16,637,917,784.00
    # Distance in kilometers: 26,776,133,158.17
    # Distance in Austronomical Units (AU): 178.99
    # Round-trip communication time in hours: 49.62

    # Get user input
    days_since = int(input("\n\nHow many days since 09/25/2009?\n> "))

    # Multiply by 24 and 38,241 for the distance traveled each day, then add 16,637,000,000 because the Voyager 1 had already traveled that far before 09/25/2009
    miles = ((days_since * 24 * 38_241) + 16_637_000_000)
    print (f"\nDistance in miles: {miles:,.2f}")

    # Calculate miles to km
    km = miles * 1.609344
    print (f"Distance in kilometers: {km:,.2f}")

    # Calculate miles to Austronomical Units
    au = miles / 92_955_887.6
    print (f"Distance in Austronomical Units (AU): {au:,.2f}")

    # Convert km to meters, then multiply for 2-way distance, then divide by speed of light in mph for hourly time
    radio_time = (km*1_000*2) / (299_792_458 * 3600)
    print(f"Round-trip communication time in hours: {radio_time:,.2f}\n")


# Script for problem 3
def problem_3():
    # Problem 4: Current Time From Seconds
    # Strategy: Will take an input from user in terms of seconds. Then convert to hours, subract the corresponding amount of seconds from seconds variable, do the same for minutes, then output time in terms of hours:minutes:seconds

    # Test Case: if input is 65000, output is "That time is: 18:03:20"

    # Get input from user
    seconds = (int(input("\n\nEnter an amount of seconds between 1 and 86,400, I will tell you the corrsponding time in terms of hours, minutes, and seconds in a 24 hour format:\n> ")))

    # Calculate hours
    hours = math.floor(seconds/60/60)

    # Subtract hours from seconds
    seconds -= hours*60*60

    # Calculate minutes
    minutes = math.floor(seconds/60)

    # Subtract minute from seconds
    seconds -= minutes*60

    # Print time in terms of hours, minutes, seconds. Always displays 2 digits for each value
    print(f"\nThat time is: {hours:02}:{minutes:02}:{seconds:02}\n")


# Script for problem 4
def problem_4():

    # Problem #4: Date and Time Using Modules
    # Strategy: Import data from module, then convert data to correct format, then print

    # Test Case: if date is January 24, 2025 and time is 11:30pm, output shold be 01/24/2025 23:30:00

    # Load date and time date into now
    now = datetime.now()

    # Format variable date_time as Month/Day/Year Hour:Minure:Second
    now2 = now.strftime("\n\n%m/%d/%Y %H:%M:%S\n\n")

    # Print date and time in correct format
    print(now2)

    # Findings and explanation of module used:
    # datetime has all the information needed within it. I just needed to learn how to import the correct class from the module, then I needed to learn how to format it. Since this is such an intuitive module, it was quite easy to follo the documentation that I found.
    
 
# Script for problem 5
def problem_5():
    # Define constants
    NUM_SQUARES = 64
    WEIGHT_PER_GRAIN_MG = 50
    MG_TO_KG = 1/1_000_000

    # Calculate total number of grains
    total_grains = (pow(2, 30) - 1)

    # Calculate total weight in mg
    total_weight_mg = total_grains * WEIGHT_PER_GRAIN_MG

    # Caclulate total weight in kg
    total_weight_kg = total_weight_mg * MG_TO_KG

    # Output total grains
    print(f"\n\nTotal number of grains on the chessboard: {total_grains:,}")
    # Output total weight
    print(f"Total weight of the grains: {total_weight_kg:,.2f} kg\n\n")
    
    
# Script for problem 6
def problem_6():
    # Problem 6: How Thick Does Paper Folding Get?
    # Strategy: Paper starts at value of 1, so 1 can be ignored. Simply doing 2^30 gives the thickness of paper when folded 30 times in terms of mm. Convert to km and m then output value for user

    # Test Case: None, automatically runs, output is "Paper is 1073km and 741.824m thick if it can be foded in half 30 times"

    # Calculate the thickness of folded paper in hald 30 times in terms of mm
    folded_paper_mm = pow(2, 30)

    # Calculate km
    folded_paper_km = math.floor(folded_paper_mm / 1000000)

    # Subtract km from mm
    folded_paper_mm -= folded_paper_km * 1000000

    # Calculate m
    folded_paper_m = folded_paper_mm/1000

    # Print thickness in terms of km and m
    print (f"\n\nPaper is {folded_paper_km}km and {folded_paper_m}m thick if it can be foded in half 30 times\n\n")
    

# Script for problem 7
def problem_7():
    # Problem 7: Closest Number Game
    # Strategy: Generate a random number using random. Then get an input from each user. Once inputs are received, determine which is further from random_num by using subtraction. Use abs to make sure values are positive. Finally, use else, if, and elif statements to determine who the winner is.abs

    # Test Case: if p1 guesses 1 and p2 guesses 100, the player closest to random_num's value will win

    # Generate random_num
    random_num = random.randint(1, 100)

    # Get Player 1's guess
    p1 = int(input("\n\nWelcome to the Random Number Game!\n\nPlayer 1: Enter a number between 1 and 100:\n> "))

    # Get Player 2's guess
    p2 = int(input("\nPlayer 2: Ener a number between 1 and 100:\n> "))

    # Determine winner using subtraction and abs()
    if abs(p1-random_num) < abs(p2-random_num):
        print(f"\nPlayer 1 Wins!! The secret number is {random_num}\n")
    elif abs(p1-random_num) > abs(p2-random_num):
        print(f"\nPlayer 2 Wins!! The secret number is {random_num}\n")
    else:
        print(f"\nTied! the secret number is {random_num}\n")
    
    
# Script for problem 8
def problem_8():
    # Problem 8: Rock, Paper, Scissors
    # Strategy: Randomly pick for the computer, then prompt user for input. Then, use if, elif, and else statments to output the result of the game.

    # Test Case: if user inputs rock and computer picks 2rock, there is a tie

    # Generate random number 
    computer = random.choice(["ROCK", "PAPER", "SCISSORS"])

    # Get player input
    user = input("\n\nWelcome to Rock, Paper, Scissors! Enter Rock, Paper, or Scissors as your selection:\n> ")
    user = user.upper()

    # ROCK ties with ROCK, PAPER ties with PAPER, SCISSORS ties with SCISSORS
    if user == computer:
        print(f"\n You  both picked {user} and tied!\n")
    # ROCK beats SCISSORS, PAPER beats ROCK, SCISSORS beats PAPER
    elif (user == "ROCK" and computer == "SCISSORS") or (user == "PAPER" and computer == "ROCK") or (user == "SCISSORS" and computer == "PAPER"):
        print(f"\nYou entered {user} and the computer picked {computer}. You Win!!\n")
    # ROCK loses to PAPER, PAPER loses to SCISSORS, SCISSORS loses to ROCK. AKA, all other cases
    else:
        print(f"\nYou entered {user} and the computer picked {computer}. You Lose :(\n")



# Allows user to select what they want to do, repeats as many times as is desired
play = repeat()
while play == "y":
    problem_selection = int(input("\n\nWelcome to Assignment 1 for COP 4045: \
    \nEnter '1' for '1. The Great Lakes are How Big?' \
    \nEnter '2' for '2. Where is Voyager 1?' \
    \nEnter '3' for '3. Current Time from Seconds' \
    \nEnter '4' for '4. Date and Time Using Modules' \
    \nEnter '5' for '5. What is he Invention of Chess Worth?' \
    \nEnter '6' for '6. How Thick Does Paper Folding Get?' \
    \nEnter '7' for '7. Closest Number Game' \
    \nEnter '8' for '8. Rock, Paper, Scissors' \
    \n> "))
    if problem_selection == 1:
        problem_1()
        repeat()
    elif problem_selection == 2:
        problem_2()
        repeat()
    elif problem_selection == 3:
        problem_3()
        repeat()
    elif problem_selection == 4:
        problem_4()
        repeat()
    elif problem_selection == 5:
        problem_5()
        repeat()
    elif problem_selection == 6:
        problem_6()
        repeat()
    elif problem_selection == 7:
        problem_7()
        repeat()
    elif problem_selection == 8:
        problem_8()
        repeat()
    else:
        print ("\n\nInvalid Input:\n")
        repeat()