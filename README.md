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



Cannabis Retail Sales Analysis Program
Overview

The Cannabis Retail Sales Analysis Program is a Python script designed to analyze and visualize retail sales data in the cannabis industry. It utilizes the Pandas library for data manipulation and Matplotlib for data visualization.
Purpose

The purpose of this program is to provide insights into the distribution of adult-use and medical marijuana retail sales over a specific time period. By analyzing sales data, stakeholders in the cannabis industry can better understand consumer trends, market dynamics, and the overall performance of retail sales channels.
Functionality

The program performs the following tasks:

    Data Loading: It loads sales data from a CSV file named "Cannabis_Retail_Sales_by_Week_Ending.csv".

    Data Analysis: It generates histograms to visualize the distribution of adult-use retail sales and medical marijuana retail sales separately.

    Visualization: It uses Matplotlib to create histograms that display the frequency distribution of sales amounts for both adult-use and medical marijuana products.

Usage

To use the program:

    Clone or download this repository to your local machine.

    Ensure you have Python installed, along with the necessary libraries (Pandas and Matplotlib). You can install them using pip:

    bash

pip install pandas matplotlib

Place the CSV file containing the sales data in the same directory as the Python script.

Run the Python script sales_analysis.py:

bash

python sales_analysis.py

The program will generate histograms displaying the distribution of adult-use and medical marijuana retail sales, providing insights into sales trends.
