# Hang that man!
Hang that man! is an alternative of the classic word game 'Hangman'. It is built using Python and runs through the
Code institute mock terminal on Heroku.

# Contents

* [**User Experience**](<#user-experience>)
  * [Wireframes](<#wireframes>)
* [**Existing Features**](<#existing-features>)
  * [User Name Input](<#user-name-input>)
  * [Difficulty Selection](<#difficulty-selection>)
  * [Dynamic Attempts](<#dynamic-attempts>)
  * [Word Prompt](<#word-prompt>)

# User Experience
Users may attempt to guess the hidden word using either letter or word guesses. The game is over when the user guesses correctly
or runs out of attempts.

## Wireframes
Wireframes for Hang that man! were built using [Balsamiq](https:/balsamiq.com).

![Wireframe Game Flow](#)

The first wireframe consists of the initial game flow. The user is prompeted to input a name and select a difficulty. After this, the hidden answer is calculated and the number of attempts the user is given is dynamically calculated. A prompt is then built to store and display the user's correct guesses. Once the starting prompt is created, the main gameplay loop runs until the user either wins or loses. The user is then prompted to play again, returning them back to the start of the game flow.

![Wireframe Game Loop](#)

The second wireframe consists of the primary gameplay loop. The user is prompted to input either a letter or word guess into the console. 
If the user inputs a word it is checked if it matches the hidden word. When the user guesses correctly, the prompt is filled in and the user wins the loop. When the user guesses incorrectly, the number of attempts is decreased by one.
If the user inputs a letter the program checks if the letter is within the hidden word. If the guess is correct, the prompt is updated with the correct guess in the correct place(s). If the guess is incorrect, the number of attempts is decreased by one.
The main gameplay loop ends when the user either correctly guesses the word, using either letters or word guesses, or runs out of attempts.

[Back to top](<#contents>)

# Existing Features

![Opening Game Console](#)

## User Name Input
The user is prompted, during the initial loop of the game, to input a name. The name is checked to ensure it is containing only letters and does not contain symbols or numbers. If the user inputs an invalid name, the program prompts them to enter a new name and explains the valid input for a name. If the user inputs a valid name, the input is stored as the user_name variable.
The user_name variable is used to add a personal touch to the game experience for the user.

## Difficulty Selection
The user is prompted to choose a difficulty, with either easy or hard as options. When the user selects a difficulty, the program selects a random word from the appropriate list and stores it as the word_to_guess variable. If the user inputs an invalid option, an error message is generated and the user is prompted again.

## Dynamic Attempts
Once the user selects a difficulty, the program the sets the number of attempts the user gets for guessing the answers. This is done by calculating the length of the word to guess and adding two. The attempts are displayed to the user throughout the game so they do not need to scroll in order to see their remaining attempts.

## Word Prompt
The word to guess that the difficulty selector created is used to build a prompt to help the user guess. The prompt builder creates a series of underscore lines ("_") equal to the length of the word to guess

# Technologies Used