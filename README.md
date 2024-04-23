A list of my Python Projects

Guess the Word Game

This Python program implements a simple "Guess the Word" game where players attempt to guess a randomly chosen word from a predefined list.
Features

    Randomly selects a word from a list of predefined words.
    Allows players to guess individual letters or the entire word.
    Provides feedback on guessed letters and remaining attempts.
    Notifies players of the outcome (win or loss) at the end of the game.

How to Play

    Run the Python script guess_the_word.py.
    Follow the prompts to guess letters or the full word.
    Keep guessing until you either correctly guess the word, run out of attempts, or choose to quit the game.

Code Explanation

    word_list: A list containing words from which the game selects a random word to be guessed.
    choose_word(): Selects a random word from the word_list.
    display_word(word, guessed_letters): Displays the word with underscores for unguessed letters, based on the letters guessed so far.
    guess_letter_or_word(): Prompts the user to guess a letter or the full word and validates the input.
    play_game(): The main function to play the game, which handles game logic, user input, and feedback.
