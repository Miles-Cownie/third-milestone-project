'''
This code imports the random module to make the word
selected from the word lists random.
It also imports the word lists from the other two python files
(words_easy.py and words_hard.py).
'''
import random
from words_easy import easy_word_list
from words_hard import hard_word_list


def introduction():
    """
    This code provides instructions for the user
    at the start of the hangman game.
    """
    intro = """Welcome to Hangman!
The aim of the game is to guess the secret
word. You can guess either a single letter
or the entire word. The game ends when you
guess the secret word correctly or run out
of attempts to guess!\n"""
    print(intro)


def choose_name():
    """
    This code prompts the user to input their name.
    Names not made of letters will flag error to user and
    they will be prompt to submit a valid name.
    """
    name = input("Please enter your name!\n")
    if name.isalpha():
        print(f"Hello, {name.capitalize()}, let's get started!\n")
    else:
        print("Please enter a valid name using only letters.\n")
        name = input("Please enter your name!\n")
    return name.capitalize()


def choose_difficulty():
    """
    This code prompts the user to input a difficulty choice.
    The user's choice will call a random word from the chosen
    word list.
    """
    print("Please select a difficulty:")
    difficulty = input("E for Easy or H for Hard\n")
    hidden_word = ''

    while hidden_word == '':
        if difficulty.upper() == 'E':
            hidden_word = random.choice(easy_word_list)
        elif difficulty.upper() == 'H':
            hidden_word = random.choice(hard_word_list)
        else:
            print("Invalid Input.\nInput must match the below options.")
            difficulty = input("E for Easy or H for Hard\n")
    return hidden_word


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
    print(f"Alright {name.capitalize()}, let's play!")
    print(f"You have {attempts} attempts left.")
    print("\n")
    print(prompt)

    # While loop to loop until either guessed or run out of tries
    while not guessed and attempts > 0:
        guess = input(f"Please guess a letter or a word {name}.\n")
        # Code to handle when user inputs a letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed that letter:", guess.upper())
            elif guess not in hidden_word:
                print(guess.upper(), "is not in the word")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print(f"Well done {name}, {guess.upper()} is in the word!")
                guessed_letters.append(guess)
                hidden_word_as_list = list(prompt)
                list_index = [i for i,
                              letter in enumerate(hidden_word)
                              if letter == guess]
                for index in list_index:
                    hidden_word_as_list[index] = guess
                prompt = "".join(hidden_word_as_list)
                if "_" not in prompt:
                    guessed = True
        # Code to handle when user inputs a word
        elif len(guess) == len(hidden_word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You have already guessed {guess.capitalize()}.")
            elif guess != hidden_word:
                print(f"{guess.capitalize()} is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                prompt = hidden_word
        # Error message for invalid input
        else:
            print(f"That isn't a valid guess {name}.")
            print("Please guess a letter or a word.")
        print(f"You have {attempts} attempts left.")
        print("\n")
        print(prompt)
    # End of the primary gameplay loop
    if guessed:
        print(f"Well done {name}, you have guessed the word!")
    else:
        print(f"Sorry {name}, you've run out of attempts")
        print(f"The correct answer was {hidden_word}")


def main():
    """
    The primary function to run the hangman game.
    """
    introduction()
    user_name = choose_name()
    word_to_guess = choose_difficulty()
    attempts_left = calculate_attempts(word_to_guess)
    word_prompt = build_prompt(word_to_guess)
    play(user_name, word_to_guess, attempts_left, word_prompt)
    while input("Would you like to play again? Y/N\n").upper() == "Y":
        word_to_guess = choose_difficulty()
        attempts_left = calculate_attempts(word_to_guess)
        word_prompt = build_prompt(word_to_guess)
        play(user_name, word_to_guess, attempts_left, word_prompt)


main()
