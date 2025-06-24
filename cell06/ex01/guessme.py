#!/usr/bin/env python3

#Pradeep Singh Bhatia/Chayapol Ak-kharaviboon/Chatkul Pawboonserm

import random

def guess_the_number():
    print("Welcome to the Guess the Number game!🥵🥵\n")
    print("I've generated a secret number between 1 and 100. You have 5 guesses🤫.\n")

    secret = random.randint(1, 100)
    attempts = 5
    low = 1
    high = 100

    while attempts > 0:
        print(f"Attempts left: {attempts}")
        try:
            guess = int(input("Enter your guess😏😏: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.\n")
            attempts -= 1
            continue

        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.\n")
            continue

        if guess == secret:
            print("Congratulations! You guessed the correct number!😈😈😈\n")
            return
        elif guess > secret:
            high = guess - 1
        else:
            low = guess + 1

        print(f"Your guess is not correctv🤨🤨 The secret number is between {low} and {high}.\n")
        attempts -= 1

    print(f"Game over!🤯🤯 You've run out of guesses. The secret number was {secret}.\n")

if __name__ == "__main__":
    guess_the_number()