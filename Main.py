#### Stone Paper Scissors game by Micky Guha...

import random
import time

# Mapping values to their respective choices
Values = {1: "Stone", 2: "Paper", 3: "Scissors"}

# Initialize scores
player_score = 0
computer_score = 0

# Enhanced Welcome Message
print("\n----------------------------------------")
print("#### Welcome to Rock Paper Scissors Game! ####")
print("----------------------------------------\n")

# Player name input
player_name = input("Enter your name: ")
print(f"\nHello, {player_name}! Let's start the game.\n")
print("----------------------------------------")
print(f"{1} --> Stone \n{2} --> Paper\n{3} --> Scissors\n")
print("----------------------------------------\n")

while True:
    try:
        # Taking user input
        Your_input = int(input("Enter your choice (1- Stone, 2- Paper, 3- Scissors, 0- Exit): "))
        if Your_input == 0:
            print("\n----------------------------------------")
            print("Thanks for playing!")
            print(f"Final Scores:\n{player_name}: {player_score} | Computer: {computer_score}")
            print("----------------------------------------\n")
            break
        elif Your_input not in [1, 2, 3]:
            print("Invalid input! Please choose between 1, 2, 3, or 0 to exit.")
            continue
        
        # Computer's random choice
        Computer = random.choice([1, 2, 3])
        
        print("\n----------------------------------------")
        print(f"{player_name} chose {Values[Your_input]}.")
        print("Computer is choosing...")
        time.sleep(1)
        print(f"Computer chose {Values[Computer]}.")
        print("----------------------------------------")
        
        # Game logic
        if Computer == Your_input:
            print("It's a Draw!\n")
        elif (Computer == 1 and Your_input == 2) or \
             (Computer == 2 and Your_input == 3) or \
             (Computer == 3 and Your_input == 1):
            print(f"{player_name}, You Win this round!\n")
            player_score += 1
        else:
            print("Computer Wins this round!\n")
            computer_score += 1
        
        # Display current scores
        print("----------------------------------------")
        print(f"Current Scores -> {player_name}: {player_score} | Computer: {computer_score}")
        print("----------------------------------------\n")
        
    except ValueError:
        print("Invalid input! Please enter a number.")