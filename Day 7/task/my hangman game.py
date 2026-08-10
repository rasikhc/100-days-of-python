import random
from hangman_words import word_list
from hangman_art import stages, logo
print("Welcome to my Hangman Game! Guess the word to save the man's life")
print(logo)

Lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

length = len(chosen_word)
print(length)
placeholder = ""
symbols = "_"
while length > 0:
    length -= 1
    placeholder += symbols
print(placeholder)
display_temp = []
guess_list = []
display = ""
while display != chosen_word and Lives > 0:
    display = ""
    guess = input("Guess a letter: ").lower()
    if guess in guess_list:
        print("You've already guessed," + guess)
    for char in chosen_word:
        if guess == char:
            display += guess
            guess_list.append(guess)
        elif char in guess_list:
            display += char
        else:
            display += symbols

    if guess not in display:
        Lives -= 1
        item = stages.pop(Lives)
        print("You guessed", guess, "thagitt's not in the word. You lose a life.")
        print("You have " + str(Lives) + " lives left.")
        print(item)
    print(display)

    if "_" not in display:
        print(display)

if display == chosen_word:
    print("Congratulations! You guessed the word")
    print(display)
else:
    print("You Lose! The correct word was:", chosen_word )



