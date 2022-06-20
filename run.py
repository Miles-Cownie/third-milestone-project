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
    name = input("Please enter your name!\n")
    if name.isalpha():
        print(f"Hello, {name.capitalize()}, Let's get started!")
    else:
        print("Please enter a valid name using only letters. \n")
        choose_name()


def main():
    choose_name()

main()