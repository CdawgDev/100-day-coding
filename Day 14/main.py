#Break down the problem
#Make todo list
# A way to ask the user to input either A or B
# Function that loops through the data and returns comparision A and B
# Function that handles the logic for if the user is right or wrong
# Function that stores the previous answers and grabs a new comparison for the user to compare against (Should remove already guessed person from the list)
# Function that keeps the score of the user and displays the score after the logo
# Function that Randomly Grabs a new person from the data

from art import logo,vs
from game_data import data
import random
import os
clear = lambda: os.system('cls')


def grab_user_input():
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    return answer

def get_new_person(valid_persons): # Function that Randomly Grabs a new person from the data
    """Returns a person from the dictionary at random"""
    valid_people = valid_persons
    length_of_list = len(valid_people) - 1
    random_person = valid_people[random.randrange(length_of_list)] # This might return an item outside the range of the list
    return random_person

def get_player_score(prev_score):
    clear()
    score = prev_score + 1
    print(f"{logo}\nYou're right! Current score: {score}")
    return score
def display_end_game(score):
    clear()
    print(f"{logo}\nSorry, that's wrong. Final score: {score}")

def check_player_guess(person_a, person_b, guess):
    a_followers = person_a["follower_count"]
    b_followers = person_b["follower_count"]
    person_to_return = []
    if a_followers > b_followers:
        greater_followers = "a"
        person_to_return.append(person_a)
    else:
        greater_followers = "b"
        person_to_return.append(person_b)
    if guess == greater_followers:
        return [True,person_to_return[0]]
    else:
        return [False,person_to_return[0]]

def display_person(person,comparison_letter):
    comparison_letter = comparison_letter.upper()
    name = person["name"]
    description = person["description"]
    country = person["country"]
    print(f"Compare {comparison_letter}: {name}, a {description}, from {country}.")

def start_game():
    game_running = True
    start_score = 0
    clear()
    print(logo)
    person_dictionary = data

    person_a = get_new_person(person_dictionary)
    display_person(person_a,"a")
    person_dictionary.remove(person_a)
    print(vs)
    person_b = get_new_person(person_dictionary)
    display_person(person_b,"b")
    person_dictionary.remove(person_b)

    while game_running:
        user_guess = grab_user_input()
        result = check_player_guess(person_a, person_b, user_guess)

        if result[0]:
            start_score = get_player_score(start_score)
            person_a = result[1]
            display_person(person_a,"a")
            print(vs)
            person_b = get_new_person(person_dictionary)
            display_person(person_b,"b")
            person_dictionary.remove(person_b)

        else:
            display_end_game(start_score)
            game_running = False





start_game()