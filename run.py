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
    Calculates the number of attempts for the provided hidden word
    """
    attempts_left = len(hidden_word) + 2
    return attempts_left


def build_prompt(hidden_word):
    """
    Builds the user prompt for the provided hidden word
    """
    prompt = "_" * len(hidden_word)
    return prompt


def play(name, hidden_word, attempts, prompt):
    """
    This function contains the main gameplay loop for the hangman game,
    checking the user's input and updating the answer as appropriate
    """
    guessed = False
    guessed_letters = []
    guessed_words = []

    # Starting print for the game
    print(f"Alright {name.capitalize()}, Lets play!")
    print(f"You have {attempts} attempts left.")
    print(prompt)
    print("\n")


def main():
    """
    The primary function to run the hangman game.
    """
    user_name = choose_name()
    word_to_guess = choose_difficulty(user_name)
    attempts_left = calculate_attempts(word_to_guess)
    word_prompt = build_prompt(word_to_guess)
    play(user_name, word_to_guess, attempts_left, word_prompt)

main()
