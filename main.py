#Rock Paper Scissors Game 
print("Welcome to the Rock Paper Scissors Game!!\n")

import random

# Let Rock = 0
# Let Paper = 1
# Let Scissors = 2

# Associating the numbers with the choices
val = {0: "Rock", 1: "Paper", 2: "Scissors"}

while True:
    # Selecting if the player is playing with the Computer or with another Player
    mode = int(input("Select the mode:\n1 for Player vs Computer\n2 for Player vs Player\n\nEnter your choice: "))

    if mode ==1:

        print("\nYou have selected Player vs Computer mode.\n")

        # Generating a random Computer Choice
        rnum = random.choice([0,1,2])

        # Taking the User Input
        user = int(input("Options:\n0 for Rock\n1 for Paper\n2 for Scissors\n\nEnter your choice: "))

        # Displaying Choices
        print(f"\nYou chose: {val[user]}\nComputer chose: {val[rnum]}")

        # Logic for the Game
        if user == rnum:
            print("Its a Draw!")
        else:
            if user == 0 and rnum == 2:
                print("You Win!!")
            elif user == 1 and rnum == 0:
                print("You Win!!")
            elif user == 2 and rnum == 1:
                print("You Win!!")
            else:
                print("Computer Wins!!")

    elif mode == 2:
        
        print("\nYou have selected Player vs Player mode.\n")

        # Taking user inputs
        print("Options:\n0 for Rock\n1 for Paper\n2 for Scissors\n\n")
        u1 = int(input("Enter Player 1 choice: "))
        u2 = int(input("Enter Player 2 choice: "))

        # Displaying Choices
        print(f"\nPlayer 1 chose: {val[u1]}\nPlayer 2 chose: {val[u2]}")

        # Logic for the Game
        if u1 == u2:
            print("Its a Draw!")
        else:
            if u1 == 0 and u2 == 2:
                print("Player 1 Wins!!")
            elif u1 == 1 and u2 == 0:
                print("Player 1 Wins!!")
            elif u1 == 2 and u2 == 1:
                print("Player 1 Wins!!")
            else:
                print("Player 2 Wins!!")
    else:
        print("Invalid Input!! Please select a valid mode.")

    # Logic for play agian   
    pg = input("\nWant to play again(y/n):")
    if pg.lower() != "y":
        print("Thanks for playing!!")
        break
       
    


