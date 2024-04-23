import random

#List of words
word_list = ['unknown', 'vaporize','crazy','random','careful', 'funny','abruptly', 'apple', 'agile', 'easy']

def choose_word():
    #Selects a random word from the word_list
    return random.choice(word_list)

def display_word(word, guessed_letters):
    #Displays the word with underscores for unguessed letters
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def guess_letter_or_word():
    while True:
        guess = input("Guess a letter or the word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        elif guess.isalpha() and len(guess) > 1:
            return guess
            print("Please enter a single letter or a word")
def play_game():
    #Main function to play the game.
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Guess the Word Game!")
    print("You have {} attempts to guess the word.".format(attempts))

    while attempts > 0:
        print("\nWord:", display_word(word_to_guess, guessed_letters))

        guess = guess_letter_or_word()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
                if set(word_to_guess) == set(guessed_letters):
                    print("\nCongratulations! You guessed the word:", word_to_guess)
                    break
            else:
                print("Wrong guess!")
                attempts -= 1
                print("Attempts left:", attempts)
                if attempts == 0:
                    print("\nSorry, you're out of attempts. The word was:", word_to_guess)
                    break
        else:
            if guess == word_to_guess:
                print("\nCongratulations! You guessed the word:", word_to_guess)
                break
            else:
                print("\nWrong guess! Try again.")
                attempts -= 1
                print("Attempts left:", attempts)
                if attempts == 0:
                    print("\nSorry, you're out of attempts. The word was:", word_to_guess)
                    break

play_game()