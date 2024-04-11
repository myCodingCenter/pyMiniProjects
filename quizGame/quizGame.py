from questions import questions
import random
import string

options = ['A','B','C','D']
# print(len(questions))

def askQuestion():
    question = random.choice(questions)
    print(f"{question.get('question')}\nA. {question.get('A')}\nB. {question.get('B')}\nC. {question.get('C')}\nD. {question.get('D')}")
    return question.get('answer')


# Creating main Function
def main():
    while True:
        answer = askQuestion()
        userAnswer = input("Which option? ").upper()
        while userAnswer not in options:
            print("Please choose a valid option!")
            userAnswer = input("Which option? ").upper()
        if answer == userAnswer:
            print(f"Correct Option! Correct option is {answer}")
        elif answer != userAnswer:
            print(f"Incorrect Option! Correct option is {answer}")
        playAgain = input("do you want to paly again(y/n): ").strip().lower()
        if playAgain != 'y':
            break
# Calling main function
main()
