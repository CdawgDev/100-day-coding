import random
from art import logo
number = random.randrange(1,99)

# print(logo)
# print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
# game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
# attempts = 0


# if game_difficulty == "easy":
#     attempts = 10
# else:
#     attempts = 5

# while attempts > 0:
#     print(f"You have {attempts} attempts remaining to guess the number")
#     guess = int(input("Make a guess: "))
#     if guess > number:
#         print("Too High")
#         print("Guess Again")
#         attempts -= 1
#     elif guess < number:
#         print("Too Low")
#         print("Guess Again")
#         attempts -= 1
#     elif guess == number:
#         print("You found the number")
#         print(f"The number was {number}")
#         print("You win!")
#         attempts = 0

#Solution with Functions::::

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
    attempts = choose_difficulty()

    guess = 0

    while guess != number:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = get_guess()
        attempts = check_guess(guess,number,attempts)
        if attempts == 0:
            print("You ran out of guesses")
            return

def choose_difficulty():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choice == "easy":
        return 10
    else:
        return 5

def check_guess(guess, answer, attempts):
    if guess > answer:
        print("Too High")
        attempts -= 1
        return attempts
    elif guess < answer:
        print("Too Low")
        attempts -= 1
        return attempts
    elif guess == answer:
        print("You found the number")
        print(f"The number was {number}")
        print("You win!")
        attempts = 0
        return attempts
def get_guess():
    print("Guess Again")
    guess = int(input("Make a guess: "))
    return(guess)

game()
