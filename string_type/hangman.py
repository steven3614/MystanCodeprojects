"""
File: hangman.py
Name: 張文銓
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This function is a game that let user guess a word by knowing the length of the word.
    user will have 7 chances to guess.
    """
    hangman()


def hangman():
    dash = ""  # dash will show the blank for the user.
    ans = random_word()  # ans is the word that user need to guess.
    turn = 7  # every time the user has 7 chances to make guess it wrong.
    for i in range(len(ans)):
        dash += "-"
    while True:
        print("The word looks like: " + dash)
        print("You have " + str(turn) + " guesses left.")
        guess = input("Your guess: ")
        new_guess = ""  # make a new string to let the lower case change to upper case.
        while len(guess) != 1 or not guess.isalpha():  # cases that the input is not available to test.
            print("illegal format.")
            guess = input("Your guess: ")
        if guess.islower:
            new_guess += guess.upper()
        if ans.find(new_guess) == -1:  # if the letter user guessed is not in the word
            print("There is no " + new_guess + "'s in the word.")
            turn = turn - 1
        if turn == 0:  # when there is no more chance to guess.
            print("You are completely hung : (")
            print("The word was: " + ans)
            break
        found = False
        for i in range(len(ans)):
            if new_guess == ans[i]:
                found = True
                dash = dash[:i] + new_guess + dash[i + 1:]
        if found:  # preventing the function by printing "you are correct!" more than one time
            print("You are correct!")

        if dash.find("-") == -1:  # the case that user guess the word.
            print("You win!!")
            print("The word was: " + ans)
            break


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
