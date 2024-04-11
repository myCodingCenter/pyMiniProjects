import random

options = ('rock','paper','scissors')
computerScore = 0
playerScore = 0
con = 0
while con!=10:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("rock, paper or scissors? ").lower()
    if player == computer:
        print(f"Computer = {computer}")
        print(f"Player = {player}")
        print("Tie!!")
    if player == 'rock':
        if computer == 'paper':
            print(f"Computer = {computer}")
            print(f"Player = {player}")
            print("The Winner is computer")
            computerScore=computerScore+1

        elif computer == 'scissors':
            print(f"Computer = {computer}")
            print(f"Player = {player}")
            print("The Winner is player")
            playerScore = playerScore+1
    elif player == 'paper':
        if computer == 'scissors':
            print(f"Computer = {computer}")
            print(f"Player = {player}")
            print("The Winner is computer")
            computerScore=computerScore+1
        elif computer == 'rock':
            print(f"Computer = {computer}")
            print(f"Player = {player}")
            print("The Winner is player")
            playerScore = playerScore+1
    if player == 'scissors':
        if computer == 'rock':
            print(f"Computer = {computer}")
            print(f"Player = {player}")
            print("The Winner is computer")
            computerScore=computerScore+1
        elif computer == 'paper':
            print(f"Computer = {computer}")
            print(f"Player = {player}")
            print("The Winner is player")
            playerScore = playerScore+1
    con =con +1
    # yesNoList = ['yes','no']
    # playAgain = None
    # while playAgain not in yesNoList:
    #     playAgain = input("do you want to paly again(yes/no)? ").strip().lower()
    # if playAgain != 'yes':
    #     break
print(f"Computer Score = {computerScore}")
print(f"Player Score = {playerScore}")
if playerScore > computerScore:
    print("The winner is Player!")
elif playerScore == computerScore:
    print("Tie")
else:
    print("The winner is computer!")

