import ketboard

from random import choice
from sys import exit
from time import sleep

from ketboard import set_keyboard_color
from words import english_wordle_list, english_words_valid

import os
from termcolor import colored
os.system('color')

from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
from openrgb.utils import RGBColor

red = RGBColor(255, 0, 0)
green = RGBColor(0, 255, 0)
yellow = RGBColor(255, 255, 0)

cli = OpenRGBClient()
keyboard = cli.get_devices_by_type(DeviceType.KEYBOARD)[0]
keyboard.set_color(RGBColor(0, 0, 0))

#  Checks if user_word is in English word list
def word_validation(word_list, word):
    start = 0
    end = len(word_list) - 1

    while start <= end:
        middle = (start + end) // 2

        if word_list[middle] > word:
            end = middle - 1
        elif word_list[middle] < word:
            start = middle + 1
        else:
            return True

    return False


#  Returns random word depending on player's choice of game language
def choose_word():
    return choice(english_wordle_list)


#  Returns indications of correct/incorrent letter placements
def letter_placement(user_word_list):
    signs = ""
    for index, letter in enumerate(user_word_list):
        if letter == chosen_word[index]:
            state = 'green'
            signs += ' ' + colored(letter.upper(), state)
        elif letter in chosen_word:
            state = 'yellow'
            signs += ' ' + colored(letter.upper(), state)
        else:
            state = "red"
            signs += ' ' + colored(letter.upper(), state)
        ketboard.set_keyboard_color(letter, state)
    return signs


chosen_word = choose_word()


print("Type a word")

attempts = 0  # Doesn't include wrong inputs
user_word = ""  # This is what the user will put as input

while user_word != chosen_word:
    user_word = input("> ").strip().lower()
    if user_word.strip().lower() == "giveup":
        print(f"You gave up (total attempts: {attempts}), the correct answer was: {chosen_word.upper()}")
        input()
        exit()
        for i in range(3):
            keyboard.set_color(red)
            sleep(1)
            keyboard.set_color(RGBColor(0, 0, 0))
            sleep(1)

    attempts += 1

    #  Checks if user_word is valid - 5 chars. long, only letters, is in English words list
    while len(user_word) != 5: #or not user_word.isalpha() or not word_validation(english_words_valid, user_word):
        print("Wrong input, try again")
        user_word = input("> ").strip().lower()

    print(letter_placement(list(user_word)))


print(f"\nYOU WON, the correct answer was {chosen_word.upper()}\nTotal attempts: {attempts}")
for i in range(3):
    keyboard.set_color(green)
    sleep(1)
    keyboard.set_color(RGBColor(0,0,0))
    sleep(1)

input()