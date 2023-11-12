#Step 1
# import random
# word_list = ["ardvark", "baboon", "camel"]
# choosen_word = random.choice(word_list)
# guess = input("Guess a letter: ").lower()
# for letter in choosen_word:
#     if guess == letter:
#         print("Right")
#     else:
#         print("Wrong")
#Todo 1 Randoml;y choose a word from the word_list_ and assign it to a variable called choosen_word
#Todo 2 Ask the user to a guess a letter and assign their answer to a variable called guess. Make guess lowercase
#Todo3 Check if the ltter the user guessed (guess) is one of the letters in the choosen word

#Step 2

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #TODO-1: - Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

# display = []
# for letters in chosen_word:
#     display.append("_")
# print(display)
# guess = input("Guess a letter: ").lower()

# #TODO-2: - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# for x in range(len(chosen_word)):
#     if chosen_word[x] == guess:
#         display[x] = guess
#         print("Right")
#     else:
#         print("Wrong")
# print(display)
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

#Step 3

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# end_of_game = False

# def guessLetter():
#     guess = input("Guess a letter: ").lower()

#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#     print(display)

# while not end_of_game:
#     if "_" not in display:
#         end_of_game = True
#         print("You Win")
#     else:
#         guessLetter()

#Step 4

# import random

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# lives = 6
# #TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# #Set 'lives' to equal 6.

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#     if guess not in chosen_word:
#         lives -= 1
#         print(stages[lives])
#         if lives == 0:
#             end_of_game = True
#             print("You Lose. Better Luck Next Time Buddy")
#     #TODO-2: - If guess is not a letter in the chosen_word,
#     #Then reduce 'lives' by 1.
#     #If lives goes down to 0 then the game should stop and it should print "You lose."

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

#Step 5

import random
import hangman_art
import hangman_words
import os

clear = lambda: os.system('cls')
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
#Testing code

#Create blanks
display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  clear()
  if guess in display:
    print(f"You have already guessed {guess} Try another letter")
    guess
  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  #Check if user is wrong.
  if guess not in chosen_word:
    print(f"{guess} is not in the chosen word. You lose a live")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
  #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print("You win.")

  print(hangman_art.stages[lives])
