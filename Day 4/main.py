#The goal of this project is to create rock paper scissors with ascii art

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock,paper,scissors]
computer_choice = choices[random.randint(0,2)]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user_input > 2:
    print("You chose an invalid number you lose")
else:
    user_choice = choices[user_input]
    print(user_choice)
    print(f"Computer chose:\n{computer_choice}")
    if user_choice == choices[0] and computer_choice == choices[1]: #User Chooses rock. Computer chooses paper.
        print("You Lose")
    elif user_choice == choices[0] and computer_choice == choices[2]: #User Chooses rock. Computer chooses scissors.
        print("You Win")
    elif user_choice == choices[1] and computer_choice == choices[0]: #User Chooses paper. Computer chooses rock.
        print("You Win")
    elif user_choice == choices[1] and computer_choice == choices[2]: #User Chooses paper. Computer chooses scissors.
        print("You Lose")
    elif user_choice == choices[2] and computer_choice == choices[0]: #User Chooses scissors. Computer chooses rock.
        print("You Lose")
    elif user_choice == choices[2] and computer_choice == choices[1]:
        print("You Win")
    else:
        print("You Draw")
