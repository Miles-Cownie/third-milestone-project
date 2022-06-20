'''
This code imports the random module to make the word
selected from the word lists random.
It also imports the word lists from the other two python files
(words_easy.py and words_hard.py).
'''
import random
from words_easy import easy_word_list
from words_hard import hard_word_list


def choose_name():
    """
    This code prompts the user to input their name.
    Names not made of letters will flag error to user and
    they will be prompt to submit a valid name.
    """
    name = input("Please enter your name!\n")
    if name.isalpha():
        print(f"Hello, {name.capitalize()}, Let's get started!")
        return name
    else:
        print("Please enter a valid name using only letters. \n")
        choose_name()


def choose_difficulty(name):
    """
    This code prompts the user to input a difficulty choice.
    The user's choice will call a random word from the chosen
    word list.
    """
    print(f"{name.capitalize()}, Please select a difficulty:")
    difficulty = input("E for Easy or H for Hard\n")

    if difficulty.upper() == 'E':
        hidden_word = random.choice(easy_word_list)
        return hidden_word
    elif difficulty.upper() == 'H':
        hidden_word = random.choice(hard_word_list)
        return hidden_word
    else:
        print("Invalid Input.\nInput must match the above options.")
        choose_difficulty(name)


def calculate_attempts(hidden_word):
    """
    Calculates the number of attempts for the provided word
    """
    attempts = len(hidden_word) + 2
    return attempts


def main():
    """
    The primary function to run the hangman game.
    """
    user_name = choose_name()
    word_to_guess = choose_difficulty(user_name)
    attempts = calculate_attempts(word_to_guess)
    print(attempts)


main()
